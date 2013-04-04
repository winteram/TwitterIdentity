

from __future__ import division
import re
from random import randrange
from urllib import urlopen
from bs4 import BeautifulSoup
from twitter import *
import nltk
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




#import all the feature vectors


object1=open('k_words','r')
k_words=cPickle.load(object1)

object1.close()


fileObject=open('k_stems','r')
k_stems=cPickle.load(fileObject)

fileObject.close()

fileObject=open("k_hash",'r')
k_hash=cPickle.load(fileObject)

fileObject.close()

fileObject=open("k_bigram",'r')
k_bigram=cPickle.load(fileObject)

fileObject.close()

fileObject=open("k_trigram",'r')
k_trigram=cPickle.load(fileObject)

fileObject.close()

fileObject=open("k_ending",'r')
k_ending=cPickle.load(fileObject)

fileObject.close()


fileObject=open("Dev_List",'r')
Dev_List=cPickle.load(fileObject)

fileObject.close()

fileObject=open("Test_List",'r')
Test_List=cPickle.load(fileObject)

fileObject.close()





#conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='smalls7_groupid', passwd='LetsPublish!', db='smalls7_identity')
#cur = conn.cursor()


#cur.execute("SELECT DISTINCT(survey.Id) FROM survey;")



#all_user_id=cur.fetchall()


regex1=re.compile(r'(https?://\S+)') #This pulls the whole url.

regex2=re.compile("(?P<url>https?://[^\s/]+)")# This specifically pulls stems of URLs

UserFeatures={}

AllUserTweets=[]


#Simple function that calculates a users scores- takes in their tokenized and processed tweets and returns the score for a given feature.


def ScoreGenerate(UserSet,K_most_vector):
    fullset=[word for word in UserSet if word in K_most_vector[0]+K_most_vector[1]]
    setfreq=FreqDist(fullset)
    v1=[setfreq.freq(word) for word in K_most_vector[0]]
    v2=[setfreq.freq(word) for word in K_most_vector[1]]
    finalscore=[v1,v2]

    return finalscore


TweetsByUsers=[] # This will eventually give us all the tweets in semi-tokenized form, for each user


count =-1


UserLabels=[]


UserScores=[]



for party in Dev_List:
    count += 1
    for user in party:
        raw_URLforUser=[regex1.findall(word) for word in user]
    #The findall function puts the output in brackets, so the next function is to take the brackets out- so it's no longer a nested list. 
        UserUrl=[word for words in raw_URLforUser for word in words]
        raw_HashforUser=[word for word in user if word.startswith('#')]
        raw_MentionforUser=[word for word in user if word.startswith('@')]


        hash_final=[word.lower() for word in raw_HashforUser]

        unigram1=[re.sub('[^a-zA-Z ]','',word).lower() for word in user if word not in UserUrl + raw_HashforUser+ raw_MentionforUser]

        bigrams_for_user=bigrams(unigram1)
        trigrams_for_user=trigrams(unigram1)

        stems_for_user=[stem(word) for word in unigram1]

        

        endings_for_user=[re.sub(stem(word),'',word) for word in unigram1]


       
        unigram=ScoreGenerate(unigram1,k_words)
        bigram=ScoreGenerate(bigrams_for_user,k_bigram)
        trigram=ScoreGenerate(trigrams_for_user,k_trigram)
        hashtag=ScoreGenerate(hash_final,k_hash)
        stem=ScoreGenerate(stems_for_user,k_stems)
        ending=ScoreGenerate(endings_for_user,k_ending)

        UserScores+=[[sum(unigram[0]),sum(unigram[1]),sum(bigram[0]),sum(bigram[1]), sum(trigram[0]), sum(hashtag[0]),sum(hashtag[1]),sum(stem[0]),sum(stem[1]), sum(ending[0]), sum(ending[1]), numpy.var(unigram[0]),numpy.var(unigram[1]),numpy.var(bigram[0]),numpy.var(bigram[1]), numpy.var(trigram[0]), numpy.var(hashtag[0]),numpy.var(hashtag[1]),numpy.var(stem[0]),numpy.var(stem[1]), numpy.var(ending[0]),numpy.var(ending[1])]]

        UserLabels.append(count)






