


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

def unshorten_url(url):
    parsed = urlparse.urlparse(url)
    h = httplib.HTTPConnection(parsed.netloc)
    h.request('HEAD', parsed.path)
    response = h.getresponse()
    if response.status/100 == 3 and response.getheader('Location'):
        return response.getheader('Location')
    else:
        return url










#Function I pulled off stack overflow that unshortens twitter URLS:


#unpickle stuff Here
#at the end, we probably want to store the scores to the database. #note this program will not treat a series of hashtags lumped togehter #term1#term2#t3 as separte entities. might modify this in a bit to account for that.   

object1=open('WordLists','r')
wordlists=cPickle.load(object1)

#Note: wordlists[0]=Democrat Corpus(we make it G1), wordlist[1]=Republican corpus(G2)


regex1=re.compile(r'(https?://\S+)') #This pulls the whole url.

regex2=re.compile("(?P<url>https?://[^\s/]+)")# This specifically pulls stems


G1URL_temp=[regex1.findall(word) for word in wordlists[0]] # takes out all the full URLs, but puts them as a set of lists

G1FullURL=[word for words in G1URL_temp for word in words] # makes the set of lists with strings within them a simple list of strings.

#unshorten the URLs

G1Part1=G1FullURL[1:10]


G1Part_shorten=[unshorten_url(url) for url in G1Part1]

#take the stems of these unshortened URLs 

#G1URL_stemtemp=[regex2.findall(word) for word in G1Part_shorten]






    
    








    

    




























