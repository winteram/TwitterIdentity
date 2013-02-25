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

#Note to Asaf(from Asaf): Before you run, change the directory. 
#import sys
#import os
#sys.path.append('/Users/Asaf/Desktop/TwitterML_Feature_Rep')
#os.chdir('/Users/Asaf/Desktop/TwitterML_Feature_Rep')

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
    corpusText = re.sub('[^a-zA-Z ]', '', corpusText)
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
        clean_two = re.sub('[^.a-zA-Z1-9 #:/-]', '', x)

        ## TODO:  This is actually the encoding of the string
        # this leaves u's at the beginning of things, so we need pull these out. 
        #clean_two = re.sub('u(?P<beg>[A-Z])', '\g<beg>', clean_two)

        ## TODO: Probably these are line endings?  
        # there are still also n's, those should be removed.
        #clean_two = re.sub(' n ', '', clean_two)
        #clean_two = re.sub('n(?P<beg>[A-Z])', '\g<beg>', clean_two)
        #clean_two = clean_two.lower()


    return clean_two.split() #This puts the words in the string in a list. 


# URLs representing each party (including platforms)
RepURLs = ["http://whitehouse12.com/republican-party-platform/","http://gop.com/our-party/","http://en.wikipedia.org/wiki/Republican_Party_(United_States)"]
DemURLs = ["http://www.barackobama.com/record/economy","http://www.barackobama.com/record/education","http://www.barackobama.com/record/environment","http://www.barackobama.com/record/equal-rights","http://www.barackobama.com/record/health-care","http://www.barackobama.com/record/national-security","http://www.barackobama.com/record/taxes","http://www.barackobama.com/record/womens-health","http://en.wikipedia.org/wiki/Democratic_Party_(United_States)"]
lpURLs = ["http://www.lp.org/platform","http://www.lp.org/candidates/elected-officials","http://en.wikipedia.org/wiki/Libertarian_Party_(United_States)"]
GreenURLs = ["http://www.greenparty.org/Platform.php","http://www.gp.org/committees/platform/2012/Platform-2012.html","http://en.wikipedia.org/wiki/Green_Party_of_the_United_States"]
ConURLs = ["http://www.constitutionparty.com/party_platform.php","http://www.americanconstitutionparty.com/PlatformDetail.html","http://en.wikipedia.org/wiki/Constitution_Party_(United_States)"]

# Twitter account names for party leaders
# Could also score accounts by # of lists with party name as title

RepNames=["MittRomney", "Senate_GOPs","CRNC","RepublicanGOP","yrnf","GOP","Reince","NRCC","WashingtonSRC","SenRandPaul","SenatorCollins","SenJohnMcCain","johnboehner","ohiogop","newtgingrich","SenBobCorker", "RoyBlunt","SenatorKirk"]
DemNames=["TheDemocrats","BarackObama","HouseDemocrats","SenateDems","youngdems","NancyPelosi","donnabrazile","DWStweets","dccc","dscc","CollegeDems","SenatorReid","SenatorDurbin","RepJimMcDermott","PattyMurray","SenatorCardin","ChrisCoons","SenatorMenendez"]



### create lists of words for each party
wordlists = []
listnames = []
#wordlists.append(parseCorpus(corpus_Dem))
#wordlists.append(parseURLs(DemURLs))
wordlists.append(parseTweets(DemNames))
listnames.append("Dem")
#wordlists.append(parseCorpus(corpus_Rep))
#wordlists.append(parseURLs(RepURLs))
wordlists.append(parseTweets(RepNames))
listnames.append("Rep")
#wordlists.append(parseURLs(lpURLs))


fileObject=open("WordLists",'w+')
cPickle.dump(wordlists,fileObject)


fileObject.close()







# print header for output file

