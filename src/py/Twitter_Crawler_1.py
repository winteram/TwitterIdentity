
#Pull Twitter tokens and ids from participants


import sys, os

#reload(sys)
#sys.setdefaultencoding('utf-8') #The ensures that string output doesn't come back with a leading 'u', which is weird. 

#This is just specific to my computer. 
sys.path.append('C:\Users\Asaf\Documents\GitHub\TwitterIdentity\src\py')

import pymysql

import cPickle

from encrypt import *

import twitter


oauth_token = '52324123-0oMlVHSvfhTZm7eeP1HEK8B8pQWR0GsBi1Ba6MQbd'

oauth_secret = 'xA1MEXL7ELow4HJT5snjYgb0nwXQOW1wmQBYu3PxcX4wK'

CONSUMER_KEY = "PCMmY6ERIWJM9tgjIiQRwA"
CONSUMER_SECRET = "YWeRQPivyjc9ZUSLQbaFj8enJviPZ8cw55mu3qSuJdk"

conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='groupid', passwd='letspublish', db='gidb')
cur = conn.cursor()


query="Select AccessToken, Id from twitterconnectionaccounts"

cur.execute(query)


cur.execute(query) 

tokens_encr =cur.fetchall()


tokens = [decode_salt(tokens_encr[i][0]) for i in range(len(tokens_encr)-1)]


conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='groupid', passwd='letspublish', db='gidb')
cur = conn.cursor()


query="Select AccessToken from twitterconnectionaccounts"

cur.execute(query)

secret=cur.fetchall()

cur.close()





