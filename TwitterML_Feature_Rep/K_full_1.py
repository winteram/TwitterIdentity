


# These makes general function for positive and negative sets

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
    
    username=user[0] #The username is the first element in a tuple
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


#Should do some cleaning here before pickling- Basically all I need are two- raw- lists. One with all the tweets for each user, encapsulated by user, the other just one long list for of words for all the users- I can use the split function, as I had previously. Importantly- before doing bigrams and trigrams- after stuff has has been
#lower-cased, remove everything but alpha numeric stuff (this is after hashtags and urls have been pulled out. I say this because when I was playing with the trigram- there were periods and stuff. We don't want that- actually I could probably just run word tokenize or something on the list- does it work for a list, lets check. 


tweetText = ""


Tweets_by_user=""


Complete_Tweets=""



UserWordList=[]

full_Wordlist=[]


    
    
    
Party_list=[DemTweetSet,RepTweetSet]
    
    
    
    
    
for party in Party_list:

    All_Tweets="" # This will get a raw string of all tweets for each party
    PartyUserWordlist=[] #This will collect all the tweets by users in a given party


    for users in party:
        
        Tweets_by_user=""
        
        
        
        for tweet in users:
            
            tweetText = tweet[0]
            
            
            Tweets_by_user=Tweets_by_user + " " + tweetText

        PartyUserWordlist.append(Tweets_by_user.split()) # This separates the tweets for each user in list form- we can later use these to filter things


        All_Tweets=All_Tweets + " " + Tweets_by_user

    #   Complete_Tweets=Complete_Tweets + " " + All_Tweets # This is just a giant string with everything everyone has tweeted.

    full_Wordlist.append(All_Tweets.split()) #This is a list with a list of all the words in the class
    UserWordList.append(PartyUserWordlist)



fileObject=open("WordLists",'w+')
cPickle.dump(full_Wordlist,fileObject)

fileObject.close()



fileObject=open("WordsByUser",'w+')
cPickle.dump(UserWordList,fileObject)

fileObject.close()




    

    


    






    
    

