# NOTE!  uses python-twitter, not sixohsix's twitter package
# 
import pymysql
import twitter
import operator
from encrypt import *

tokens = get_tokens('GroupID_Project')
api = twitter.Api(consumer_key=tokens['CONSUMER_KEY'], consumer_secret=tokens['CONSUMER_SECRET'], access_token_key=tokens['oauth_token'], access_token_secret=tokens['oauth_secret'])


data = api.GetFollowerIDs()
followerids = data['ids']
followers = []
for i in range(1,1+len(followerids)/100):
	idx = min(len(followerids),100*i-1)
	followers.extend(api.UsersLookup(user_id=followerids[100*(i-1):idx-1]))

followers_encoded = []
for follower in followers:
	followers_encoded.append(encode_salt(follower.screen_name))

conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='smalls7_groupid', passwd='LetsPublish!', db='smalls7_identity')
cur = conn.cursor()

flist = '"' + '","'.join(followers_encoded) + '"'
cur.execute('SELECT Id, username, own_form1, own_form3, own_form5 FROM survey WHERE username IN ('+flist+')')
survey_followers = cur.fetchall()

own_groups = {}
for surveyer in survey_followers:
	for sidx in range(2,5):
		if surveyer[sidx] != None and surveyer[sidx] != '':
			if surveyer[sidx].lower() in own_groups:
				own_groups[surveyer[sidx].lower()] += 1
			else:	
				own_groups[surveyer[sidx].lower()] = 1

# write output, for safe keeping
fh = open('followgroups.csv','w')
for k, v in own_groups.iteritems():
	if k != '':
		fh.write('%s,%d\n' % (k,v))
fh.close()
