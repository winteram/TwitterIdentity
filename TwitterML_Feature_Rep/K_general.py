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


#Minimum Frequency Thresholds


UNIGRAM_THRESHOLD= 6
BIGRAM_THRESHOLD = 6
TRIGRAM_THRESHOLD= 6
STEM_THRESHOLD= 6
ENDING_THRESHOLD=6
HASH_THRESHOLD= 6
FOLLOWER_THRESHOLD=3


#Minimum Number of Users Thresholds

UNIGRAM_THRESHOLD_USER= 3
BIGRAM_THRESHOLD_USER= 3
TRIGRAM_THRESHOLD_USER= 3
STEM_THRESHOLD_USER= 3
ENDING_THRESHOLD_USER= 3
HASH_THRESHOLD_USER= 3
FOLLOWER_THRESHOLD_USER=3





# import copy



#start by unpickling DemWord Lists and RepList


 




#Function I pulled off stack overflow that unshortens twitter URLS:


def unshorten_url(url):
    parsed = urlparse.urlparse(url)
    h = httplib.HTTPConnection(parsed.netloc)
    h.request('HEAD', parsed.path)
    response = h.getresponse()
    if response.status/100 == 3 and response.getheader('Location'):
        return response.getheader('Location')
    else:
        return url






#unpickle stuff Here
#at the end, we probably want to store the scores to the database. #note this program will not treat a series of hashtags lumped togehter #term1#term2#t3 as separte entities. might modify this in a bit to account for that.   




#object1=open('WordLists','r')
#wordlists=cPickle.load(object1)

object2=open('Seed_List','r')
Seed_List=cPickle.load(object2)


object3=open('IdList','r')
IdList=cPickle.load(object3)


object4=open('Seed_Follow', 'r')
Seed_Follow=cPickle.load(object4)

#Note: wordlists[0]=Democrat Corpus(we make it G1), wordlist[1]=Republican corpus(G2)


regex1=re.compile(r'(https?://\S+)') #This pulls the whole url.

regex2=re.compile("(?P<url>https?://[^\s/]+)")# This specifically pulls stems of URLs





G1URL_temp_users=[[regex1.findall(word) for word in users] for users in Seed_List[0]]
G1FullURL_users=[[word for user in users for word in user] for users in G1URL_temp_users]



G2URL_temp_users=[[regex1.findall(word) for word in users] for users in Seed_List[1]]
G2FullURL_users=[[word for user in users for word in user] for users in G1URL_temp_users]




#do the same for hash tags. Then create one for loop excluding words- user by user, to be efficient [user set of words[i]]
#not in hash[i]+URL[i]

#Eventual function just needs 4 parameters- minimum frequency, minimum 


#G1URL_temp=[regex1.findall(word) for word in wordlists[0]] # takes out all the full URLs, but puts them as a set of lists

#G1FullURL=[word for words in G1URL_temp for word in words] # makes the set of lists with strings within them a simple list of strings.

#unshorten the URLs



#G1FullURL_final=[[unshorten_url(url) for url in users] for users in G1FullURL_users]

#take the stems of these unshortened URLs 

#G1URL_stemtemp=[regex2.findall(word) for word in G1FullURL_final]

#take the stems out of lists and make them simply a series of strings in one list

#G1URL_stem_final=[word for words in G1URL_stemtemp for word in words] #This is the final one we care about


#Doing the same for group 2


#G2URL_temp=[regex1.findall(word) for word in wordlists[1]]

#G2FullURL=[word for words in G2URL_temp for word in words]



#unshorten URLs

#G2FullURL_final=[unshorten_url(url) for url in G2FullURL]

#take the stem of these unshortened URLs

#G2URL_stemtemp=[regex2.findall(word) for word in G2FullURL_final]

#G2URL_stem_final=[word for words in G2URL_stemtemp for word in words] #This is the final one we care about



#Now, we want to separate the hashtags terms

#G1URL_temp_users1=[[regex1.findall(word) for word in users] for users in Seed_List[0]]

#G1FullURL_users=[[word for user in users for word in user] for users in G1URL_temp_users1]


G1Hash_users=[[word for word in users if word.startswith('#')] for users in Seed_List[0]] #This will pull hashtag terms for Democrats


G2Hash_users=[[word for word in users if word.startswith('#')] for users in Seed_List[1]] 

#Above sets are used for exclusion purposes in a later piece of code. The code below is a bit redundant but makes everytihng lowercase.


G1HashFinalUser= [[re.sub('[^a-zA-Z# ]','',word).lower() for word in users if word.startswith('#')] for users in Seed_List[0]]
G2HashFinalUser= [[re.sub('[^a-zA-Z# ]','',word).lower() for word in users if word.startswith('#')] for users in Seed_List[1]]






