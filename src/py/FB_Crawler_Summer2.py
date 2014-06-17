
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


conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='groupid', passwd='letspublish', db='gidb')
cur = conn.cursor()

query="Select AccessToken,fbid from fbconnectionaccounts JOIN users ON users.Id=fbconnectionaccounts.id WHERE length(AccessToken)>120;"

cur.execute(query) 

tokens_encr =cur.fetchall()

tokens = [decode_salt(tokens_encr[i][0]) for i in range(0,len(tokens_encr)) ]

ids = [decode_salt(tokens_encr[i][1]) for i in range(0,len(tokens_encr)) ] # this one doesn't really get used. An issue is that there are tokens for which the id was not 
#stored in the database. So, I later resort to just pulling the ids using the tokens and then pairing them that way. 

path = 'C:\Users\Asaf\Participants'

object1=open(path+'/'+'tokens_id_full','r')
token_id=pickle.load(object1)

object1.close()







#Make a dictionary that will house every error for any given id in a list

error_log={}


  #This code just makes a file for each participant, the file name is the facebook id of the participant.   

if not os.path.exists(path):
    os.makedirs(path)

for i in tokens:
    try:
        
        oauth_access_token=i 
        graph = facebook.GraphAPI(oauth_access_token)
        profile=graph.get_object("me")
        
        ids=profile['id'].encode('utf8') # just takes that u' bit off
        token_id.append((i,ids))
        id_direct=path + '/' + ids
        if not os.path.exists(id_direct):
            os.makedirs(id_direct)
        file_profile=open(id_direct +'/' + "profile",'w+')
        cPickle.dump(profile,file_profile)
        file_profile.close() 
    except Exception as e:
        print (e)
        bad_token.append(i)

pull_fields=['accounts','books','movies', 'groups', 'achievements','activities', 'likes','events','family','feed',
'friends', 'games', 'groups','home','interests','music','scores','television','statuses','posts','links'] 

token_file=open(path +'/'+'token_id', 'w+')
cPickle.dump(token_id,token_file)

for i in token_id:
    oauth_access_token=i[0]
    graph = facebook.GraphAPI(oauth_access_token)
    y={}
    
    try:
        for field in pull_fields:
            y[field]=graph.get_connections("me",field, limit=5000)
            edges_path= path + '/' + i[1] + '/edges'
            edges_file= open(edges_path,'w+')
            cPickle.dump(y,edges_file)
            edges_file.close()
    except Exception as e:
        print (e)
        if i[1] in error_log.keys():
            error_log[i[1]].append(e)
        else:
            error_log[i[1]]=[e]
            
            

error_file=open(path +'/'+'error_log', 'w+')
cPickle.dump(error_log,error_file)
error_file.close()


error_clean={}    
for i in error_log.keys():
    if error_log[i] != []:
        error_clean[i]=error_log[i]

retry_list=[i for i in token_id if token_id[i][1] in error_clean.keys()]


error_file=open (path +'/'+'retry1', 'w+')
cPickle.dump(retry_list,error_file)
    

       
error_log2={}

for i in retry_list:
    oauth_access_token=i[0]
    graph = facebook.GraphAPI(oauth_access_token)
    y={}
    
    try:
        for field in pull_fields:
            y[field]=graph.get_connections("me",field, limit=2000)
            edges_path= path + '/' + i[1] + '/edges_retry'
            edges_file= open(edges_path,'w+')
            cPickle.dump(y,edges_file)
            edges_file.close()
    except Exception as e:
        print (e)
        if i[1] in error_log2.keys():
            error_log2[i[1]].append(e)
        else:
            error_log2[i[1]]=[e]



error_file=open(path +'/'+'error_log2', 'w+')
cPickle.dump(error_log,error_file)





#Code to get feed, home, posts, links

error_log_2_pull={}

second_pull=['home','feed','posts','links']

for i in token_id:
    oauth_access_token=i[0]
    graph = facebook.GraphAPI(oauth_access_token)
    y={}
    
    try:
        for field in second_pull:
            y[field]=graph.get_connections("me",field, limit=5000)
            edges_path= path + '/' + i[1] + '/edges_2'
            edges_file= open(edges_path,'w+')
            cPickle.dump(y,edges_file)
            edges_file.close()
    except Exception as e:
        print (e)
        if i[1] in error_log_2_pull.keys():
            error_log_2_pull[i[1]].append(e)
        else:
            error_log_2_pull[i[1]]=[e]
            
            
