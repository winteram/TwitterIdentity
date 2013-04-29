


# These makes general function for positive and negative sets


#sys.path.append('/Users/Asaf/Documents/TwitterIdentity/TwitterML_Feature_Rep')
#os.chdir('/Users/Asaf/Documents/TwitterIdentity/TwitterML_Feature_Rep')

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
from collections import defaultdict




conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='smalls7_groupid', passwd='LetsPublish!', db='smalls7_identity')

cur = conn.cursor()

cur.execute("SELECT TwitterAccountNodeId, TwitterAccountParentId from relationship, survey where relationship.TwitterAccountNodeId = survey.Id;")

biglist=cur.fetchall()

SEED_SIZE=.5

DEVELOPMENT_SIZE=.3

TEST_SIZE=.2



Ufollowers=defaultdict(list)



for name,follower in biglist:
    Ufollowers[name].append(follower)


cur.execute("SELECT DISTINCT(survey.Id) FROM survey WHERE party = 'republican';")

#This is the list of republicans

RepList=cur.fetchall()

RepList=[user[0] for user in RepList]

RepList=[name for name in RepList if name in Ufollowers.keys()]




random.shuffle(RepList) # randomize these each time



UserNames=[] #This is a list with all the usernames as strings, not as tuples which is how they seem to be coming out.

RepNames=[]
DemNames=[]


RepTweetSet=[] #Set of all Republican Tweets

DemTweetSet=[]

DemFollows=[] #Set of names the participant follows

RepFollows=[] 


## Assign sets for seed, training, and testing.
for user in RepList:
    cur.execute("SELECT TweetText FROM tweet WHERE UserId='"+ user +"';")
    tweets=cur.fetchall()

    if len(tweets) > 0:
        RepNames.append(user)
        RepTweetSet.append(tweets)
        RepFollows.append(Ufollowers[user])





cur.execute("SELECT DISTINCT(survey.Id) FROM survey WHERE party = 'democrat';")
    
DemList=cur.fetchall()

DemList=[user[0] for user in DemList]

DemList=[name for name in DemList if name in Ufollowers.keys()]

random.shuffle(DemList)










for user in DemList:
    
    cur.execute("SELECT TweetText FROM tweet WHERE UserId='"+ user +"';")
    tweets=cur.fetchall()

    if len(tweets) > 0:
        DemNames.append(user)
        DemTweetSet.append(tweets)
        DemFollows.append(Ufollowers[user])



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


 #Note this assumes, as in our sample there are more Democrats than republicans. I can make this more general later...   
   
    
Party_list=[DemTweetSet,RepTweetSet]




Seed_split=int(len(RepNames)* SEED_SIZE)

Dev_split= Seed_split + int(len(RepNames)*DEVELOPMENT_SIZE)    
    
    
    
    
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

    #full_Wordlist.append(All_Tweets.split()) #This is a list with a list of all the words in the class

    

    IdList=[DemNames,RepNames]


    Seed_List.append(PartyUserWordlist[0:Seed_split])

    Dev_List.append(PartyUserWordlist[Seed_split:Dev_split])

    Test_List.append(PartyUserWordlist[Dev_split:])



    


    #UserWordList.append(PartyUserWordlist)



Seed_Follow=[DemFollows[0:Seed_split],RepFollows[0:Seed_split]]

Dev_Follow=[DemFollows[Seed_split:Dev_split],RepFollows[Seed_split:Dev_split]]

Test_Follow=[DemFollows[Dev_split:],RepFollows[Dev_split:]]










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

fileObject=open("Seed_Follow",'w+')
cPickle.dump(Seed_Follow,fileObject)

fileObject.close()

fileObject=open("Dev_Follow",'w+')
cPickle.dump(Dev_Follow,fileObject)

fileObject.close()

fileObject=open("Test_Follow",'w+')
cPickle.dump(Test_Follow,fileObject)

fileObject.close()











    

    


    






    
    

