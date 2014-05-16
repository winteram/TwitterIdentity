

import sys, os

import collections

sys.path.append('C:\Users\Asaf\Documents\GitHub\TwitterIdentity\src\py')
import pymysql

# Set up connection
conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='groupid', passwd='letspublish', db='gidb')
cur = conn.cursor()

# Get names of table (test fcn)
# cur.execute("SHOW TABLES")
#
# r = cur.fetchall()
#
# for table in r:
#    print table

# Count of survey respondents today

#query = "SELECT IUName, ended FROM users JOIN survey ON users.Id=survey.Id WHERE IUname !='none' AND IUname !='' ORDER BY survey.ended ASC"

query="SELECT fbid,IUName FROM users JOIN survey ON users.Id=survey.Id WHERE (ended < '2014-04-12 13:26:03' AND fbid != '')" #This is the time point the change was made. Note:
#I could have just done something like- WHERE lenght(fbaccesstoken)=120, might be smarter actually- let me see if I get the same output. No, screw it, the way I'm doing it will work.
cur.execute(query)

names_prior=cur.fetchall()

#print names_full

FBids_prior=[entries[0] for entries in names_prior]

#query2 = "SELECT fbid FROM users JOIN survey ON users.Id=survey.Id WHERE (ended > '2014-04-12 13:26:03' AND fbid != '')"
#cur.execute(query2)


#names_after=cur.fetchall() 

id_name={}

for i in names_prior:
    id_name[i[0]]=i[1]

#FBids_after=[entries[0] for entries in names_after]
    
#out_set = [name for name in FBids_prior if name not in FBids_after]

#final_name_set=[id_name[i] for i in out_set]

query3="SELECT FBid from users where FBid !=''"

cur.execute(query3)

ids_full=cur.fetchall()
 
ids_full=[entries[0] for entries in ids_full]

FBids_duplicates= [x for x,y in collections.Counter(ids_full).items() if y > 1]

set_mail=[x for x in FBids_prior if x not in FBids_duplicates]

names_mail=[id_name[i] for i in set_mail]

username=names_mail


username_clean=[i for i in username if '@' not in i and i !='none']

email_adresses=[i+"@indiana.edu" for i in username_clean]














'''

for i,j in enumerate(username):
	if j== "AsafBeasley":
		indexer = i


NoNo=username[0:indexer]


query2="SELECT AccessToken from fbconnectionaccounts"

cur.execute(query2)

tokens_full=cur.fetchall()

'''









'''
count= w[1]



lastname='eeiteljo'

j= FindnameIndex(lastname)

j[0]=index2

ListForRA=[user for user in username[index2:] if user not in NoNo]

'''










'''

username_clean=[i for i in username if '@' not in i]

email_adresses=[i+"@indiana.edu" for i in username_clean]

'''