#G1Hash=[word for word in wordlists[0] if word.startswith('#')] #This will pull hashtag terms for Democrats

#G2Hash=[word for word in wordlists[1] if word.startswith('#')]

G1Mentions =[[word for word in users if word.startswith('@') or word.startswith('http')] for users in Seed_List[0]]

G2Mentions =[[word for word in users if word.startswith('@') or word.startswith('http')] for users in Seed_List[1]]




# Now we want to exclude all hash tag terms and urls from our set of unigrams

#G1Words=[word for word in wordlists[0] if word not in G1Hash + G1FullURL and len(word)>2] #This gives us all nonhashtag and non-urls 3 or more characters long

#G2Words=[word for word in wordlists[1] if word not in G2Hash + G2FullURL and len(word)>2]


#Now I want to get the unigrams with hashtags and urls removed

Unigrams_Group1_by_User=[]

words_for_ngrams1=[] #This will be the same as the unigram list EXCEPT it will include words of 2 or less characters for construction of bigrams and trigrams


for i, user in enumerate(Seed_List[0]):
    k=[re.sub('[^a-zA-Z ]','',word).lower() for word in user if word not in G1Hash_users[i] + G1FullURL_users[i] + G1Mentions[i] and len(word) > 2]
    w=[re.sub('[^a-zA-Z ]','',word).lower() for word in user if word not in G1Hash_users[i] + G1FullURL_users[i] + G1Mentions[i]]
    Unigrams_Group1_by_User.append(k)
    words_for_ngrams1.append(w)



Unigrams_Group2_by_User=[]

words_for_ngrams2=[] 

for i, user in enumerate(Seed_List[1]):
    k=[re.sub('[^a-zA-Z ]','',word).lower() for word in user if word not in G2Hash_users[i] + G2FullURL_users[i] + G2Mentions[i] and len(word) > 2]
    w=[re.sub('[^a-zA-Z ]','',word).lower() for word in user if word not in G2Hash_users[i] + G2FullURL_users[i] + G2Mentions[i]] 
    Unigrams_Group2_by_User.append(k)
    words_for_ngrams2.append(w) 


#Use NLTK collocation functions to generate meaningful bigrams and trigrams. This is a bit tricky because the function returns n-best and we have to 
#somewhat arbitrarily decide what n should be. 




bigram_measures = nltk.collocations.BigramAssocMeasures()

full_for_ngrams1=[word for user in words_for_ngrams1 for word in user]

finder = BigramCollocationFinder.from_words(full_for_ngrams1)

finder.apply_freq_filter(2)

bigrams1=finder.nbest(bigram_measures.pmi, 1200)



full_for_ngrams2=[word for user in words_for_ngrams2 for word in user]

finder = BigramCollocationFinder.from_words(full_for_ngrams2)

finder.apply_freq_filter(2)

bigrams2=finder.nbest(bigram_measures.pmi, 1200)


trigram_measures = nltk.collocations.TrigramAssocMeasures()

finder = TrigramCollocationFinder.from_words(full_for_ngrams1)

finder.apply_freq_filter(2)

trigrams1=finder.nbest(trigram_measures.pmi, 1200)



finder = TrigramCollocationFinder.from_words(full_for_ngrams2)

finder.apply_freq_filter(2)

trigrams2=finder.nbest(trigram_measures.pmi, 1200)




#

#G1Trigram_by_User= [trigrams(users) for users in words_for_ngrams1 if word in trigrams(users) in trigrams1]




G1Bigram_by_User= [[word for word in bigrams(users) if word in bigrams1] for users in words_for_ngrams1]

G2Bigram_by_User= [[word for word in bigrams(users) if word in bigrams2] for users in words_for_ngrams2]




G1Trigram_by_User= [[word for word in trigrams(users) if word in trigrams1] for users in words_for_ngrams1]

G2Trigram_by_User= [[word for word in trigrams(users) if word in trigrams2] for users in words_for_ngrams2]




G1Stems_by_User= [[stem(word) for word in users] for users in Unigrams_Group1_by_User]

G2Stems_by_User= [[stem(word) for word in users] for users in Unigrams_Group2_by_User]


#Suffixes- note that since special characters were simply deleted and replaced with an empty string- some these things are actually full words


G1ending_by_User= [[re.sub(stem(word),'',word) for word in users if re.sub(stem(word),'',word) !=''] for users in Unigrams_Group1_by_User]

G2ending_by_User= [[re.sub(stem(word),'',word) for word in users if re.sub(stem(word),'',word) !=''] for users in Unigrams_Group2_by_User]