file=open(path +'/'+'error_log_2_pull', 'w+')
error_file=open(path +'/'+'error_log_2_pull', 'w+')
cPickle.dump(error_log_2_pull,error_file)
 
    



token_onward=[i for i in token_id if i not in retry_list]


group_error_log={}

error_id_list=[]

pull_group=["admins","events","feed","members","docs","files"]

for i in token_onward:
        oauth_access_token=i[0]
        graph = facebook.GraphAPI(oauth_access_token)
        object1=open(path+'/'+i[1]+'/'+'edges', 'r')
        edge=cPickle.load(object1)
        ids1=i[1]
        group_info={}
        group_info_path=open(path + '/' + ids1 + '/' + 'group_info', 'w+')

        
        for j in edge['groups']['data']:
            try:
                ids=j['id']
                group_info[ids]={} #just indexing the dictionary with the id, and an empty dictionary
                
                profile=graph.get_object(ids)
                
                group_info[ids]['profile']=profile
                
                if profile['privacy']=='CLOSED':
                    for field in pull_group:
                        group_info[ids][field]=graph.get_connections(ids,field,limit=1500)
                
               
                
                 
            except Exception as e:
                print (e)
                if ids in group_error_log.keys():
                    
                    group_error_log[ids].append(e)
                else:
                    group_error_log[ids]=[e]
                    

        
        try:
            cPickle.dump(group_info,group_info_path)
            group_info_path.close()
        except:
            print('could not pickle', [i][1])
            error_id_list.append(i[1])

        
        
#Piece of code to retry stuff in a more systematic way and to actually store the file with errors- before I forgot to close the file in the code,
#Which messed things up.

error_log={}

for i in newlist:
    oauth_access_token=i[0]
    graph = facebook.GraphAPI(oauth_access_token)
    y={}
    
    for field in pull_fields:
        
        try:
            y[field]=graph.get_connections("me",field, limit=3000)
            edges_path= path + '/' + i[1] + '/edges_2'
            edges_file= open(edges_path,'w+')
            cPickle.dump(y,edges_file)
            edges_file.close()
        except Exception as e:
            print (e)
            
            if i[1] in error_log.keys():
                error_log[i[1]].append([e,field])
            else:
                error_log[i[1]]=[[e,field]]
            y[field]='error'
            edges_path= path + '/' + i[1] + '/edges_2'
            edges_file= open(edges_path,'w+')
            cPickle.dump(y,edges_file)
            edges_file.close()
            
            
error_file=open(path +'/'+'error_log_retry2', 'w+')
cPickle.dump(error_log,error_file)
error_file.close()


#Code to pull friends






pull_fields_friends=['accounts','books','movies', 'groups', 'achievements', 'accounts','activities', 'likes','events','feed',
'friends', 'games', 'groups','interests','music','scores','television','statuses','posts','links']

ids_in_path=os.listdir(path)

for ids in ids_in_path:
    friend_log={}
    unpack=open(path+'/'+ids+'/edges', 'r')
    edges=cPickle.load(unpack)
    unpack.close()
    friend_id=[i['id'] for i in edges['friends']['data']]
    y=defaultdict(dict) # Make sure that y gets initialized in a way that I can assign values to it as an embedded dictionary
    #get a token for each person
    
    token=[j[0] for j in token_id if j[1]==ids]
    
    
    
    graph = facebook.GraphAPI(token[0])
    
    for friend in friend_id:
        try:
            y[friend]['profile'] = graph.get_object(friend)
        except Exception as e:
            print e
            if friend in friend_log.keys():
                friend_log[friend].append(e)
            else:
                friend_log[friend]=[e]
            y[friend]['profile']='error'
    
    unpack=open(path+'/'+ids+'/friends', 'w+')
    cPickle.dump(y,unpack)
    unpack.close()
    unpack2=open(path+'/'+ids+'/friends_log', 'w+')
    cPickle.dump(friend_log,unpack2)
    unpack2.close() 


          
    
        
        
        
        
    

    





         
            
        
        


        

