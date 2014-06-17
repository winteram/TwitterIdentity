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

conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='groupid', passwd='letspublish', db='gidb')
cur = conn.cursor()

query="Select AccessToken,fbid from fbconnectionaccounts JOIN users ON users.Id=fbconnectionaccounts.id WHERE length(AccessToken)>120;"

cur.execute(query) 

tokens_encr =cur.fetchall()

tokens = [decode_salt(tokens_encr[i][0]) for i in range(0,len(tokens_encr)) ]

ids = [decode_salt(tokens_encr[i][1]) for i in range(0,len(tokens_encr)) ] # this one doesn't really get used. An issue is that there are tokens for which the id was not 
#stored in the database. So, I later resort to just pulling the ids using the tokens and then pairing them that way. 

path = 'C:\Users\Asaf\Participants'

token_id=[]


#Need to recreate token_id variable, unfortunately, because of a problem I had pickling... whatevs

for i in tokens:
    try:
        
        oauth_access_token=i 
        graph = facebook.GraphAPI(oauth_access_token)
        profile=graph.get_object("me")
        
        ids=profile['id'].encode('utf8') # just takes that u' bit off
        token_id.append((i,ids))
        
    except Exception as e:
        print (e)
        
        
token_file=open(path +'/'+'token_id', 'w+')
cPickle.dump(token_id,token_file)
token_file.close()


object1=open(path+'/'+'token_id','r')
token_id=pickle.load(object1)

object1.close()


status_error={}

#make a temp dictionary just for testing purposes

#test1={}


for i in token_id:
    oauth_access_token=i[0]
    graph = facebook.GraphAPI(oauth_access_token)
    y=[]
    status_path= path + '/' + i[1] + '/statuses'
    status_file= open(status_path,'w+')
    limit=2000
    offset=0
    done = False 
    
    try:
        
        while offset < (limit+100) and done==False:
            
            k=graph.get_connections("me",'statuses', limit=100, offset=offset)
            y.append(k)
            offset += 100
            if len(k['data']) < 100:
                done=True

    except Exception as e:
        print (e)
        if i[1] in status_error.keys():
            status_error[i[1]].append(e)# I am making each user id the the key for my status_error variable. 
        else:
            status_error[i[1]]=[e]
    cPickle.dump(y,status_file)
    status_file.close()
    #ids=i[1]
    #test1[ids]=y
    
            
            
error_file=open(path +'/'+'status_error', 'w+')
cPickle.dump(status_error,error_file)
error_file.close()



