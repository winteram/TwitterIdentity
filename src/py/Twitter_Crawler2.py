import sys, os

#reload(sys)
#sys.setdefaultencoding('utf-8') #The ensures that string output doesn't come back with a leading 'u', which is weird. 

#This is just specific to my computer. 
# sys.path.append('C:\Users\Asaf\Documents\GitHub\TwitterIdentity\src\py')

import pymysql
import cPickle
from encrypt import *
from twitter import *

#The following fields are constants
CONSUMER_KEY = 'zhew9FPCoQGPRnR4PHPB3A'
CONSUMER_SECRET = 'ToHQwjgWSX4v3NUsRxe7IthQ6TUmTT78bJKcDIey7LY'


# CONSUMER_KEY = '4KGJAk29GXnlniKVqSmZoLbP8'
# CONSUMER_SECRET = 'd3QP1Zr05sYjqzguZJzhP0BsiHaNVhtbG0z0BFY5aOCqOOlP3r'
#oauth_token='625200110-OAgXw6qs3GlYxs4RKJLKv0S6SIMp9GzSAOpRXhmg'
#oauth_secret= 'TOVaGhvptuQGl0TW0pXVwFmmW3QSsZvG4O4REaIBenc'



#CONSUMER_KEY = "PCMmY6ERIWJM9tgjIiQRwA"
#CONSUMER_SECRET = "YWeRQPivyjc9ZUSLQbaFj8enJviPZ8cw55mu3qSuJdk"
'''

I believe that oauth_token and oauth_secret are varialbes, which I will pull for each participant. These will just
be pulled out wit ids and then parsed in the following code.

'''

conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='groupid', passwd='letspublish', db='gidb')
cur = conn.cursor()


query="Select t.Id,AccessTokenSecret,AccessToken,FBid,Twitid,IUname from twitterconnectionaccounts t join users u on t.Id=u.Id and IUname='wimason'"

cur.execute(query)

raw=cur.fetchall()

#decoded

clean_again=[(raw[i][0],decode_salt(raw[i][1]), decode_salt(raw[i][2]), decode_salt(raw[i][3])) for i in range(0,len(raw))]

#undecoded

#clean_again=[(raw[i][0],raw[i][1], raw[i][2]) for i in range(0,621)]

#This is a little bizarre, I can't seem to decode the last 3. 

#w=(raw[621][0],decode_salt(raw[621][1]), decode_salt(raw[621][2]))


for i in clean_again:
	oauth_token=i[2]
	oauth_secret=i[1]
	user=i[3]
	print "OAuth token: " + oauth_token
	print "OAuth secret: " + oauth_secret
	response = raw_input("Get user " + user + "?")
	if response == 'y':
		try:
			t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET)) 
			status = t.statuses.user_timeline(count=200)
			print "Success"
			print status[0]
		except TwitterHTTPError as e:
			print e
			continue
	if response == 'q':
		break
	else:
		continue
	








