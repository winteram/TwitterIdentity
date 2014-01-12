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
cur.execute("SELECT COUNT(Id) FROM survey WHERE Date(ended) = Date(NOW())")


# Comments on survey today
cur.execute("SELECT Id, comments FROM survey WHERE Date(ended) = Date(NOW())")
comments_today = cur.fetchall()

# Get count for responses to each of the messages on the twitter bot
#cur.execute("SELECT SUM(username REGEXP '_1$') AS message1, SUM(username REGEXP '_2$') AS message2, SUM(username REGEXP '_3$') AS message3 FROM (SELECT DISTINCT(username) FROM visitors) v")
#something = cur.fetchall()

# Get entire survey
# cur.execute("SELECT * FROM survey")
# surveycont = cur.fetchall()

# Get Ids for survey
cur.execute("SELECT Id FROM survey")
ids = cur.fetchall()

# Get demographics
cur.execute("SELECT Id, gender, yob, country, ethnicity, income, edu FROM survey WHERE own_form1 IS NOT NULL")
demogs = cur.fetchall()

# Get profile information

# Get political identity
# Get the responses to political survey for those who completed it

# Get nationality
# Get responses to nationality survey

# Get tweets of participant

# Get tweets of participants' friends

# Get tweets of participants' followers


### Predict political identity ###

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