TestScores=[]
TestLabels=[]

count=-1



for party in Test_List:
    count += 1
    for user in party:
        raw_URLforUser=[regex1.findall(word) for word in user]
    #The findall function puts the output in brackets, so the next function is to take the brackets out- so it's no longer a nested list. 
        UserUrl=[word for words in raw_URLforUser for word in words]
        raw_HashforUser=[word for word in user if word.startswith('#')]
        raw_MentionforUser=[word for word in user if word.startswith('@')]


        hash_final=[word.lower() for word in raw_HashforUser]

        unigram1=[re.sub('[^a-zA-Z ]','',word).lower() for word in user if word not in UserUrl + raw_HashforUser+ raw_MentionforUser]

        bigrams_for_user=bigrams(unigram1)
        trigrams_for_user=trigrams(unigram1)

        stems_for_user=[stem(word) for word in unigram1]

        

        endings_for_user=[re.sub(stem(word),'',word) for word in unigram1]


       
        unigram=ScoreGenerate(unigram1,k_words)
        bigram=ScoreGenerate(bigrams_for_user,k_bigram)
        trigram=ScoreGenerate(trigrams_for_user,k_trigram)
        hashtag=ScoreGenerate(hash_final,k_hash)
        stem=ScoreGenerate(stems_for_user,k_stems)
        ending=ScoreGenerate(endings_for_user,k_ending)

        TestScores+=[[sum(unigram[0]),sum(unigram[1]),sum(bigram[0]),sum(bigram[1]), sum(trigram[0]), sum(hashtag[0]),sum(hashtag[1]),sum(stem[0]),sum(stem[1]), sum(ending[0]), sum(ending[1]), numpy.var(unigram[0]),numpy.var(unigram[1]),numpy.var(bigram[0]),numpy.var(bigram[1]), numpy.var(trigram[0]), numpy.var(hashtag[0]),numpy.var(hashtag[1]),numpy.var(stem[0]),numpy.var(stem[1]), numpy.var(ending[0]),numpy.var(ending[1])]]

        TestLabels.append(count)




        


        #UserFeatures[username]={}
        #UserFeatures[username]['unigram']=ScoreGenerate(unigram1,k_words)
        #UserFeatures[username]['bigram']=ScoreGenerate(bigrams_for_user,k_bigram)
        #UserFeatures[username]['trigram']=ScoreGenerate(trigrams_for_user,k_trigram)
        #UserFeatures[username]['hash']=ScoreGenerate(hash_final,k_hash)
        #UserFeatures[username]['stem']=ScoreGenerate(stems_for_user,k_stems)
        #UserFeatures[username]['ending']=ScoreGenerate(endings_for_user,k_ending)

























    











    #unigram_for_scoring=[word  for word in unigram1 if word in k_words[0] + k_words[1]]

    #unigramFreq=FreqDist(unigram_for_scoring)

    #G1_score=[]

    #Make this into a function later- because it's the same dynamics for all the features- or perhaps I could use a list comprehension

    #for words in k_words[0]:
        #v=unigramFreq.freq(word)
        #G1_score.append(v)


    #G1_score_alt=[unigramFreq.freq(word) for word in k_words[0]]

    #UnigramDict[username]=G1_score

    #UnigramaltDict[username]=G1_score_alt



    # 

























    #G1URL_temp=[regex1.findall(word) for word in wordlists[0]] # takes out all the full URLs, but puts them as a set of lists

#G1FullURL=[word for words in G1URL_temp for word in words]

    
   






#raw=TweetforUser.split()
#raw_for_unigram=[re.sub('[^a-zA-Z ]','',word).lower() for word in raw]
#raw_for_unigram=[word for word in k_words[0]+k_words[1]]
    
#raw_uni_freq=FreqDist(raw_for_unigram)

        
    
    
 
        
        