
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

#Note: I can pickle these tokens for quicker access, so we don't have to query the db each time the script runs. Also, I can order the tokens by time

oauth_access_token=tokens[4] # take an example token. This is what I will use to demonstrate all the queries we are interested. 

graph = facebook.GraphAPI(oauth_access_token) 



profile = graph.get_object("me") # Get all the profile information. 

#The abobe profiles variable comes out as a Python dictionary. Below are example commands we need to get specific info. Remember to later add .encode('utf8') to take the leading 'u' off strings. 
#All the information is stored as strings.
#Different people will have different profile different dictionary keys- depending on what is listed in their profile. So,we can just use: profile.keys(), 
# to see what information they have and pull only from those fields (instead of, say, doing a try, except statement). 


gender = profile['gender']


if 'languages' in profile.keys():
    
    languages = profile['languages']



#This gives access to the entire homescreen, I think as many pages back as we want. The limit just has to be specified.

home=graph.get_connections("me","home", limit=200) 

#the variable home scomes out as a set of nested dictionaries.
#home['data'] contains most of the info we want. There are a number of types of entities here- like pictures, links, and status updates. Each can have different fields
#and they don't include null fields. So, what appears in the dictionary are only the fields for which there is information (there aren't entries for null fields. 
#Here is an example of some keys: 
#[u'picture',u'story', u'from', u'privacy', u'actions', u'updated_time', u'application', u'link', u'story_tags', u'created_time', u'type', u'id', u'icon']



#Pull friends for this sample user
friends = graph.get_connections("me", "friends")

feed=graph.get_connections("me","feed", limit=100)





friend_ids=[friends['data'][i]['id'] for i in range(0,len(friends['data']))]

#pull info from friend- all the commands follow this simple format. Everything is the same as above, but we use the friend
#ID instead of 'me'. 






likes_friend=graph.get_connections(friend_ids[3],"likes")


    



