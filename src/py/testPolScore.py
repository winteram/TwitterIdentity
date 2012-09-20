import re
import pymysql
from urllib import urlopen
from bs4 import BeautifulSoup
from nltk import *
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from nltk.collocations import *

wewords = ["we","us","our","ours","ourselves"]
bigram_measures = BigramAssocMeasures()
trigram_measures = TrigramAssocMeasures()

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
    # Create Frequency Distributions for bigrams
    # Dem_bigrams = BigramCollocationFinder._ngram_freqdist(Dem_wordlist, 2)

    # Create Frequency Distributions for trigrams
    # Dem_trigrams = BigramCollocationFinder._ngram_freqdist(Dem_wordlist, 3)

    return [w for w in word_tokenize(urlText) if w not in stopwords.words('english')]


# Get text for political party dictionaries (from corp and/or URLs)

#Assign a directory for corpus to be used.
#corpus_Dem = 'politics/Dem'
#corpus_Rep = 'politics/Rep'

# Republican Party
RepURLs = ["http://whitehouse12.com/republican-party-platform/","http://gop.com/our-party/","http://en.wikipedia.org/wiki/Republican_Party_(United_States)"]

# Democrat Party
#DemURLs = ["http://en.wikipedia.org/wiki/Democratic_Party_(United_States)"]
DemURLs = ["http://www.barackobama.com/record/economy","http://www.barackobama.com/record/education","http://www.barackobama.com/record/environment","http://www.barackobama.com/record/equal-rights","http://www.barackobama.com/record/health-care","http://www.barackobama.com/record/national-security","http://www.barackobama.com/record/taxes","http://www.barackobama.com/record/womens-health","http://en.wikipedia.org/wiki/Democratic_Party_(United_States)"]

# Libertarian Party
lpURLs = ["http://www.lp.org/platform","http://www.lp.org/candidates/elected-officials","http://en.wikipedia.org/wiki/Libertarian_Party_(United_States)"]

# Green Party
GreenURLs = ["http://www.greenparty.org/Platform.php","http://www.gp.org/committees/platform/2012/Platform-2012.html","http://en.wikipedia.org/wiki/Green_Party_of_the_United_States"]

# Constitution Party
ConURLs = ["http://www.constitutionparty.com/party_platform.php","http://www.americanconstitutionparty.com/PlatformDetail.html","http://en.wikipedia.org/wiki/Constitution_Party_(United_States)"]


wordlists = []
listnames = []
#wordlists.append(parseCorpus(corpus_Dem))
wordlists.append(parseURLs(DemURLs))
listnames.append("Dem")
#wordlists.append(parseCorpus(corpus_Rep))
wordlists.append(parseURLs(RepURLs))
listnames.append("Rep")
wordlists.append(parseURLs(lpURLs))
listnames.append("LP")
wordlists.append(parseURLs(GreenURLs))
listnames.append("Green")
wordlists.append(parseURLs(ConURLs))
listnames.append("Const")

# could make wordlists from tweets of party leaders

# Input list of wordlists, return list of "score" dictionaries
TotalDist = FreqDist([word for sublist in wordlists for word in sublist])
wordRats = []
for wordlist in wordlists:
    wordDist = FreqDist(wordlist)
    wordRat = {}
    for word in wordDist.keys():
        wordRat[word] = wordDist.freq(word) / TotalDist.freq(word)
    wordRats.append(wordRat)


# Set up connection
conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='smalls7_groupid', passwd='letspublish', db='smalls7_identity')
cur = conn.cursor()


# Get data for each user (process each user separately)
cur.execute("SELECT DISTINCT(survey.Id), party FROM survey JOIN tweet ON survey.Id = tweet.UserId WHERE party IS NOT NULL")
users = cur.fetchall()

# print header
print "Id Party ", " ".join(listnames), " ".join([w + "-we" for w in listnames])

for user in users:
    catScores = [0] * 2*len(listnames)
    cur.execute("SELECT TweetText FROM tweet WHERE UserId=%s", user[0])
    tweets = cur.fetchall()

    tweetText = ""
    tweetWordCount = 0
    weTweetWordCount = 0
    for tweet in tweets:
        # clean tweet text & tokenize
        tweetText = tweet[0] + " "
        tweetText = re.sub('[^a-zA-Z ]', '', tweetText)
        tweetText = re.sub('(?P<endword>[a-z]+)(?P<begword>[A-Z])', '\g<endword> \g<begword>', tweetText)
        tweetText = tweetText.lower()
        tweet_wordlist = word_tokenize(tweetText)
        tweetWordCount += len(tweet_wordlist)
        weTweetWC = len(list(set(tweet_wordlist) & set(wewords)))
        # see if tweet has "we" word(s) in it
        has_we = False
        if weTweetWC>0:
            has_we = True
            weTweetWordCount += len(tweet_wordlist)
        # go through each word in tweet
        for word in tweet_wordlist:
            # for each category
            for idx, wordRat in enumerate(wordRats):
                # if word in tweet is in dictionary of category, add score
                if word in wordRat:
                    catScores[idx] += wordRat[word]
                    # if word in tweet is in dictionary of category AND we word, add score
                    if has_we:
                        catScores[idx+len(listnames)] += wordRat[word]

    catScores[:len(listnames)] = [str(x / tweetWordCount) for x in catScores[:len(listnames)]]
    catScores[len(listnames):] = [str(x / weTweetWordCount) if weTweetWordCount > 0 else "0" for x in catScores[len(listnames):]]
    print user[0], user[1], " ".join(catScores)


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



