import pymysql
import cPickle
import facebook
from encrypt import *



#This will pull one person's information in its entirety, but I will write it as a loop, eventually

# Set up connection
conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='groupid', passwd='letspublish', db='gidb')
cur = conn.cursor()

query="SELECT AccessToken FROM fbconnectionaccounts WHERE length(AccessToken) >120" #take all tokens from our users that are valid, i.e. are over 120 characters
cur.execute(query)

#Assign a variable to the encrypted tokens
tokens_encr =cur.fetchall()

#decrypt the tokens 
tokens = [decode_salt(tokens_encr[i][0]) for i in range(0,len(tokens_encr)) ] 

#Note: I can pickle these tokens for quicker access, so we don't have to query the db each time the script runs. Also, I can order the tokens by time
for i in tokens[0:1]:
    oauth_access_token=tokens[i] # take an example token. This is what I will use to demonstrate all the queries we are interested. 
    
    graph = facebook.GraphAPI(oauth_access_token) 
    
    
    
    profile = graph.get_object("me") # Get all the profile information. 
    
    friends = graph.get_connections("me", "friends")
    
    feed=graph.get_connections("me","feed", limit=100)
    
    
    friend_ids=[friends['data'][i]['id'] for i in range(0,len(friends['data']))]
    
    #pull info from friend- all the commands follow this simple format. Everything is the same as above, but we use the friend
    #ID instead of 'me'. 
    
    
    
    
    
    
    likes_friend=graph.get_connections(friend_ids[3],"likes")
    
    
    
fileObject=open("Seed_List",'w+')
cPickle.dump(Seed_List,fileObject)

fileObject.close()