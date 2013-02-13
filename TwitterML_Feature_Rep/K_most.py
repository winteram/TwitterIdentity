

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
import cPickle

import pymysql

import operator




#unpickle stuff Here
#at the end, we probably want to store the scores to the database.

object1=open('WordLists','r')
wordlists=cPickle.load(object1)

#Note: wordlists[0]=Democrat Corpus, wordlist[1]=Repbulican corpus. 


#Now, we want to separate the hashtags terms and regular words (later we can pull out URLs. For urls, it will probably be better to also include dots and slashes, so we can pull out stems. Right now the program excludes these)

DemHash=[word for word in wordlists[0] if word.startswith('#')] #This will pull hashtag terms for Democrats

DemWords=[word for word in wordlists[0] if word not in DemHash and len(word)>2] #This gives us all non-hashtag words

RepHash=[word for word in wordlists[1] if word.startswith('#')]

RepWords=[word for word in wordlists[1] if word not in RepHash and len(word)>2]


DemFreq=FreqDist(DemWords)#gives us an initial frequency

RepFreq=FreqDist(RepWords)


n=6 # experiment with this parameter a bit- minimum frequency

Dwords=[word for word in DemWords if DemFreq[word]>n]

Rwords=[word for word in RepWords if DemFreq[word]>n]

FullWords=Dwords+Rwords



FullFreq=FreqDist(FullWords)

DFreq=FreqDist(Dwords)

RFreq=FreqDist(Rwords)

DemDic={}

RepDic={}



#Now create a list with proportions for each word in the democratic corpus 

for i in DFreq.keys():
    rat= (DFreq[i]/FullFreq[i])
    DemDic[i]=rat

sorted_Dem = sorted(DemDic.iteritems(), key=operator.itemgetter(1),reverse=True)

for word in RFreq.keys():
    x= (RFreq[word]/FullFreq[word])
    RepDic[word]=x

sorted_Rep= sorted(RepDic.iteritems(), key=operator.itemgetter(1),reverse=True)









    

    




























