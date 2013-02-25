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


### Go through test user names & get scores for each party
for user in RepList[0:20]:
   
    # get tweets of target user
    
    username=user[0]
    UserNames.append(username)
    
    cur.execute("SELECT TweetText FROM tweet WHERE UserId='"+ username +"';")

    tweets=cur.fetchall()
    
    RepTweetSet.append(tweet)
    
    
        
    tweetText = ""
    tweetWordCount = 0
    weTweetWordCount = 0
    WeTweetSet=[] # This will be the vector that stores all tweets containing "we" words- it will be of length TotalDist for the dot product stuff.
    WeTweetScore=[]
    TweetScore=[]
    TweetSet=[] #This is the set of all tweets
    
    
    for tweet in tweets:
        # clean tweet text & tokenize
        tweetText = tweet[0]    #.encode('utf8')
        
        
        #Note: with the UTF8 encoding a lot of this reg-expression cleanup is not necessary.
        
        tweetText = re.sub('[^.a-zA-Z1-9 #/:-]', '', tweetText)
        tweetText = re.sub('(?P<endword>[a-z]+)(?P<begword>[A-Z])', '\g<endword> \g<begword>', tweetText)
        tweetText = tweetText.lower()
        #Note I think we should preserve case sensitivity because things like "FED" vs "fed", "US" vs "us". However, this might get captured better when we use n-grams
        
        tweet_wordlist = word_tokenize(tweetText)
        #tweetWordCount += len(tweet_wordlist) This is unneccessary
        weTweetWC = len(list(set(tweet_wordlist) & set(wewords)))
        # see if tweet has "we" word(s) in it
        TweetSet.append(tweet_wordlist)
        has_we = False
        if weTweetWC>0:
            has_we = True
            WeTweetSet.append(tweet_wordlist) #put each tweet in the list of we_tweets
    WeFreq=FreqDist([word for sublist in WeTweetSet for word in sublist]) #Make a term frequency distribution for we containing tweets
    AllFreq=FreqDist([word for sublist in TweetSet for word in sublist]) # Freq dist for all tweets
    r_AllFreq=AllFreq.freq
    
    b=len(TotalDist.keys())*[0]
    c=len(TotalDist.keys())*[0]
    
    for i,word in enumerate(TotalDist.keys()):
        
        b[i] = WeFreq[word]
        c[i] = r_AllFreq(word)  # Now this is relative frequency
    for i in range(len(listnames)):
        
        we_temp=cosine_distance(b,wordRats[i]) # 2nd term will be: wordRats[i]
        all_temp=cosine_distance(c,wordRats[i])
        
        
        TweetScore.append(all_temp)
        WeTweetScore.append(we_temp)

        if i == 0:
            DemScores.append(all_temp)
        else:
            RepScores.append(all_temp)



    TweetScore[:len(listnames)] = [str(x) for x in TweetScore[:len(listnames)]]
    WeTweetScore[:len(listnames)] = [str(x) for x in WeTweetScore[:len(listnames)]]






    print username, " ".join(TweetScore)
    print username, " ".join(WeTweetScore)





#for ID in IDs:
# Get tweets of participants' followers

### Create dataset for predicting political identity ###


# Create dictionary of words relevant to political identity (to use for word counting in tweets)

# Get counts of words in dictionary in own tweets
# Get counts of words in dictionary in own tweets with "we" words
# Get counts of words in dictionary in own tweets with "I" words
# Get valence of own tweets with words in dictionary
# Get counts of LIWC categories for own tweets

# Get counts of words in dictionary in own posted URLs
# Get counts of LIWC categories for own posted URLs

# Get counts of words in dictionary in friends tweets
# Get valence of friends tweets with words in dictionary
# Get counts of LIWC categories for friends tweets

# Get counts of words in dictionary in followers tweets
# Get valence of followers tweets with words in dictionary
# Get counts of LIWC categories for followers tweets


### Identify strong groups (using, e.g., LDA) ###


