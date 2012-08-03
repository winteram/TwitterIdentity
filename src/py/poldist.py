import re
import pymysql
from urllib import urlopen
from bs4 import BeautifulSoup
from nltk import *
from nltk.corpus import PlaintextCorpusReader
from nltk.collocations import *

# parse corpus
def parseCorpus(corpusdir):
    # Load the corpus into nltk and store files as separate file ID, which can be accessed by name.
    # to see which files are in the corpus use the command: corpus.fileids()
    corpus = PlaintextCorpusReader(corpusdir, '.*')
    corpusText = corpus.raw()
    corpusText = re.sub('[^a-zA-Z ]', '', corpusText)
    corpusText = re.sub('(?P<endword>[a-z]+)(?P<begword>[A-Z])', '\g<endword> \g<begword>', corpusText)
    corpusText = corpusText.lower()
    return word_tokenize(corpusText)

# parse list of URLs
def parseURLs(urllist):
    # verify the input is a list
    assert type(urllist) == type(list())
    urlText = ""
    for url in urllist:
        urlRaw = urlopen(url).read()
        urlSoup = BeautifulSoup(urlRaw)
        for para in urlSoup.find_all('p'):
            urlText += para.get_text()
        urlText += " " 
    urlText = re.sub('[^a-zA-Z ]', '', urlText)
    urlText = re.sub('(?P<endword>[a-z]+)(?P<begword>[A-Z])', '\g<endword> \g<begword>', urlText)
    urlText = urlText.lower()
    return word_tokenize(urlText)

bigram_measures = BigramAssocMeasures()
trigram_measures = TrigramAssocMeasures()

# Get text for political party dictionaries (from corp and/or URLs)

#Assign a directory for corpus to be used.
corpus_Dem = 'politics/Dem'
corpus_Rep = 'politics/Rep'

# Libertarian Party
lpURLs = ["http://www.lp.org/platform","http://www.lp.org/candidates/elected-officials"]

wordlists = []
listnames = []
wordlists.append(parseCorpus(corpus_Dem))
listnames.append("Dem")
wordlists.append(parseCorpus(corpus_Rep))
listnames.append("Rep")
wordlists.append(parseURLs(lpURLs))
listnames.append("LP")

#Create Frequency Distributions for each of these
DemDist = FreqDist(Dem_wordlist)
RepDist = FreqDist(Rep_wordlist)
LPDist = FreqDist(lp_wordlist)

# Create Frequency Distributions for bigrams
#Dem_bigrams = BigramCollocationFinder._ngram_freqdist(Dem_wordlist, 2)

# Create Frequency Distributions for trigrams
#Dem_trigrams = BigramCollocationFinder._ngram_freqdist(Dem_wordlist, 3)

# get proportions for each term
TotalList = {}

DemList = [(word,DemDist.freq(word)) for word in DemDist.keys()]
DemProp = {}
for word, prop in DemList:
    DemProp.setdefault(word, []).append(prop)
    if word in TotalList:
        TotalList[word] += prop
    else:
        TotalList[word] = prop

RepList = [(word,RepDist.freq(word)) for word in RepDist.keys()]
RepProp = {}
for word, prop in RepList:
    RepProp.setdefault(word, []).append(prop)
    if word in TotalList:
        TotalList[word] += prop
    else:
        TotalList[word] = prop

LPList = [(word,LPDist.freq(word)) for word in LPDist.keys()]
LPProp = {}
for word, prop in LPList:
    LPProp.setdefault(word, []).append(prop)
    if word in TotalList:
        TotalList[word] += prop
    else:
        TotalList[word] = prop

DemRat = {}
for word, prop in DemList:
    DemRat[word] = prop / TotalList[word]

RepRat = {}
for word, prop in RepList:
    RepRat[word] = prop / TotalList[word]

LPRat = {}
for word, prop in LPList:
    LPRat[word] = prop / TotalList[word]



# Set up connection
conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='smalls7_groupid', passwd='letspublish', db='smalls7_identity')
cur = conn.cursor()


# Get data for each user (process each user separately)
cur.execute("SELECT Id, party FROM survey WHERE party IS NOT NULL")
users = cur.fetchall()

for user in users:
    cur.execute("SELECT TweetText FROM tweet WHERE UserId=%s", user[0])
    tweets = cur.fetchall()

    tweetText = ""
    for tweet in tweets:
        tweetText = tweet[0] + " "
        tweetText = re.sub('[^a-zA-Z ]', '', tweetText)
        tweetText = re.sub('(?P<endword>[a-z]+)(?P<begword>[A-Z])', '\g<endword> \g<begword>', tweetText)
        tweetText = tweetText.lower()
        tweet_wordlist = word_tokenize(tweetText)
        for word in tweet_wordlist:
            tweetDem

    tweetDist = FreqDist(tweet_wordlist)

    tweetDem = float(0)
    for word, prob in DemRat.iteritems():
        tweetDem += prob * tweetDist.freq(word)

    tweetRep = float(0)
    for word, prob in RepRat.iteritems():
        tweetRep += prob * tweetDist.freq(word)

    tweetLP = float(0)
    for word, prob in LPRat.iteritems():
        tweetLP += prob * tweetDist.freq(word)

    print user[0], user[1], tweetDem, tweetRep, tweetLP


#for ID in IDs:
    # Get tweets of participants' followers
#    cur.execute("SELECT TwitterAccountParentId, TweetText FROM tweet JOIN relationship ON tweet.Id=relationship.TwitterAccountNodeId WHERE tweet.Id=%s", ID)
#    friendtweets = cur.fetchall()

    ### Create dataset for predicting political identity ###

# Process responses to survey into factors

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



