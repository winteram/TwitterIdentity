
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

import random
import numpy



SEED_SIZE=.5

DEVELOPMENT_SIZE=.3

TEST_SIZE=.2



conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='smalls7_groupid', passwd='LetsPublish!', db='smalls7_identity')
cur = conn.cursor()
#cur.execute("SELECT TwitterAccountNodeId, TwitterAccountParentId from relationship, survey where relationship.TwitterAccountNodeId = survey.Id;")

#biglist=cur.fetchall()


cur.execute("SELECT DISTINCT(survey.Id) FROM survey WHERE gender='F';")

#This is the list of Females

FemaleList=cur.fetchall()

FemaleList=[user[0] for user in FemaleList]




random.shuffle(FemaleList) # randomize these each time



UserNames=[] #This is a list with all the usernames as strings, not as tuples which is how they seem to be coming out.

FemaleNames=[]
MaleNames=[]


FemaleTweetSet=[] #Set of all Femaleublican Tweets

MaleTweetSet=[]


## Assign sets for seed, training, and testing.
for user in FemaleList:
    cur.execute("SELECT TweetText FROM tweet WHERE UserId='"+ user +"';")
    tweets=cur.fetchall()

    if len(tweets) > 0:
        FemaleNames.append(user)
        FemaleTweetSet.append(tweets)





cur.execute("SELECT DISTINCT(survey.Id) FROM survey WHERE gender = 'M';")
    
MaleList=cur.fetchall()

MaleList=[user[0] for user in MaleList]

random.shuffle(MaleList)





for user in MaleList:
    
    cur.execute("SELECT TweetText FROM tweet WHERE UserId='"+ user +"';")
    tweets=cur.fetchall()

    if len(tweets) > 0:
        MaleNames.append(user)
        MaleTweetSet.append(tweets)


#Should do some cleaning here before pickling- Basically all I need are two- raw- lists. One with all the tweets for each user, encapsulated by user, the other just one long list for of words for all the users- I can use the split function, as I had previously. Importantly- before doing bigrams and trigrams- after stuff has has been
#lower-cased, remove everything but alpha numeric stuff (this is after hashtags and urls have been pulled out. I say this because when I was playing with the trigram- there were periods and stuff. We don't want that- actually I could probably just run word tokenize or something on the list- does it work for a list, lets check. 


tweetText = ""


Tweets_by_user=""


Complete_Tweets=""



UserWordList=[]

full_Wordlist=[]


Seed_List=[]

Dev_List=[]

Test_List=[]


    
   
    
gender_list=[FemaleTweetSet,MaleTweetSet]




Seed_split=int(len(MaleNames)* SEED_SIZE)

Dev_split= Seed_split + int(len(MaleNames)*DEVELOPMENT_SIZE)    
    
    
    
    
for gender in gender_list:

    All_Tweets="" # This will get a raw string of all tweets for each gender
    genderUserWordlist=[] #This will collect all the tweets by users in a given gender


    for users in gender:
        
        Tweets_by_user=""
        
        
        
        for tweet in users:
            
            tweetText = tweet[0]
            
            
            Tweets_by_user=Tweets_by_user + " " + tweetText

        genderUserWordlist.append(Tweets_by_user.split()) # This separates the tweets for each user in list form- we can later use these to filter things


        All_Tweets=All_Tweets + " " + Tweets_by_user

    #   Complete_Tweets=Complete_Tweets + " " + All_Tweets # This is just a giant string with everything everyone has tweeted.

    #full_Wordlist.append(All_Tweets.split()) #This is a list with a list of all the words in the class



    IdList=[FemaleNames,MaleNames]

    Seed_List.append(genderUserWordlist[0:Seed_split])

    Dev_List.append(genderUserWordlist[Seed_split:Dev_split])

    Test_List.append(genderUserWordlist[Dev_split:])



    


    #UserWordList.append(genderUserWordlist)













#fileObject=open("WordLists",'w+')
#cPickle.dump(full_Wordlist,fileObject)

#fileObject.close()


fileObject=open("Seed_List",'w+')
cPickle.dump(Seed_List,fileObject)

fileObject.close()

fileObject=open("Dev_List",'w+')
cPickle.dump(Dev_List,fileObject)


fileObject.close()


fileObject=open("Test_List",'w+')
cPickle.dump(Test_List,fileObject)

fileObject=open("IdList",'w+')
cPickle.dump(IdList,fileObject)



fileObject.close()

