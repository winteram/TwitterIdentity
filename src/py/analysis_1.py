import pymysql
import nltk
import pyml

# Set up connection
conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='smalls7_groupid', passwd='letspublish', db='smalls7_identity')
cur = conn.cursor()

# Get data for each user (process each user separately)
cur.execute("SELECT Id FROM survey WHERE own_form1 IS NOT NULL")
IDs = cur.fetchall()

for ID in IDs:
    
    # Get entire survey (demographics, political party, nationality, own groups, survey responses)
    cur.execute("SELECT * FROM survey WHERE Id=%s", ID)
    surveyall = cur.fetchall()

    # Get profile information
    cur.execute("SELECT profile.Id, Location, Created_at, Lang, Verified, IF(Profile_bgd_color='C0DEED',1,0) AS color_chg, Geo_enabled, Time_zone, Favourites_count, Followers_count, Friends_count, Statuses_count FROM profile JOIN survey ON Id WHERE Id=%s", ID)
    profile = cur.fetchall()

    # Get tweets of participant
    cur.execute("SELECT TweetText FROM tweet WHERE Id=%s", ID)
    owntweets = cur.fetchall()

    # Get tweets of participants' friends
    cur.execute("SELECT TweetText FROM tweet JOIN relationship ON tweet.Id=relationship.TwitterAccountParentId WHERE tweet.Id=%s", ID)
    friendtweets = cur.fetchall()

    # Get tweets of participants' followers
    cur.execute("SELECT TweetText FROM tweet JOIN relationship ON tweet.Id=relationship.TwitterAccountNodeId WHERE tweet.Id=%s", ID)
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



