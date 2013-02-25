


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
    
    username=user[0]
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
    cur.execute("SELECT DISTINCT(survey.Id) FROM survey WHERE party = 'democrat';")
    tweets=cur.fetchall()

    DemTweetSet.append(tweets)


#Should do some cleaning here before pickling- Basically all I need are two- raw- lists. One with all the tweets for each user, encapsulated by user, the other just one long list for of words for all the users- I can use the split function, as I had previously. Importantly- before doing bigrams and trigrams- after stuff has has been
#lower-cased, remove everything but alpha numeric stuff (this is after hashtags and urls have been pulled out. I say this because when I was playing with the trigram- there were periods and stuff. We don't want that- actually I could probably just run word tokenize or something on the list- does it work for a list, lets check. 


tweetText = ""
        
        
        
All_Tweets=""

= ""

UserWordList=[]


    
    
    
Party_list=DemTweetSet+RepTweetSet
    
    
    
    
    
for party in Party_list:


    for users in party
        
        Tweets_by_user=""
        
        
        
        for tweet in users:
            # clean tweet text & tokenize
            tweetText = tweet[0] #.encode('utf8')
            
            
            Tweets_by_user=Tweets_by_user + " " + tweetText
        


    All_Tweets=All_Tweets + " " + tweetText

    UserWordList.append(tweetText) # This separates the tweets for each user in list form- we can later use these to filter things
    






    
    

#Now it pickles

fileObject=open("RepList",'w+')

cPickle.dump(RepTweetSet,fileObject)

fileObject.close()

fileObject=open("DemList",'w+')

cPickle.dump(DemTweetSet,fileObject)

fileObject.close()
    
    #Tweets can be processed to some degree
    
    #to get it in the right format:

    
    
    
    #Will pull this directly from the database eventually. Right now, I will just use what we have pickled.
    
    # So this part assumes things have been pickled- need to put code unpickle DemList, unpickle RepList- also, I have the option of doing something like...
    # Make a vector that is DemList+RepList= PolList
    #for party in PolList:
    #   for user in party....
    
    
   
            
            
            
            
            
            
            #Note: with the UTF8 encoding a lot of this reg-expression cleanup is not necessary.
            
            tweetText = re.sub('[^.a-zA-Z1-9 #/:-]', '', tweetText)
            tweetText = re.sub('(?P<endword>[a-z]+)(?P<begword>[A-Z])', '\g<endword> \g<begword>', tweetText)
            tweetText = tweetText.lower()
            #Note I think we should preserve case sensitivity because things like "FED" vs "fed", "US" vs "us". However, this might get captured better when we use n-grams
            
            tweet_wordlist = word_tokenize(tweetText)


#This might be useful for something-I should use it:

for i,word in enumerate(TotalDist.keys()):
    
    b[i] = WeFreq[word]
    c[i] = r_AllFreq(word)  # Now this is relative frequency



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

G1Hash=[word for word in wordlists[0] if word.startswith('#')] #This will pull hashtag terms for Democrats

G2Hash=[word for word in wordlists[1] if word.startswith('#')]


# Now we want to exclude all hash tag terms and urls from our set of unigrams

G1Words=[word for word in wordlists[0] if word not in G1Hash + G1FullURL and len(word)>2] #This gives us all nonhashtag and non-urls 3 or more characters long

G2Words=[word for word in wordlists[1] if word not in G2Hash + G2FullURL and len(word)>2]


#Now we want a list of stems

G1stem=[stem(word) for word in G1Words]
G2stem=[stem(word) for word in G2Words]

#Create a list of bigrams and trigrams

bigram_measures = BigramAssocMeasures()
trigram_measures = TrigramAssocMeasures()

G1_trigrams = BigramCollocationFinder._ngram_freqdist(G1Words, 3)



def generate_K_most(G1Corp, G2Corp, n): # G1Corp= The words, hashtags, urls or whatever raw set we have extracted associated with a class (G1), G2 is the other class, n= #minimum frequency a potential feature must appear within the corpus

    G1Freq=FreqDist(G1Corp) 
    
    G2Freq=FreqDist(G2Corp)


    GP1words=[word for word in G1Corp if G1Freq[word]>n]

    GP2words=[word for word in G2Corp if G2Freq[word]>n]
    
    GP1_FinalFreq=FreqDist(GP1words)
    GP2_FinalFreq=FreqDist(GP2words)

    FullWords=GP1words+GP2words


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

    G1_set=[x[0] for x in sorted_G1[0:200]]
    G2_set=[x[0] for x in sorted_G2[0:200]]

#K_vector= G1_set+G2_set
    K_vector=sorted_G1[0:200]+sorted_G2[0:200]

    return K_vector


k_most_words=generate_K_most(G1Words,G2Words,5)

k_most_stems=generate_K_most(G1stem,G2stem,5)

k_most_hash=generate_K_most(G1Hash,G2Hash,5)






    
    








    

    




























