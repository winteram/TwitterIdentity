
#Pull Twitter tokens and ids from participants


import sys, os

#reload(sys)
#sys.setdefaultencoding('utf-8') #The ensures that string output doesn't come back with a leading 'u', which is weird. 

#This is just specific to my computer. 
sys.path.append('C:\Users\Asaf\Documents\GitHub\TwitterIdentity\src\py')

import pymysql

import cPickle

from encrypt import *

conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='groupid', passwd='letspublish', db='gidb')
cur = conn.cursor()


query="Select AccessToken, Id from twitterconnectionaccounts"

cur.execute(query)


cur.execute(query) 

tokens_encr =cur.fetchall()

#tokens = [decode_salt(tokens_encr[i][0]) for i in range(0,len(tokens_encr)) ]