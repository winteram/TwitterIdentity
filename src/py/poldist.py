import pymysql
import urllib
import html2text
#import nltk

# Get text for political party dictionaries (from corp and/or URLs)

h = html2text.HTML2Text()
h.ignore_links = True
h.ignore_images = True
h.body_width = 0

gp_raw = "http://www.gp.org/committees/platform/2010/democracy.php"
j = urllib.urlopen(gp_raw)
data = j.read()
encoding = 'utf-8'
gp_data = data.decode(encoding)
gp = h.handle(gp_data)

print gp

# Set up connection
conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='smalls7_groupid', passwd='letspublish', db='smalls7_identity')
cur = conn.cursor()

# Get data for each user (process each user separately)
cur.execute("SELECT Id FROM survey JOIN profile ON Id WHERE Followers_count > 90 AND Followers_count < 110 AND own_form1 IS NOT NULL")
IDs = cur.fetchall()

for ID in IDs:
    # Get tweets of participants' followers
    cur.execute("SELECT TwitterAccountParentId, TweetText FROM tweet JOIN relationship ON tweet.Id=relationship.TwitterAccountNodeId WHERE tweet.Id=%s", ID)
    friendtweets = cur.fetchall()

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



