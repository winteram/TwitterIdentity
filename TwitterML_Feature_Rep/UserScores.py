

from __future__ import division
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
import httplib
import urlparse
import cPickle
import pymysql
import operator
from stemming.porter2 import stem
import copy

object1=open('k_words','r')
k_words=cPickle.load(object1)

conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='smalls7_groupid', passwd='LetsPublish!', db='smalls7_identity')
cur = conn.cursor()


cur.execute("SELECT DISTINCT(survey.Id) FROM survey;")

all_user_id=cur.fetchall()

UnigramDict={}

TweetsByUsers=[] # This will eventually give us all the tweets in semi-tokenized form, for each user
for user in all_user_id[1000:1020]:
    username=user[0]
    cur.execute("SELECT TweetText FROM tweet WHERE UserId='"+ username +"';")
    temptweets1=cur.fetchall()
    # I am pretty sure I can assign scores and dictionary elements here. I need to import the K-vectors, though.
    TweetforUser=""
    raw=[]

    for tweets in temptweets1:
        
        TweetforUser=TweetforUser + " " + tweets[0]# This is just the tweets by user

    raw=TweetforUser.split()
    raw_for_unigram=[re.sub('[^a-zA-Z ]','',word).lower() for word in raw]
    raw_for_unigram=[word for word in k_words[0]+k_words[1]]
    raw_uni_freq=FreqDist(raw_for_unigram)
    
    
    
    



    TweetsByUsers.append(TweetforUser.split())





        
    
    
 
        
        