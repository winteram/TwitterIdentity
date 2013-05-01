



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
import random
import pickle
import cPickle

wewords = ["we","us","our","ours","ourselves"]
bigram_measures = BigramAssocMeasures()
trigram_measures = TrigramAssocMeasures()

oauth_token = "563118238-aVS68vGHeiWuoLCHIOudAPa6hmhnwIBsSkUfeBXt"
oauth_secret = "M6h51pETL8CWkowEeyh6cb7gNpNTyBpl7fLJk45J4Y"
CONSUMER_KEY = "PCMmY6ERIWJM9tgjIiQRwA"
CONSUMER_SECRET = "YWeRQPivyjc9ZUSLQbaFj8enJviPZ8cw55mu3qSuJdk"

t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))


# parse corpus
def parseCorpus(corpusdir):    
    # Load the corpus into nltk and store files as separate file ID, which can be accessed by name.
    # to see which files are in the corpus use the command: corpus.fileids()
    corpus = PlaintextCorpusReader(corpusdir, '.*')
    corpusText = corpus.raw()
    #corpusText = re.sub('[^a-zA-Z ]', '', corpusText)
    corpusText = re.sub('(?P<endword>[a-z]+)(?P<begword>[A-Z])', '\g<endword> \g<begword>', corpusText)
    corpusText = corpusText.lower()
    # Create Frequency Distributions for bigrams
    # Dem_bigrams = BigramCollocationFinder._ngram_freqdist(Dem_wordlist, 2)

    # Create Frequency Distributions for trigrams
    # Dem_trigrams = BigramCollocationFinder._ngram_freqdist(Dem_wordlist, 3)

#    return word_tokenize(corpusText)
    return [w for w in word_tokenize(corpusText) if w not in stopwords.words('english')]



# parse tweets of party leaders
def parseTweets(nameList):
    # verify the input is a list
    assert type(nameList) == type(list())
    tweetText = ""
    x = ""

    Userlist=[]
    # get tweets for each twitter account in list
    for name in nameList:        
        tweets1= t.statuses.user_timeline(id = name, count = 200)
        tweets2= t.statuses.user_timeline(id = name, count = 200, max_id = tweets1[len(tweets1)-1]['id'])
        tweets3= t.statuses.user_timeline(id = name, count = 200, max_id = tweets2[len(tweets2)-1]['id'])
        tweets= tweets1 + tweets2 + tweets3
    
        # combine
        
        for i in range(len(tweets)):
            x = x + " " + tweets[i]['text'].encode('utf8')
        
        ## TODO: pull out URLs first and parse their text?
        # takes everything but alpha characters and hashtags from the string
        #clean_two = re.sub('[^a-zA-Z #]', '', x)

        ## TODO:  This is actually the encoding of the string
        # this leaves u's at the beginning of things, so we need pull these out. 
        clean_two = re.sub('u(?P<beg>[A-Z])', '\g<beg>', x)

        ## TODO: Probably these are line endings?  
        # there are still also n's, those should be removed.
        clean_two = re.sub(' n ', '', clean_two)
        clean_two = re.sub('n(?P<beg>[A-Z])', '\g<beg>', clean_two)
        clean_two = clean_two.lower()
        Userlist.append(clean_two.split())

    return Userlist



RepNames=["nrsc","gopleader","teapublican","roaring_repub","gopwhip","coutpost","the_rga", "MittRomney", "Senate_GOPs","CRNC","RepublicanGOP","yrnf","GOP","Reince","NRCC","WashingtonSRC","SenRandPaul","SenatorCollins","SenJohnMcCain","johnboehner","ohiogop","newtgingrich","SenBobCorker", "RoyBlunt","SenatorKirk"]
DemNames=["washdems", "usdemocrats","dncyouthcouncil","ofa_ca", "demlegislators","youngdemocrat","dccc", "TheDemocrats","BarackObama","HouseDemocrats","SenateDems","youngdems","NancyPelosi","donnabrazile","DWStweets","dccc","dscc","CollegeDems","SenatorReid","SenatorDurbin","RepJimMcDermott","PattyMurray","SenatorCardin","ChrisCoons","SenatorMenendez"]
#DemNames=["TheDemocrats","BarackObama"]


random.shuffle(RepNames)
random.shuffle(DemNames)

wordlists = []
listnames = []

SEED_SIZE=.5
DEVELOPMENT_SIZE=.3
Seed_split=int(len(RepNames)* SEED_SIZE)

Dev_split= Seed_split + int(len(RepNames)*DEVELOPMENT_SIZE)  
#wordlists.append(parseCorpus(corpus_Dem))
#wordlists.append(parseURLs(DemURLs))
wordlists.append(parseTweets(DemNames))
listnames.append("Dem")
#wordlists.append(parseCorpus(corpus_Rep))
#wordlists.append(parseURLs(RepURLs))
wordlists.append(parseTweets(RepNames))
listnames.append("Rep")




Seed_List= [wordlists[0][0:Seed_split],wordlists[1][0:Seed_split]]

Dev_List= [wordlists[0][Seed_split:Dev_split],wordlists[1][Seed_split:Dev_split]]

Test_List= [wordlists[0][Dev_split:],wordlists[1][Dev_split:]]


fileObject=open("Seed_List",'w+')
cPickle.dump(Seed_List,fileObject)

fileObject.close()

fileObject=open("Dev_List",'w+')
cPickle.dump(Dev_List,fileObject)


fileObject.close()


fileObject=open("Test_List",'w+')
pickle.dump(Test_List,fileObject)

fileObject.close()




