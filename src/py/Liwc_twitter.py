
import sys, os
import pandas as pd
import cPickle as pickle
import re
import numpy as np
import nltk
 

os.chdir('C:/Users/Asaf/Documents/GitHub/TwitterIdentity/src/py')



survey=pd.read_pickle('DataFrames/SurveySentiment')


import string 

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
survey['tw_liwc']=None #Initialize column for Liwc scores.
survey['tw_tot_words']=None 
#cat gives us the dictionaries of words that we are looking for and their associated categories, cat[1], as well as the Liwc categories
#
cat=read_liwc('liwc_file.txt')

tw_ids=os.listdir('B:/Twitter_Part')
path='B:/Twitter_Part/'
error_log=[]

 # take every tweet's sentiment and combine them all. 


for j in tw_ids:

    sent_statuses=''# This is just the collection of all statuses. 
    filename=path+str(j)+'/tweets'
    
    try:

        z=pickle.load(open(filename))
        sent_path=path+str(j)+'/LIWC'
        for status in z:
            if 'text' in status.keys():
                if status['text'] != 'None':
                    message=status['text'].encode('utf-8')


                    #Here is where I need to reference some cool function that does the appropriate stuff with LIWC

                    # Features- Takes in a text string, tokenizes it using nltk, also, make it lower case. 
                    # Two ways to to do it. Just, agregate all of a person's info- yeah, just agregate for now 

                    sent_statuses+= ' '+ message







        sent_statuses=nltk.word_tokenize(sent_statuses.lower())
        freq=nltk.FreqDist(sent_statuses)
        words=freq.keys()
        score={}
        score2={}
        for entry in cat[0].keys():
            score[entry]=0
        #Initialize a dictionary to keep track of the score for each category- at the end if a category is not represented
        #I can add it as a key with frequency 0. Also, for now I can add up all all the words used in Tweets- but it won't be entirely accurate
        #because of the format and the way things were tokenized. I can do relative scores for distributions. 

        for i in cat[1].keys():# each word in the Liwc dictionary- check to see if it is in in the frequency distribution
            if i[-1]=='*':
                candidates=[j for j in words if j.startswith(i[0:-1])]
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

        survey.tw_liwc[survey.Twitid==j]=[score2]
        survey.tw_tot_words[survey.Twitid==j]=all_words

                
          
                
                    
                
       # else:
            
            
            
        
   
        
    
    except Exception, e:
    	print e


pickle.dump(survey,open('DataFrames/SurveySentiment', 'wb'))