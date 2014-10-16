import sys, os
import pandas as pd
import cPickle as pickle
import re
import numpy as np
import nltk
import codecs
 

os.chdir('C:/Users/Asaf/Documents/GitHub/TwitterIdentity/src/py')



survey=pd.read_pickle('DataFrames/SurveySentiment')


import string 





#This function creates two dictionaries one for categories, like pronounds posneg emoions and an associated id number, and the other dictionary
#is, returned in the function as "dic", are the words Liwc uses and the category ids associated with them
def read_liwc(filename):
    liwc_data = open(filename, 'r')
    
    mode = 0
    cat = {}
    dic = {}

    for line in liwc_data:
        line = line.strip('\r\n')
        if line == '%':
            mode += 1
            continue
        elif mode == 1: # cat
            chunks = line.split('\t')
            cat[chunks[0]] = chunks[1]
        elif mode == 2: # dic
            chunks = line.split('\t')
            word = chunks.pop(0)
            dic[word] = chunks
    return (cat, dic)


survey['fb_liwc']=None #Initialize column for Liwc scores.
survey['fb_tot_words']=None 

#Stuff for crawling each file individually

all_files=[]
error_log=[]


path= 'B:/Participants/'

for i in survey['FBid']:
    path_full=path+i+'/statuses'
    sent_statuses=''
    
    if os.path.exists(path_full):
        all_files.append(path_full)


cat=read_liwc('liwc_file.txt')



for file_name in all_files:

	try:


	    z=pickle.load(open(file_name))
	    # I took out the bit about opening as a binary, it doesn't work some files, and it screws up the the indexing
	    #basically it adds an /r to the end of keys, which makes it more cumbersome. 
	    #Now we want to pull out the all out each status for each person, and then look at the stentiment for that status.
	    #We also want to store the sentiments for each person in another pickle file. This way later we can look at distributions and stuff
	    #for each person initilize a new list that will be the sentiment for all their status
	    sent_statuses=''
	    temp=re.findall(r'\d+',file_name)
	    sent_path='B:/Participants/'+temp[0]+'/status_sentiment'

	    for status_set in z:
	        for status_list in status_set['data']:
	            if 'message' in status_list.keys():
	                    msg=status_list['message'].encode('utf-8')
	                    sent_statuses += ' ' + msg
	    sent_statuses=nltk.word_tokenize(sent_statuses.lower().decode('utf-8')) 
	    freq=nltk.FreqDist(sent_statuses) #Just use nltk to do the work of creating the frequency distribution
	    words=freq.keys() #Gives us each word in someone's set of statuses
	    score={}
	    score2={}
	    for entry in cat[0].keys(): #Go through each category, like "work", "posneg emotions", etc
	        score[entry]=0 #In the new dictionary, "score" just initialize a key for that category, with a value of 0

	#for now I can add up all all the words used in Tweets- but it won't be entirely accurate
	#because of the format and the way things were tokenized. I can do relative scores for distributions. 

	    for i in cat[1].keys():# each word in the Liwc dictionary- check to see if it is in in the frequency distribution
	        if i[-1]=='*': #If it is a stemmed version, indicated by the astericks
	            candidates=[q for q in words if q.startswith(i[0:-1])]
	            if len(candidates) > 0: #If at least one of these stems is present
	                tot_stems=0 # initialize a variable that will represent the total number of occurences with a given stem
	                for k in candidates:
	                    tot_stems+=freq[k]# Add the frequence for each variation
	                    to_tally=cat[1][i]
	                for categ in to_tally:
	                    score[categ]=tot_stems

	        else:
	            if i in words:
	                to_tally=cat[1][i]
	                for categ in to_tally:
	                    score[categ]=freq[i]



	    for i in score.keys():
	        if i in cat[0].keys():
	            name=cat[0][i]
	            score2[name]=int(score[i])

	    all_words=len(sent_statuses)
	     #Note I seem to have to do embed the dictionary in a list, otherwise it won't store to the DataFrame
	    survey.fb_liwc[survey.FBid==temp[0]]=[score2] 
	    survey.fb_tot_words[survey.FBid==temp[0]]=all_words

	except Exception, e:
		print e, temp
		k=(temp,e)
		error_log.append(k)


pickle.dump(survey,open('DataFrames/SurveySentiment', 'wb'))

pickle.dump(error_log,open('DataFrames/Liwc_fb_error', 'wb'))



