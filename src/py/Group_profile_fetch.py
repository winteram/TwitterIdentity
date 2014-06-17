import sys, os

#reload(sys)
#sys.setdefaultencoding('utf-8') #The ensures that string output doesn't come back with a leading 'u', which is weird. 

#This is just specific to my computer. 
sys.path.append('C:\Users\Asaf\Documents\GitHub\TwitterIdentity\src\py')

import pymysql

import urlparse

import cPickle

import pickle

import facebook
from encrypt import *

from collections import defaultdict

from pyfaceb import*

path = 'E:\Participants'


#load the stored variable with ids and corresponding tokens for which we have access

conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='groupid', passwd='letspublish', db='gidb')
cur = conn.cursor()

query="Select AccessToken,fbid from fbconnectionaccounts JOIN users ON users.Id=fbconnectionaccounts.id WHERE length(AccessToken)>120;"

cur.execute(query) 

tokens_encr =cur.fetchall()


#This is the query to get all the people who 

query="Select AccessToken from fbconnectionaccounts JOIN survey ON survey.Id=fbconnectionaccounts.id WHERE (ended < '2014-04-16 1:26:03' AND length(AccessToken)>120);"

cur.execute(query) 

necessity_list=cur.fetchall()

query="Select AccessToken from fbconnectionaccounts JOIN survey ON survey.Id=fbconnectionaccounts.id WHERE (ended < '2014-06-16 1:26:03' AND length(AccessToken)>120) ORDER BY survey.ended ASC;"

cur.execute(query)

full_with_ended=cur.fetchall() # These are just all the people who finished the survey after we fixed the bug and weren't re-authenticating (presumably- because who would want to take this 2X and we informed people
#that they didn't need to take the survey again). In the query it's sorted by date, so we can hit the earliest ones first. 

cur.close()

full_with_ended=[decode_salt(full_with_ended[i][0]) for i in range(len(full_with_ended))]



necessity_tokens=[decode_salt(necessity_list[i][0]) for i in range(len(necessity_list))]






tokens_id = [(decode_salt(tokens_encr[i][1]),decode_salt(tokens_encr[i][0])) for i in range(0,len(tokens_encr))]


#run these first
initial_ids=[tokens_id[i][0] for i in range(len(tokens_id)) if tokens_id[i][1] in necessity_tokens]

initial_ids=[i for i in initial_ids if i in current]


ids_with_ended=[tokens_id[i][0] for i in range(len(token_id) if tokens_id[i][1] in full_with_ended]

path = 'E:\Participants'

K=open(path+'/crawl_lists','r')

to_crawl=cPickle.load(K)

K.close()





group_error_log={}

error_id_list=[]

full_try=initial_ids+to_crawl['re_auth']+to_crawl['expire_later']


for ids in full_try:
        token=[j[1] for j in tokens_id if j[0]==ids]
        k=token[0] 
        graph = facebook.GraphAPI(k)
        object1=open(path+'/'+ids +'/'+'edges', 'r')
        edge=cPickle.load(object1)
        object1.close()
        group_info={}
        group_info_path=open(path + '/' + ids + '/' + 'group_info', 'w+')

        
        for j in edge['groups']['data']:
            try:
                ids_group=j['id']
                group_info[ids_group]={} #just indexing the dictionary with the id, and an empty dictionary
                
                profile=graph.get_object(ids_group)
                
                group_info[ids_group]['profile']=profile
                
                print 'successful'
                
                 
            except Exception as e:
                print (e)
                if ids in group_error_log.keys():
                    
                    group_error_log[ids].append(e)
                else:
                    group_error_log[ids]=[e]
                    
        try:
            cPickle.dump(group_info,group_info_path)
            group_info_path.close()
        except:
            print('could not pickle', [i][1])
            error_id_list.append(i[1])