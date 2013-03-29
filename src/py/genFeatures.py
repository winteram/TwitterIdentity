import argparse
import pymysql

#Minimum Frequency Thresholds
UNIGRAM_THRESHOLD= 7
BIGRAM_THRESHOLD = 5
TRIGRAM_THRESHOLD= 4
STEM_THRESHOLD= 7
ENDING_THRESHOLD=5
HASH_THRESHOLD= 4

#Minimum Number of Users Thresholds
UNIGRAM_THRESHOLD_USER= 5
BIGRAM_THRESHOLD_USER= 4
TRIGRAM_THRESHOLD_USER= 2
STEM_THRESHOLD_USER= 3
ENDING_THRESHOLD_USER=2
HASH_THRESHOLD_USER= 4



def genPartyWordLists(savefiles):
    party1,party2 = "democrat","republican"
    conn = pymysql.connect(host='', port=3306, user='groupid', passwd='LetsPublish!', db='group_identity')
    cur = conn.cursor()

    cur.execute('SELECT survey.Id, TweetText FROM survey JOIN tweet WHERE survey.party = "'+party1+'" AND survey.Id=tweet.UserId ORDER BY survey.Id;')

    # This is the list of users & tweets in party1
    G1List=cur.fetchall()

    cur.execute('SELECT survey.Id, TweetText FROM survey JOIN tweet WHERE survey.party = "'+party2+'" AND survey.Id=tweet.UserId ORDER BY survey.Id;')

    # This is the list of users & tweets in party1
    G2List=cur.fetchall()

    party_list=[G1List,G2List]

    all_words=[]
    words_by_user={}
    for party in party_list:
        for tweet in party:
		user = tweet[0]
		words = tweet[1].split(' ')
		if user in words_by_user:
			words_by_user[user].extend(words)
		else:
			words_by_user[user] = words
		all_words.extend(words)

    if savefiles:
	    fileObject=open("WordLists.pkl",'w+')
	    cPickle.dump(all_words,fileObject)
	    fileObject.close()
	    
	    fileObject=open("WordsByUser.pkl",'w+')
	    cPickle.dump(words_by_user,fileObject)
	    fileObject.close()

    return all_words,words_by_user

# Function I pulled off stack overflow that unshortens twitter URLS:
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

# G1Corp = The words, hashtags, urls or whatever raw set we have extracted associated with a class (G1)
# G2Corp is the other class
# n = minimum frequency a potential feature must appear within the corpus.
def generate_K_most(G1Corp, G2Corp, n, j): 

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


	# Now create a list with proportions for each word in the Democratic corpus. 

    for i in GP1_FinalFreq.keys():
        rat= (GP1_FinalFreq[i]/FullFreq[i])
        G1Dic[i]=rat
	
	# This sorts the dictionary items into tuples in descending order by ratio value. 
    sorted_G1 = sorted(G1Dic.iteritems(), key=operator.itemgetter(1),reverse=True)

    for word in GP2_FinalFreq.keys():
        x= (GP2_FinalFreq[word]/FullFreq[word])
        G2Dic[word]=x

    sorted_G2= sorted(G2Dic.iteritems(), key=operator.itemgetter(1),reverse=True)

    G1_set=[x[0] for x in sorted_G1]
    G2_set=[x[0] for x in sorted_G2]

	# K_vector= G1_set+G2_set
    K_vector=sorted_G1[0:200]+sorted_G2[0:200]

    K_final1=[]
    K_final2=[]

	# This part filters out words that appear among less than j users-
	# In the WordsByUser- It would probably be smarter to split it up before importing-
	# this way it's not contingent on knowing how many users are present. Maybe make 

    for word in sorted_G1:
            count=0
            if len(K_final1)==200 or word[1] <.6:
                break
            for users in G1Corp:
                if word[0] in users:
                    count=count+1
                    if count == j:
                        K_final1.append(word[0])
                        break

    for word in sorted_G2:
            count=0
            if len(K_final2)==200 or word[1] <.6:
                break
            for users in G2Corp:
                if word[0] in users:
                    count=count+1
                    if count == j:
                        K_final2.append(word[0])
                        break


    K_final=[K_final1,K_final2]

    return K_final


