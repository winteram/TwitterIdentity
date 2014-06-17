'''
This is just a simple script to start picking up all the keys available in user- and then in connection stuff

'''

import sys, os

#reload(sys)
#sys.setdefaultencoding('utf-8') #The ensures that string output doesn't come back with a leading 'u', which is weird. 

#This is just specific to my computer. 
#sys.path.append('C:\Users\Asaf\Documents\GitHub\TwitterIdentity\src\py')

import pymysql

import pymysql
import facebook
from encrypt import *


# Set up connection
conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='groupid', passwd='letspublish', db='gidb')
cur = conn.cursor()

query="SELECT AccessToken FROM fbconnectionaccounts WHERE length(AccessToken) >120" #take all tokens from our users that are valid, i.e. are over 120 characters
cur.execute(query)

#Assign a variable to the encrypted tokens
tokens_encr =cur.fetchall()

#decrypt the tokens 
tokens = [decode_salt(tokens_encr[i][0]) for i in range(0,len(tokens_encr)) ]

#Initialize a variable that will contain all the keys that we generate. 
full_keys=[]


#loop through and grab keys. 
for i in tokens[0:50]:
    try:
        graph = facebook.GraphAPI(i) 
        profile = graph.get_object("me")
        k=profile.keys()
        full_keys.append(k)
    except:
        pass


pull_fields=['accounts','books','movies', 'groups', 'achievements', 'accounts','activities', 'likes','events','family','feed',
'friends', 'games', 'groups','home','interests','music','scores','television']

keys=[keys for keylists in full_keys for keys in keylists]
final_profile=set(keys)

#I am initializing a dictionary with dictionary keys. I will append to the keys upon iterations and then create a new dictionary
#which will have the same keys but take the set of the values. 

keys_full={}

#before I can append to values in this dictionary, I need to initialize keys with an array. So, I will just give each one an empty array.

for field in pull_fields:
    keys_full[field]=[]
    

for i in tokens[0:20]:
    try:
        graph = facebook.GraphAPI(i)
        for field in pull_fields:
            y[field]=graph.get_connections("me",field, limit=3)
            keys_full[field].append(y[field]['data'].keys())
    except:
        pass
            
            
            
            
         
    




'''
This will be an experiment in seeing if the since parameter works'''


  