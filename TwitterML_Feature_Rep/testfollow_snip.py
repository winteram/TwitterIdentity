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
import pickle
import pymysql
import operator
from stemming.porter2 import stem
import copy






fileObject=open("Test_List",'r')
Test_List=pickle.load(fileObject)


fileObject.close()



fileObject=open("Dev_List",'r')
Dev_List=cPickle.load(fileObject)


fileObject.close()

fileObject=open("k_follow",'r')
k_follow=pickle.load(fileObject)


fileObject.close()

fileObject=open("Dev_Follow",'r')
Dev_Follow=pickle.load(fileObject)


fileObject.close()

fileObject=open("Test_Follow",'r')
Dev_Follow=pickle.load(fileObject)

fileObject.close()

FollowScores=[]


def ScoreGenerate(UserSet,K_most_vector):
    fullset=[word for word in UserSet if word in K_most_vector[0]+K_most_vector[1]]
    setfreq=FreqDist(fullset)
    v1=[setfreq.freq(word) for word in K_most_vector[0]]
    v2=[setfreq.freq(word) for word in K_most_vector[1]]
    finalscore=[v1,v2]
    return finalscore


count =-1

for i,party in enumerate(Dev_List):
    count += 1
    for j,user in enumerate(party):
    	print i,j



        #follows=ScoreGenerate(Dev_Follow[i][j],k_follow)



        #FollowScores+=[follows[0],follows[1]]