def extractTerms(wordlists,WordsByUser):

	regex1=re.compile(r'(https?://\S+)') # This pulls the whole url.
	regex2=re.compile("(?P<url>https?://[^\s/]+)") # This specifically pulls domains of URLs


	G1URL_temp_users=[[regex1.findall(word) for word in users] for users in WordsByUser[0]]
	G1FullURL_users=[[word for user in users for word in user] for users in G1URL_temp_users]

	G2URL_temp_users=[[regex1.findall(word) for word in users] for users in WordsByUser[1]]
	G2FullURL_users=[[word for user in users for word in user] for users in G1URL_temp_users]

	# This will pull hashtag terms for Democrats
	G1Hash_users=[[word for word in users if word.startswith('#')] for users in WordsByUser[0]] 
	G2Hash_users=[[word for word in users if word.startswith('#')] for users in WordsByUser[1]] 

	# Above sets are used for exclusion purposes in a later piece of code. 
	# The code below is a bit redundant but makes everytihng lowercase.
	G1HashFinalUser= [[re.sub('[^a-zA-Z ]','',word).lower() for word in users if word.startswith('#')] for users in WordsByUser[0]]
	G2HashFinalUser= [[re.sub('[^a-zA-Z ]','',word).lower() for word in users if word.startswith('#')] for users in WordsByUser[1]]


	# G1Hash=[word for word in wordlists[0] if word.startswith('#')] #This will pull hashtag terms for Democrats
	# G2Hash=[word for word in wordlists[1] if word.startswith('#')]
	G1Mentions =[[word for word in users if word.startswith('@')] for users in WordsByUser[0]]
	G2Mentions =[[word for word in users if word.startswith('@')] for users in WordsByUser[1]]

	# Now we want to exclude all hash tag terms and urls from our set of unigrams
	# This gives us all nonhashtag and non-urls 3 or more characters long
	# G1Words=[word for word in wordlists[0] if word not in G1Hash + G1FullURL and len(word)>2] 
	# G2Words=[word for word in wordlists[1] if word not in G2Hash + G2FullURL and len(word)>2]


	# Now I want to get the unigrams with hashtags and urls removed
	Unigrams_Group1_by_User=[]
	words_for_ngrams1=[] 
	# This will be the same as the unigram list EXCEPT it will include words of 2 or less characters for construction of bigrams and trigrams
	for i, user in enumerate(WordsByUser[0]):
	    k=[re.sub('[^a-zA-Z ]','',word).lower() for word in user if word not in G1Hash_users[i] + G1FullURL_users[i] + G1Mentions[i] and len(word) > 2]
	    w=[re.sub('[^a-zA-Z ]','',word).lower() for word in user if word not in G1Hash_users[i] + G1FullURL_users[i] + G1Mentions[i]]
	    Unigrams_Group1_by_User.append(k)
	    words_for_ngrams1.append(w)

	Unigrams_Group2_by_User=[]
	words_for_ngrams2=[] 
	for i, user in enumerate(WordsByUser[1]):
	    k=[re.sub('[^a-zA-Z ]','',word).lower() for word in user if word not in G2Hash_users[i] + G2FullURL_users[i] + G2Mentions[i] and len(word) > 2]
	    w=[re.sub('[^a-zA-Z ]','',word).lower() for word in user if word not in G2Hash_users[i] + G2FullURL_users[i] + G2Mentions[i]] 
	    Unigrams_Group2_by_User.append(k)
	    words_for_ngrams2.append(w)

	# Use NLTK collocation functions to generate meaningful bigrams and trigrams. This is a bit tricky because the function returns n-best and we have to 
	# somewhat arbitrarily decide what n should be. 
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


	G1Bigram_by_User= [[word for word in bigrams(users) if word in bigrams1] for users in words_for_ngrams1]
	G2Bigram_by_User= [[word for word in bigrams(users) if word in bigrams2] for users in words_for_ngrams2]

	G1Trigram_by_User= [[word for word in trigrams(users) if word in trigrams1] for users in words_for_ngrams1]
	G2Trigram_by_User= [[word for word in trigrams(users) if word in trigrams2] for users in words_for_ngrams2]

	G1Stems_by_User= [[stem(word) for word in users] for users in Unigrams_Group1_by_User]
	G2Stems_by_User= [[stem(word) for word in users] for users in Unigrams_Group2_by_User]

	# Suffixes- note that since special characters were simply deleted and replaced with an empty string- some these things are actually full words
	G1ending_by_User= [[re.sub(stem(word),'',word) for word in users if re.sub(stem(word),'',word) !=''] for users in Unigrams_Group1_by_User]
	G2ending_by_User= [[re.sub(stem(word),'',word) for word in users if re.sub(stem(word),'',word) !=''] for users in Unigrams_Group2_by_User]

	k_most_words=generate_K_most(Unigrams_Group1_by_User,Unigrams_Group2_by_User,UNIGRAM_THRESHOLD,UNIGRAM_THRESHOLD_USER)
	k_most_stems=generate_K_most(G1Stems_by_User,G2Stems_by_User,STEM_THRESHOLD,STEM_THRESHOLD_USER)
	k_most_hash=generate_K_most(G1HashFinalUser,G2HashFinalUser,HASH_THRESHOLD,HASH_THRESHOLD_USER)
	k_most_bigrams=generate_K_most(G1Bigram_by_User,G2Bigram_by_User,BIGRAM_THRESHOLD,BIGRAM_THRESHOLD_USER)
	k_most_trigrams=generate_K_most(G1Trigram_by_User,G2Trigram_by_User,TRIGRAM_THRESHOLD,TRIGRAM_THRESHOLD_USER)
	k_most_ending=generate_K_most(G1ending_by_User,G2ending_by_User,ENDING_THRESHOLD,ENDING_THRESHOLD_USER)



