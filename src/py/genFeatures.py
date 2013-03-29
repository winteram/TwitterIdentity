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


# G1Corp= The words, hashtags, urls or whatever raw set we have extracted associated with a class (G1), 
# G2 is the other class, n = num minimum frequency a potential feature must appear within the corpus.
def generate_K_most(G1Corp, G2Corp, n, j): 
    
    #This will eventually need six parameters- 3 more for the WordsByUser versions
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


	# Now create a list with proportions for each word in the Democratic corpus 
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

	# This part filters out words that appear among less than j users- In the WordsByUser- 
	# It would probably be smarter to split it up before importing- this way it's not contingent on knowing how many
	# users are present. Maybe make 
    for word in sorted_G1:
		count=0
		if len(K_final1)==200:
			break
		for users in G1Corp:
			if word[0] in users:
				count=count+1
				if count == j:
					K_final1.append(word)
					break
        
    for word in sorted_G2:
		count=0
		if len(K_final2)==200:
			break
		for users in G2Corp:
			if word[0] in users:
				count=count+1
				if count == j:
					K_final2.append(word)
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


	# do the same for hash tags. Then create one for loop excluding words- user by user, to be efficient [user set of words[i]]
	# not in hash[i]+URL[i]
	# Eventual function just needs 4 parameters- minimum frequency, minimum 

	# takes out all the full URLs, but puts them as a set of lists
	# G1URL_temp=[regex1.findall(word) for word in wordlists[0]] 
	# makes the set of lists with strings within them a simple list of strings.
	# G1FullURL=[word for words in G1URL_temp for word in words] 


	# unshorten the URLs
	# G1FullURL_final=[[unshorten_url(url) for url in users] for users in G1FullURL_users]

	# take the stems of these unshortened URLs 
	# G1URL_stemtemp=[regex2.findall(word) for word in G1FullURL_final]

	# take the stems out of lists and make them simply a series of strings in one list
	# This is the final one we care about
	# G1URL_stem_final=[word for words in G1URL_stemtemp for word in words] 


	# Doing the same for group 2
	# G2URL_temp=[regex1.findall(word) for word in wordlists[1]]
	# G2FullURL=[word for words in G2URL_temp for word in words]

	# unshorten URLs
	# G2FullURL_final=[unshorten_url(url) for url in G2FullURL]

	# take the stem of these unshortened URLs
	# G2URL_stemtemp=[regex2.findall(word) for word in G2FullURL_final]
	# G2URL_stem_final=[word for words in G2URL_stemtemp for word in words] #This is the final one we care about


	# Now, we want to separate the hashtags terms
	# G1URL_temp_users1=[[regex1.findall(word) for word in users] for users in WordsByUser[0]]
	# G1FullURL_users=[[word for user in users for word in user] for users in G1URL_temp_users1]

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
	for i, user in enumerate(WordsByUser[0]):
	    k=[re.sub('[^a-zA-Z ]','',word).lower() for word in user if word not in G1Hash_users[i] + G1FullURL_users[i] + G1Mentions[i] and len(word) > 2]
	    Unigrams_Group1_by_User.append(k)


	Unigrams_Group2_by_User=[]
	for i, user in enumerate(WordsByUser[1]):
	    k=[re.sub('[^a-zA-Z ]','',word).lower() for word in user if word not in G2Hash_users[i] + G2FullURL_users[i] + G2Mentions[i] and len(word) > 2]
	    Unigrams_Group2_by_User.append(k)


	G1Stems_by_User= [[stem(word) for word in users] for users in Unigrams_Group1_by_User]
	G2Stems_by_User= [[stem(word) for word in users] for users in Unigrams_Group2_by_User]
	G1Bigram_by_User= [bigrams(users) for users in Unigrams_Group1_by_User]
	G2Bigram_by_User= [bigrams(users) for users in Unigrams_Group2_by_User]

	G1Trigram_by_User= [trigrams(users) for users in Unigrams_Group1_by_User]
	G2Trigram_by_User= [trigrams(users) for users in Unigrams_Group2_by_User]

	G1_trigrams = BigramCollocationFinder._ngram_freqdist(G1Words, 3)

	k_most_words=generate_K_most(Unigrams_Group1_by_User,Unigrams_Group2_by_User,7,5)
	k_most_stems=generate_K_most(G1Stems_by_User,G2Stems_by_User,7,5)
	k_most_hash=generate_K_most(G1HashFinalUser,G2HashFinalUser, 5,4)
	k_most_bigrams=generate_K_most(G1Bigram_by_User,G2Bigram_by_User,5,4)
	k_most_trigrams=generate_K_most(G1Trigram_by_User,G2Trigram_by_User,5,4)



def ScoreGenerate(UserSet,K_most_vector):
    fullset=[word for word in UserSet if word in K_most_vector[0]+K_most_vector[1]]
    setfreq=FreqDist(fullset)
    v1=[setfreq.freq(word) for word in K_most_vector[0]]
    v2=[setfreq.freq(word) for word in K_most_vector[1]]
    finalscore=[v1,v2]

    return finalscore


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
	elif loadfiles == 1:
		fh1=open('WordLists.pkl','r')
		wordlist1,wordlist2=cPickle.load(fh1)
		fh1.close()

		fh2=open('WordsByUser.pkl','r')
		wbu1,wbu2=cPickle.load(fh22)
		fh2.close()
		words,stems,hashes,bigrams,trigrams,endings = extractTerms(wordlist1,wordlist2)
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
		
		
    
