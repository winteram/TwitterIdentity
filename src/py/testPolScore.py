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
    # url_bigrams = BigramCollocationFinder._ngram_freqdist(urlText, 2)

    # Create Frequency Distributions for trigrams
    # url_trigrams = BigramCollocationFinder._ngram_freqdist(urlText, 3)

    return [w for w in word_tokenize(urlText) if w not in stopwords.words('english')]

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
        #clean_two = re.sub('[^a-zA-Z #]', '', x)

        ## TODO:  This is actually the encoding of the string
        # this leaves u's at the beginning of things, so we need pull these out. 
        #clean_two = re.sub('u(?P<beg>[A-Z])', '\g<beg>', clean_two)

        ## TODO: Probably these are line endings?  
        # there are still also n's, those should be removed.
        #clean_two = re.sub(' n ', '', clean_two)
        #clean_two = re.sub('n(?P<beg>[A-Z])', '\g<beg>', clean_two)
        #clean_two = clean_two.lower()

    return [w for w in word_tokenize(clean_two)]



def cosine_distance(u, v):
    """
        Returns the cosine of the angle between vectors v and u. This is equal to
        u.v / ||u|| ||v||.
        """
    return numpy.dot(u, v) / (math.sqrt(numpy.dot(u, u)) * math.sqrt(numpy.dot(v, v)))



### Get text for political party dictionaries (from corpora, URLs, and/or Twitter accounts)

#Assign a directory for corpus to be used.
#corpus_Dem = 'politics/Dem'
#corpus_Rep = 'politics/Rep'

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





### Split into train & test groups. This has been re-ordered to match the listnames order. 
testNames = []

for i in range(3):
    testNames.append(DemNames.pop(randrange(0,len(DemNames))))
    testNames.append(RepNames.pop(randrange(0,len(RepNames))))



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




# Input list of wordlists, return list of "score" dictionaries
#TotalDist = FreqDist([word for sublist in wordlists for word in sublist])
##wordRats = []
    #for wordlist in wordlists:
    #wordDist = FreqDist(wordlist)
    #wordRat = {}
    #for word in wordDist.keys():
    #   wordRat[word] = wordDist.freq(word) / TotalDist.freq(word)
#wordRats.append(wordRat)

TotalDist = FreqDist([word for sublist in wordlists for word in sublist])
wordRats = []
for wordlist in wordlists:
    wordDist = FreqDist(wordlist)
    
    b=len(TotalDist.keys())*[0]
    for i,word in enumerate(TotalDist.keys()):
        #Create a series of vectors with the length of the unique set of all words (TotalDist.keys())
        
        b[i] = wordDist.freq(TotalDist.keys()[i]) / TotalDist.freq(word) #This is taking the relative frequency words in the political corpi (each of the two) and dividing by the relative
    #frequency in the entire corpus- kind of wonky- I'm going to add some other measures.
    
        w[i] = wordDist.freq(TotalDist.keys()[i]) #Thi is just relative frequency- within a party
    
    
    
    #in Here put alternate scoring algorithms then additionally vectors like wordRats1, 2, etc to append these to.
    wordRats.append(b)#This gives us vectors which will act as weights in the cosine similiarity measure used later

#In this new program wordRats is not the end of the line- we still need to calculate cosine similarity- where should that go?




# print header for output file
print "Id Party ", " ".join(listnames), " ".join([w + "-we" for w in listnames])


### Go through test user names & get scores for each party
# SELECT DISTINCT(survey.Id) FROM survey JOIN tweet ON survey.Id=tweet.UserId;

for user in testNames:
    catScores = [0] * 2*len(listnames)
    # get tweets of target user
    tweets1= t.statuses.user_timeline(id = user, count = 200)
    tweets2= t.statuses.user_timeline(id = user, count = 200, max_id = tweets1[len(tweets1)-1]['id'])
    tweets3= t.statuses.user_timeline(id = user, count = 200, max_id = tweets2[len(tweets2)-1]['id'])
    tweets= tweets1 + tweets2 + tweets3
	# "SELECT TweetText FROM tweet WHERE UserId='"+user+"';"

    tweetText = ""
    tweetWordCount = 0
    weTweetWordCount = 0
    WeTweetSet=[] # This will be the vector that stores all tweets containing "we" words- it will be of length TotalDist for the dot product stuff.
    WeTweetScore=[]
    TweetScore=[]
    TweetSet=[] #This is the set of all tweets
    
    for tweet in tweets:
        # clean tweet text & tokenize
        tweetText = tweet["text"].encode('utf8')
        
        
        #Note: with the UTF8 encoding a lot of this reg-expression cleanup is not necessary. 
        
        tweetText = re.sub('[^a-zA-Z #]', '', tweetText)
        tweetText = re.sub('(?P<endword>[a-z]+)(?P<begword>[A-Z])', '\g<endword> \g<begword>', tweetText)
        tweetText = tweetText.lower()
        #Note I think we should preserve case sensitivity because things like "FED" vs "fed", "US" vs "us". However, this might get captured better when we use n-grams
        
        tweet_wordlist = word_tokenize(tweetText)
        #tweetWordCount += len(tweet_wordlist) This is unneccessary
        weTweetWC = len(list(set(tweet_wordlist) & set(wewords))) 
        # see if tweet has "we" word(s) in it
        TweetSet.append(tweet_wordlist)
        has_we = False
        if weTweetWC>0:
            has_we = True
            WeTweetSet.append(tweet_wordlist) #put each tweet in the list of we_tweets
    WeFreq=FreqDist([word for sublist in WeTweetSet for word in sublist]) #Make a term frequency distribution for we containing tweets
    AllFreq=FreqDist([word for sublist in TweetSet for word in sublist]) # Freq dist for all tweets

    b=len(TotalDist.keys())*[0]
    c=len(TotalDist.keys())*[0]

    for i,word in enumerate(TotalDist.keys()):
    
        b[i] = WeFreq[word]
        c[i] = AllFreq.freq[word]  # Now this is relative frequency
    for i in range(len(listnames)):

        we_temp=cosine_distance(b,wordRats[i]) # 2nd term will be: wordRats[i]
        all_temp=cosine_distance(c,wordRats[i])
    
        TweetScore.append(all_temp)
        WeTweetScore.append(we_temp)
    
     
    TweetScore[:len(listnames)] = [str(x) for x in TweetScore[:len(listnames)]]
    WeTweetScore[:len(listnames)] = [str(x) for x in WeTweetScore[:len(listnames)]]
    
    
    
    
    
    
    print user, " ".join(TweetScore)
    print user, " ".join(WeTweetScore)





#for ID in IDs:
    # Get tweets of participants' followers

    ### Create dataset for predicting political identity ###


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



