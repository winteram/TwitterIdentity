


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
import copy



#start by unpickling DemWord Lists and RepList


 




#Function I pulled off stack overflow that unshortens twitter URLS:


def unshorten_url(url):
    parsed = urlparse.urlparse(url)
    h = httplib.HTTPConnection(parsed.netloc)
    resource = parsed.path
    if parsed.query != "":
        resource += "?" + parsed.query
    h.request('HEAD', resource )
    response = h.getresponse()
    if response.status/100 == 3 and response.getheader('Location'):
        return unshorten_url(response.getheader('Location')) # changed to process chains of short urls
    else:
        return url


#unpickle stuff Here
#at the end, we probably want to store the scores to the database. #note this program will not treat a series of hashtags lumped togehter #term1#term2#t3 as separte entities. might modify this in a bit to account for that.   

object1=open('WordLists','r')
wordlists=cPickle.load(object1)

object2=open('WordsByUser','r')
WordsByUser=cPickle.load(object2)

#Note: wordlists[0]=Democrat Corpus(we make it G1), wordlist[1]=Republican corpus(G2)


regex1=re.compile(r'(https?://\S+)') #This pulls the whole url.

regex2=re.compile("(?P<url>https?://[^\s/]+)")# This specifically pulls stems


G1URL_temp=[regex1.findall(word) for word in wordlists[0]] # takes out all the full URLs, but puts them as a set of lists

G1FullURL=[word for words in G1URL_temp for word in words] # makes the set of lists with strings within them a simple list of strings.

#unshorten the URLs

#G1FullURL_final=[unshorten_url(url) for url in G1FullURL]

#take the stems of these unshortened URLs 

#G1URL_stemtemp=[regex2.findall(word) for word in G1FullURL_final]

#take the stems out of lists and make them simply a series of strings in one list

#G1URL_stem_final=[word for words in G1URL_stemtemp for word in words] #This is the final one we care about


#Doing the same for group 2


G2URL_temp=[regex1.findall(word) for word in wordlists[1]]

G2FullURL=[word for words in G2URL_temp for word in words]



#unshorten URLs

#G2FullURL_final=[unshorten_url(url) for url in G2FullURL]

#take the stem of these unshortened URLs

#G2URL_stemtemp=[regex2.findall(word) for word in G2FullURL_final]

#G2URL_stem_final=[word for words in G2URL_stemtemp for word in words] #This is the final one we care about



#Now, we want to separate the hashtags terms

G1Hash=[word.lower() for word in wordlists[0] if word.startswith('#')] #This will pull hashtag terms for Democrats

G2Hash=[word.lower() for word in wordlists[1] if word.startswith('#')]


# Now we want to exclude all hash tag terms and urls from our set of unigrams

G1Words=[word for word in wordlists[0] if word not in G1Hash + G1FullURL and len(word)>2] #This gives us all nonhashtag and non-urls 3 or more characters long

G2Words=[word for word in wordlists[1] if word not in G2Hash + G2FullURL and len(word)>2]







#clean these up.

G1Words=[re.sub('[^a-zA-Z ]','',word).lower() for word in G1Words]
G1Words=[re.sub('[^a-zA-Z ]','',word).lower() for word in G1Words]






#Now we want a list of stems

G1stem=[stem(word) for word in G1Words]
G2stem=[stem(word) for word in G2Words]

#Create a list of bigrams and trigrams

#bigram_measures = BigramAssocMeasures()
#trigram_measures = TrigramAssocMeasures()

#G1_bigrams = BigramCollocationFinder._ngram_freqdist(G1Words,3)
#G2_bigrams = BigramCollocationFinder._ngram_freqdist(G1Words,3)

G1_bigrams=bigrams(G1Words)
G2_bigrams=bigrams(G2Words)

G1_trigrams=trigrams(G1Words)
G2_trigrams=trigrams(G2Words)



def generate_K_most(G1Corp, G2Corp, n): # G1Corp= The words, hashtags, urls or whatever raw set we have extracted associated with a class (G1), G2 is the other class, n= #minimum frequency a potential feature must appear within the corpus.
    
    #This will eventually need six parameters- 3 more for the WordsByUser versions

    G1Freq=FreqDist(G1Corp) 
    
    G2Freq=FreqDist(G2Corp)


    GP1words=[word for word in G1Corp if G1Freq[word]>n]

    GP2words=[word for word in G2Corp if G2Freq[word]>n]
    
  
    
    GP1_FinalFreq=FreqDist(GP1words)
    GP2_FinalFreq=FreqDist(GP2words)

    FullWords=G1Corp+G2Corp


    FullFreq=FreqDist(FullWords)

    G1Dic={}

    G2Dic={}


#Now create a list with proportions for each word in the Democratic corpus 

    for i in GP1_FinalFreq.keys():
        rat= (GP1_FinalFreq[i]/FullFreq[i])
        G1Dic[i]=rat

    sorted_G1 = sorted(G1Dic.iteritems(), key=operator.itemgetter(1),reverse=True)# This sorts the dictionary items into tuples in descending order by ratio value. 

    for word in GP2_FinalFreq.keys():
        x= (GP2_FinalFreq[word]/FullFreq[word])
        G2Dic[word]=x

    sorted_G2= sorted(G2Dic.iteritems(), key=operator.itemgetter(1),reverse=True)

    G1_set=[x[0] for x in sorted_G1]
    G2_set=[x[0] for x in sorted_G2]

#K_vector= G1_set+G2_set
    K_vector=sorted_G1[0:200]+sorted_G2[0:200]

    
    
    K_final1=[]
    K_final2=[]

#This part filters out words that appear among less than j users- In the WordsByUser- It would probably be smarter to split it up before importing- this way it's not contingent on knowing how many
#users are present. Maybe make 

   


    return K_vector


k_most_words=generate_K_most(G1Words,G2Words,5)

k_most_stems=generate_K_most(G1stem,G2stem,5)

k_most_hash=generate_K_most(G1Hash,G2Hash,5)

k_most_bigrams=generate_K_most(G1_bigrams,G2_bigrams,3)

k_most_trigrams=generate_K_most(G1_trigrams,G2_trigrams,3)




#generate user scores

fileObject=open("k_words",'w+')
cPickle.dump(k_most_words,fileObject)

fileObject.close()


fileObject=open("k_stems",'w+')
cPickle.dump(k_most_stems,fileObject)

fileObject.close()

fileObject=open("k_hash",'w+')
cPickle.dump(k_most_hash,fileObject)

fileObject.close()

fileObject=open("k_bigram",'w+')
cPickle.dump(k_most_bigrams,fileObject)

fileObject.close()

fileObject=open("k_trigram",'w+')
cPickle.dump(k_most_trigrams,fileObject)

fileObject.close()






















    
    








    

    




























