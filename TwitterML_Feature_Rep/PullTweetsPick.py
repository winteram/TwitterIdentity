import re
from random import randrange
from urllib import urlopen
from bs4 import BeautifulSoup
from twitter import *
from nltk import *
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from nltk.collocations import *
from numpy import*
import cPickle

import pymysql




conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='smalls7_groupid', passwd='LetsPublish!', db='smalls7_identity')
cur = conn.cursor()

cur.execute("SELECT DISTINCT(survey.Id) FROM survey WHERE party = 'republican';")

#This is the list of republicans

RepList=cur.fetchall()





UserNames=[] #This is a list with all the usernames as strings, not as tuples which is how they seem to be coming out.


RepTweetSet=[] #Set of all Republican Tweets

DemTweetSet=[]


### Go through test user names & get scores for each party
for user in RepList[0:40]:
   
    # get tweets of target user
    
    username=user[0]
    UserNames.append(username)
    
    cur.execute("SELECT TweetText FROM tweet WHERE UserId='"+ username +"';")

    tweets=cur.fetchall()
    
    RepTweetSet.append(tweets)

cur.execute("SELECT DISTINCT(survey.Id) FROM survey WHERE party = 'democrat';")

DemList=cur.fetchall()


for user in DemList[0:40]:
    
    # get tweets of target user
    
    username=user[0]
    UserNames.append(username)
    
    cur.execute("SELECT TweetText FROM tweet WHERE UserId='"+ username +"';")
    
    tweets=cur.fetchall()
    
    DemTweetSet.append(tweets)



fileObject=open("RepList",'w+')

cPickle.dump(RepTweetSet,fileObject)

fileObject.close()

fileObject=open("DemList",'w+')

cPickle.dump(DemTweetSet,fileObject)

fileObject.close()











    
    
   