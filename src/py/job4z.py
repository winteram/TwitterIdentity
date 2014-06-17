import cPickle

import pickle

import facebook

import time


from collections import defaultdict

from pyfaceb import*

path = 'E:\Participants'

K=open(path+'/crawl_lists','r')

to_crawl=cPickle.load(K)

urgent_id=to_crawl['urgent_id']

tokens_id=to_crawl['tokens_id']

re_crawl_list=[]

K.close()

re_auth=to_crawl['re_auth']

expire_later=to_crawl['expire_later']


pull_fields_friends=['accounts','books','movies', 'groups', 'achievements','activities', 'likes','events','feed',
'games','interests','music','television','statuses','posts','links']

print 'now it should hang'


#new_list=re_auth[139:140]+re_auth[155:160]+re_auth[276:280]+re_auth[236:240]



for ids in expire_later[150:]:
    friends_batch={} #initialize a dictionary where each key will be a friend's id and the value will be a tuple containing the batched information about this person
    token=[j[1] for j in tokens_id if j[0]==ids] #Take tokens associated with ids out.
    k=token[0] # since some people authenticated twice, there are two tokens for a given id.- Arbitrarily take one of them. They all seem to work. 
    friend_log={} #Initialize dictionary that will store errors, where the keys are friend ids. 
    unpack=open(path+'/'+ids+'/edges', 'r') # Open the existing file where friends are stored
    edges=cPickle.load(unpack)
    unpack.close()
    fbg = FBGraph(k)# k is the token we are using
    friend_batch_log={}
    
    friend_id=[i['id'] for i in edges['friends']['data']]# pull out each person's friend list
    
    for friend in friend_id: # Loop through each friend and make a batch request
        batch=[GetRequestFactory(friend)]#initialize the batch variable with profile info
        
        #Populate batch request with everything in the pull_fields_friends list
        for field in pull_fields_friends:
            batch.append(GetRequestFactory(friend +'/'+field, limit=200)) # Set limit to 200- most of them time what will be more than is returned.
        time.sleep(1.1)
        try:
            friend_info=fbg.batch(batch)
            print 'it is getting here 1'
            friends_batch[friend]=friend_info # add that friend's info to the dictionary
            print 'successfully pulled '+ friend
            
            
        except Exception as e:
            print e
            friend_batch_log[friend]=e
            friends_batch[friend]='error'
        try:
            if friends_batch[friend][1]['body']['error']['message']=='(#4) Application request limit reached':
                print 'paused'
                time.sleep(7200)
                re_crawl_list.append(friend)
        except:
            pass
                
                   
        
    unpack=open(path+'/'+ids+'/friends_batch', 'w+')
    to_recrawl=open(path+'/to_recrawl', 'w+')
    cPickle.dump(re_crawl_list,to_recrawl)
    to_recrawl.close()
    cPickle.dump(friends_batch,unpack)
    unpack.close()
    unpack2=open(path+'/'+ids+'/friends_batch_log', 'w+')
    cPickle.dump(friend_log,unpack2)
    unpack2.close()