import sys, os

#reload(sys)
#sys.setdefaultencoding('utf-8') #The ensures that string output doesn't come back with a leading 'u', which is weird. 

#This is just specific to my computer. 
sys.path.append('C:\Users\Asaf\Documents\GitHub\TwitterIdentity\src\py')

import pymysql

import urlparse

import cPickle

import pickle

import facebook
from encrypt import *

from collections import defaultdict

from pyfaceb import*

path = 'E:\Participants'


#load the stored variable with ids and corresponding tokens for which we have access

conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='groupid', passwd='letspublish', db='gidb')
cur = conn.cursor()

query="Select AccessToken,fbid from fbconnectionaccounts JOIN users ON users.Id=fbconnectionaccounts.id WHERE length(AccessToken)>120;"

cur.execute(query) 

tokens_encr =cur.fetchall()


#This is the query to get all the people who 

query="Select AccessToken from fbconnectionaccounts JOIN survey ON survey.Id=fbconnectionaccounts.id WHERE (ended < '2014-04-16 1:26:03' AND length(AccessToken)>120);"

cur.execute(query) 

necessity_list=cur.fetchall()

query="Select AccessToken from fbconnectionaccounts JOIN survey ON survey.Id=fbconnectionaccounts.id WHERE (ended < '2014-06-16 1:26:03' AND length(AccessToken)>120) ORDER BY survey.ended ASC;"

cur.execute(query)

full_with_ended=cur.fetchall() # These are just all the people who finished the survey after we fixed the bug and weren't re-authenticating (presumably- because who would want to take this 2X and we informed people
#that they didn't need to take the survey again). In the query it's sorted by date, so we can hit the earliest ones first. 

cur.close()

full_with_ended=[decode_salt(full_with_ended[i][0]) for i in range(len(full_with_ended))]



necessity_tokens=[decode_salt(necessity_list[i][0]) for i in range(len(necessity_list))]






tokens_id = [(decode_salt(tokens_encr[i][1]),decode_salt(tokens_encr[i][0])) for i in range(0,len(tokens_encr))]


#run these first
initial_ids=[tokens_id[i][0] for i in range(len(tokens_id)) if tokens_id[i][1] in necessity_tokens]

ids_with_ended=[tokens_id[i][0] for i in range(len(token_id) if tokens_id[i][1] in full_with_ended]

fileObject=open(path+'/'+'tokens_id_full','w+')
cPickle.dump(tokens_id,fileObject)
fileObject.close()

pull_fields_friends=['accounts','books','movies', 'groups', 'achievements','activities', 'likes','events','feed',
'games','interests','music','television','statuses','posts','links']

ids_in_path=os.listdir(path)



corrupted=[]

friend_lengths=[]


for ids in ids_in_path[0:3]:
    try:
        friend_log={}
        unpack=open(path+'/'+ids+'/edges', 'r')
        edges=cPickle.load(unpack)
        unpack.close()
        friend_id=[i['id'] for i in edges['friends']['data']]
        friend_lengths.append(len(friend_id))
    except:
        print ids
        corrupted.append(ids)



all_id_files=[i for i in ids_in_path if i not in corrupted]


tokens_id = [(decode_salt(tokens_encr[i][1]),decode_salt(tokens_encr[i][0])) for i in range(0,len(tokens_encr))]

#Make a big batch request


#for ids in all_id_files[0:100]:

#The script crashed because I forgot to stipulate that the id, from initial_ids must be in the directory (those not in the directories will give an error, because you need to pull the friends_list from the edges_file. 

#So, here are the ones that have been run

done=['100000967142850',
 '82300945',
 '1376874268',
 '100000111561010',
 '689881408',
 '100001747138098',
 '100003398557331',
 '760193973',
 '1300860354',
 '100001457843972',
 '100000226225771',
 '100000779062049',
 '501811678',
 '603236380',
 '1051636786',
 '1720016845',
 '1079655524',
 '100003968217931',
 '1334542599',
 '1563823349']
 
 #Here is the new list:
 
urgent_id=[i for i in initial_ids if i not in done and i in all_id_files] # Basically I just take the files out everything that's been crawled and doesn't appear in the existing filing directory.

re_auth=[i for i in all_id_files if i not in ids_with_ended]

expire_later=[i for i in ids_with_ended if i not in initial_ids and i in all_id_files]

expire_later=list(set(expire_later))

not_working=[tokens_id[i][0] for i in range(len(tokens_id)) if tokens_id[i][0] not in all_id_files]

not_working=list(set(not_working))

#pickle everything in a dictionary so that I can use it in other scripts

y={}

y['urgent_id']=urgent_id
y['re_auth']=re_auth
y['expire_later']=expire_later
y['not_working']=not_working
y['tokens_id']=tokens_id

fileObject=open(path+'/crawl_lists', 'w+')

cPickle.dump(y,fileObject)

fileObject.close()




 #Now I also want to make a file that includes the next urgent list- people who will expire by June 14 (2 months from the day I sent out that massive email) . I unfortunately don't have the ended dates for these
 #people- because that was a variable that was only assigned after people completed the survey. BUT- I do know who did complete the survey for the first time (and likely wasn't just re-authenticating)
 #So, basically I can take the full list of ids- and subtract the list of people who have any kind of ended date (because they were not re-authenticating) and this will give me the flood of people who re-authenticated-
 #probably within a span of a day or two from April 15th. They should be the next priority. 
 
 




for ids in initial_ids:
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
        
        try:
            friend_info=fbg.batch(batch)
            print 'it is getting here 1'
            friends_batch[friend]=friend_info # add that friend's info to the dictionary
            print 'successfully pulled '+ friend
            
        except Exception as e:
            print e
            friend_batch_log[friend]=e
            friends_batch[friend]='error'
        
    unpack=open(path+'/'+ids+'/friends_batch', 'w+')
    
    cPickle.dump(friends_batch,unpack)
    unpack.close()
    unpack2=open(path+'/'+ids+'/friends_batch_log', 'w+')
    cPickle.dump(friend_log,unpack2)
    unpack2.close()
            
            

        
        
    
    
   
        
        