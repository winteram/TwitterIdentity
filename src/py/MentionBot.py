# Before running this program, make sure there is an empty file called tweeted.txt and put it in the working directory.

import sys, time, json, os, random

from twitter import *

#Opted to put the variables in the file as the function, rather than importing them from

oauth_token = "563118238-aVS68vGHeiWuoLCHIOudAPa6hmhnwIBsSkUfeBXt"
oauth_secret = "M6h51pETL8CWkowEeyh6cb7gNpNTyBpl7fLJk45J4Y"
CONSUMER_KEY = "PCMmY6ERIWJM9tgjIiQRwA"
CONSUMER_SECRET = "YWeRQPivyjc9ZUSLQbaFj8enJviPZ8cw55mu3qSuJdk"

maxtweeted = 5 # Initially we don't want to send more than 10.

# The code related to command lines still needs to be tested in the AutoTweet function

def getTweeted():
    g = open("tweeted.txt")

    names = list()

    for line in g:
        names.append(line.rstrip('\n'))

    return names


def AutoTweet(argin, t): 

    already_tweeted = getTweeted()


    try:
        argin = int(argin)
    #If numer, corresponding to twee rate, is input in a command, this can be considered a test sent to Asaf
    except ValueError:
        TweetUser(argin,t)        
    else:
        N = 3600/min(argin, 320) # Rate to tweet in seconds. 
        numtweeted = 0

	while numtweeted < maxtweeted:
            usernames = pullUsername(t) # Pull from stream

	    for user in usernames:

                #Don't tweet names that have been tweeted
                if user not in already_tweeted:

                    # Make sure that number doesn't exceed max within the loop.
                    if numtweeted < maxtweeted:

                        time.sleep(N) # Pause for N seconds to ensure desired rate

                        #TweetUser(user,t)
                        TweetUser('GroupID_Project',t)
                        numtweeted += 1

    

def pullUsername(t): 

    tweeted=open("profiles.txt","a")
    toTweet = list()
    newstream = t.statuses.public_timeline()

    for tweet in newstream:
        toTweet.append(str(tweet['user']['screen_name']))
        tweeted.write(json.dumps(tweet['user'], tweeted) + "\n")

    tweeted.close()

    return toTweet





def TweetUser(username,t):


    k = random.randrange(0,3)
    tweet = ""

    if k == 0:
        tweet = "@" + username + ", you have been randomly selected to participate in a study on identities in Twitter. Click here: http://smallsocialsystems.com/asaf/AboutUs.php?flag=" + username + "_1"
    elif k == 1:
        tweet = "@" + username + ", please participate in our short experiment on how people express their identities on Twitter: http://smallsocialsystems.com/asaf/AboutUs.php?flag=" + username + "_2"
    else:
        tweet = "@" + username + ", please participate in our short survey on how people express their identities on Twitter: http://smallsocialsystems.com/asaf/AboutUs.php?flag=" + username + "_3"

    
    try:
        result = t.statuses.update(status=tweet)
    except TwitterHTTPError as e:
        print "Http error: ", e
    except TwitterError as f:
        print "Other Twitter error: ", f
    except:
        print "Other error:", sys.exc_info()[0]
    else:
	#     (function) Append tweeted names to file
        appendName(username)




def appendName(username):
    f=open("tweeted.txt", "a")
    f.write(username + "\n")
    f.close
    



if __name__ == "__main__": #If we're calling the entire module, as opposed to a specific function

    if len(sys.argv) == 1: #If no rate number was input in the call
        argin = "asaf1" #Just tweet asaf

    else:
        argin = sys.argv[1] #Corresponds to tweet rate

    begin_time = time.time()
    t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

    AutoTweet(argin, t) # Calls the main function which executes all the elements of the bot. 

    print "Total time: " + str(time.time() - begin_time)
