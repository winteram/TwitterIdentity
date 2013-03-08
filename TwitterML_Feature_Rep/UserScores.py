

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


regex1=re.compile(r'(https?://\S+)') #This pulls the whole url.

regex2=re.compile("(?P<url>https?://[^\s/]+)")# This specifically pulls stems of URLs

UnigramDict={}
UnigramaltDict={}

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
    raw_URLforUser=[regex1.findall(word) for word in raw]
    #The findall function puts the output in brackets, so the next function is to take the brackets out- so it's no longer a nested list. 
    UserUrl=[word for words in raw_URLforUser for word in words]
    raw_HashforUser=[word for word in raw if word.startswith('#')]
    Hash_final=[word.lower() for word in raw_HashforUser]
    raw_MentionforUser=[word for word in raw if word.startswith('@')]

    unigram1=[re.sub('[^a-zA-Z ]','',word).lower() for word in raw if word not in UserUrl + raw_HashforUser+ raw_MentionforUser and len(word) > 2]

    unigram_for_scoring=[word  for word in unigram1 if word in k_words[0] + k_words[1]]

    unigramFreq=FreqDist(unigram_for_scoring)

    G1_score=[]

    #Make this into a function later- because it's the same dynamics for all the features- or perhaps I could use a list comprehension

    for words in k_words[0]:
        v=unigramFreq.freq(word)
        G1_score.append(v)


    G1_score_alt=[unigramFreq.freq(word) for word in k_words[0]]

    UnigramDict[username]=G1_score

    UnigramaltDict[username]=G1_score_alt

























    #G1URL_temp=[regex1.findall(word) for word in wordlists[0]] # takes out all the full URLs, but puts them as a set of lists

#G1FullURL=[word for words in G1URL_temp for word in words]

    
    TweetsByUsers.append(TweetforUser.split())






#raw=TweetforUser.split()
#raw_for_unigram=[re.sub('[^a-zA-Z ]','',word).lower() for word in raw]
#raw_for_unigram=[word for word in k_words[0]+k_words[1]]
    
#raw_uni_freq=FreqDist(raw_for_unigram)

        
    
    
 
        
        