def ScoreGenerate(UserSet,K_most_vector):
    fullset=[word for word in UserSet if word in K_most_vector[0]+K_most_vector[1]]
    setfreq=FreqDist(fullset)
    v1=[setfreq.freq(word) for word in K_most_vector[0]]
    v2=[setfreq.freq(word) for word in K_most_vector[1]]
    finalscore=[v1,v2]

    return finalscore

def UserScores(words,stems,hashes,bigrams,trigrams,endings):	
    conn = pymysql.connect(host='', port=3306, user='groupid', passwd='LetsPublish!', db='group_identity')
	cur = conn.cursor()


	cur.execute("SELECT DISTINCT(Id) FROM survey;")



	all_user_id=cur.fetchall()
	
	regex1=re.compile(r'(https?://\S+)') # This pulls the whole url.
	regex2=re.compile("(?P<url>https?://[^\s/]+)") # This specifically pulls stems of URLs

	UserFeatures={}

	AllUserTweets=[]
	TweetsByUsers=[] # This will eventually give us all the tweets in semi-tokenized form, for each user
	for user in all_user_id[200:250]:
	    username=user[0]
	    cur.execute("SELECT TweetText FROM tweet WHERE UserId='"+ username +"';")
	    temptweets1=cur.fetchall()
	    # I am pretty sure I can assign scores and dictionary elements here. I need to import the K-vectors, though.
	    TweetforUser=""
	    raw=[]

	    for tweets in temptweets1:

	        TweetforUser=TweetforUser + " " + tweets[0]# This is just the tweets by user

	    raw=TweetforUser.split()
	    AllUserTweets.append(raw)
	    raw_URLforUser=[regex1.findall(word) for word in raw]
	    #The findall function puts the output in brackets, so the next function is to take the brackets out- so it's no longer a nested list. 
	    UserUrl=[word for words in raw_URLforUser for word in words]
	    raw_HashforUser=[word for word in raw if word.startswith('#')]
	    raw_MentionforUser=[word for word in raw if word.startswith('@')]


	    hash_final=[word.lower() for word in raw_HashforUser]

	    unigram1=[re.sub('[^a-zA-Z ]','',word).lower() for word in raw if word not in UserUrl + raw_HashforUser+ raw_MentionforUser]

	    bigrams_for_user=bigrams(unigram1)
	    trigrams_for_user=trigrams(unigram1)

	    stems_for_user=[stem(word) for word in unigram1]

	    endings_for_user=[re.sub(stem(word),'',word) for word in unigram1]

	    UserFeatures[username]={}
	    UserFeatures[username]['unigram']=ScoreGenerate(unigram1,words)
	    UserFeatures[username]['bigram']=ScoreGenerate(bigrams_for_user,bigrams)
	    UserFeatures[username]['trigram']=ScoreGenerate(trigrams_for_user,trigrams)
	    UserFeatures[username]['hash']=ScoreGenerate(hash_final,hashes)
	    UserFeatures[username]['stem']=ScoreGenerate(stems_for_user,stems)
	    UserFeatures[username]['ending']=ScoreGenerate(endings_for_user,endings)
		TweetsByUsers.append(TweetforUser.split())


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Create tweet features for classifier')
	parser.add_argument('-s','--save', dest='savefiles', action='store_true', default=False,
						help='Save intermediate files')
	parser.add_argument('-l','--load', dest='loadfiles', metavar='LLL', default=0,
						help='Load from files. Value indicates start point: 0) Do not load from files; 1) Load word lists of tweets; 2) Load extracted term lists')
	args = parser.parse_args()
	
	if loadfiles == 0:
		wordlist1,wordlist2 = genPartyWordLists(savefiles)
		words,stems,hashes = extractTerms(wordlist1,wordlist2)
		UserScores(words,stems,hashes,bigrams,trigrams,endings)
	elif loadfiles == 1:
		fh1=open('WordLists.pkl','r')
		wordlist1,wordlist2=cPickle.load(fh1)
		fh1.close()

		fh2=open('WordsByUser.pkl','r')
		wbu1,wbu2=cPickle.load(fh22)
		fh2.close()
		words,stems,hashes,bigrams,trigrams,endings = extractTerms(wordlist1,wordlist2)
		UserScores(words,stems,hashes,bigrams,trigrams,endings)
	elif loadfiles == 2:
		object1=open('k_words','r')
		words=cPickle.load(object1)
		object1.close()

		fileObject=open('k_stems','r')
		stems=cPickle.load(fileObject)
		fileObject.close()

		fileObject=open("k_hash",'r')
		hashes=cPickle.load(fileObject)
		fileObject.close()

		fileObject=open("k_bigram",'r')
		bigrams=cPickle.load(fileObject)
		fileObject.close()

		fileObject=open("k_trigram",'r')
		trigrams=cPickle.load(fileObject)
		fileObject.close()

		fileObject=open("k_ending",'r')
		endings=cPickle.load(fileObject)
		fileObject.close()
		UserScores(words,stems,hashes,bigrams,trigrams,endings)
		
		
    