#These are bigrams and trigrams not generated from collocations. We can see if these work for our purposes later, but it seems like a long shot. 

#G1Bigram_by_User= [bigrams(users) for users in Unigrams_Group1_by_User]

#G2Bigram_by_User= [bigrams(users) for users in Unigrams_Group2_by_User]


#G1Trigram_by_User= [trigrams(users) for users in Unigrams_Group1_by_User]

#G2Trigram_by_User= [trigrams(users) for users in Unigrams_Group2_by_User]

















#clean these up.

#G1Words=[re.sub('[^a-zA-Z ]','',word).lower() for word in G1Words]
#G1Words=[re.sub('[^a-zA-Z ]','',word).lower() for word in G1Words]






#Now we want a list of stems

#G1stem=[stem(word) for word in G1Words]
#G2stem=[stem(word) for word in G2Words]

#Create a list of bigrams and trigrams

#bigram_measures = BigramAssocMeasures()
#trigram_measures = TrigramAssocMeasures()

#G1_bigrams = BigramCollocationFinder._ngram_freqdist(G1Words,3)
#G2_bigrams = BigramCollocationFinder._ngram_freqdist(G1Words,3)

#G1_bigrams=bigrams(G1Words)
#G2_bigrams=bigrams(G2Words)

#G1_trigrams=trigrams(G1Words)
#G2_trigrams=trigrams(G2Words)



def generate_K_most(G1Corp, G2Corp, n, j): # G1Corp= The words, hashtags, urls or whatever raw set we have extracted associated with a class (G1), G2 is the other class, n= #minimum frequency a potential feature must appear within the corpus.
    
    # j is the minimum number of users to use the term. 

    G1=[word for user in G1Corp for word in user]
    G2=[word for user in G2Corp for word in user]
    


    G1Freq=FreqDist(G1) 
    
    G2Freq=FreqDist(G2)


    GP1words=[word for word in G1 if G1Freq[word]>n]

    GP2words=[word for word in G2 if G2Freq[word]>n]
    
  
    
    GP1_FinalFreq=FreqDist(GP1words)
    GP2_FinalFreq=FreqDist(GP2words)

    FullWords=G1+G2


    FullFreq=FreqDist(FullWords)

    G1Dic={}

    G2Dic={}


#Now create a list with proportions for each word in the Democratic corpus. 

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

#This part filters out words that appear among less than j users- In the Seed_List- It would probably be smarter to split it up before importing- this way it's not contingent on knowing how many
#users are present. Maybe make 

    
        
    for word in sorted_G1:
            count=0
            if len(K_final1)==200 or word[1] <.65:
            
                break
            for users in G1Corp:
                if word[0] in users:
                    count=count+1
                    if count == j:
                        K_final1.append(word[0])
                        break
        
    for word in sorted_G2:
            count=0
            if len(K_final2)==200 or word[1] <.65:
            
                break
            for users in G2Corp:
                if word[0] in users:
                    count=count+1
                    if count == j:
                        K_final2.append(word[0])
                        break
    
    
    K_final=[K_final1,K_final2]




   


    return K_final



k_most_words=generate_K_most(Unigrams_Group1_by_User,Unigrams_Group2_by_User,UNIGRAM_THRESHOLD,UNIGRAM_THRESHOLD_USER)

k_most_stems=generate_K_most(G1Stems_by_User,G2Stems_by_User,STEM_THRESHOLD,STEM_THRESHOLD_USER)

k_most_hash=generate_K_most(G1HashFinalUser,G2HashFinalUser,HASH_THRESHOLD,HASH_THRESHOLD_USER)

k_most_bigrams=generate_K_most(G1Bigram_by_User,G2Bigram_by_User,BIGRAM_THRESHOLD,BIGRAM_THRESHOLD_USER)

k_most_trigrams=generate_K_most(G1Trigram_by_User,G2Trigram_by_User,TRIGRAM_THRESHOLD,TRIGRAM_THRESHOLD_USER)

k_most_ending=generate_K_most(G1ending_by_User,G2ending_by_User,ENDING_THRESHOLD,ENDING_THRESHOLD_USER)

k_most_follow=generate_K_most(Seed_Follow[0],Seed_Follow[1], FOLLOWER_THRESHOLD,FOLLOWER_THRESHOLD_USER )


#put in endings by user




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

fileObject=open("k_ending",'w+')
cPickle.dump(k_most_ending,fileObject)

fileObject.close()

fileObject=open("k_follow",'w+')
cPickle.dump(k_most_follow,fileObject)

fileObject.close()

























    
    








    

    




























