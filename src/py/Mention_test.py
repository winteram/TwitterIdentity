import sys, time, json, os

from twitter import *

#Note: A file called Twitter.txt must be created and stored in the working directory for this to work.
#This file contains all of the tweeted names. 


os.chdir("/Users/asaf/Documents") #Obviously specific to where I have things stored in my computer. 





oauth_token = "563118238-aVS68vGHeiWuoLCHIOudAPa6hmhnwIBsSkUfeBXt"
oauth_secret = "M6h51pETL8CWkowEeyh6cb7gNpNTyBpl7fLJk45J4Y"
CONSUMER_KEY = "PCMmY6ERIWJM9tgjIiQRwA"
CONSUMER_SECRET = "YWeRQPivyjc9ZUSLQbaFj8enJviPZ8cw55mu3qSuJdk"

t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))





def pullUsername(t):
    
    tweeted=open("tweeted.txt","a")
    toTweet1 = list()
    newstream = t.statuses.public_timeline()

    for tweet in newstream:
        
        toTweet1.append(tweet['user']['screen_name'])
        json.dumps(tweet['user'], tweeted)
        tweeted.close()
        


    toTweet = list()



    for i in toTweet1:
        toTweet.append(str(i)) # take off the leading u in the list, make all els strings

    #TweetLoop(toTweet)
    return toTweet

k= pullUsername(t)


    

def TweetLoop(k):
    maxtweet=5
    numtweet=0
    fullTweet=list()
    while maxtweet > numtweet:
        for i in k:
            if numtweet < maxtweet:
                
                fullTweet.append(TweetUser(i,t))
                numtweet += 1

    return fullTweet


def appendName(username):
    f=open("Tweeted.txt", "a")
    f.write(username + "\n")
    f.close
    

def getTweeted():
    g = open("tweeted.txt")

    names = list()

    for line in g:
        names.append(line.rstrip('\n'))

    return names




# get already tweeted usernames
already_tweeted = getTweeted()




        


def TweetUser(username,t):


    


    try:
        print "g"
        #result = t.statuses.update(status=message)
    except TwitterHTTPError as e:
        print "Http error: ", e
    except TwitterError as f:
        print "Other Twitter error: ", f
    except:
        print "Other error:", sys.exc_info()[0]
    else:
	#     (function) Append tweeted names to file

        appendName(username)
    
    message = '@' + username +', Please consider participating in our short study on how people express \
their identities on Twitter http://smallsocialsystems.com/asaf/AboutUs.php?flag=' + username

    #Not sure if this is the best message

    #t.statuses.update(status= message)

    return message



def TweetAsaf(username,t):

    message = '@' + username +', Please consider participating in our short experiment on how people express \
their identities on Twitter http://smallsocialsystems.com/asaf/AboutUs.php?flag=' + username


    #t.statuses.update(status=message)


    try:
        result = t.statuses.update(status=message)
    except TwitterHTTPError as e:
        print "Http error: ", e
    except TwitterError as f:
        print "Other Twitter error: ", f
    except:
        print "Other error:", sys.exc_info()[0]
    else:
	#(function) Append tweeted names to file

        appendName(username)
    

    return message



   
