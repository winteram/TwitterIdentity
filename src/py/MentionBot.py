# Before running this program, make sure there is an empty file called Tweeted.txt and put it in the working directory.

import sys, time, json, os, random

from twitter import *

#Opted to put the variables in the file as the function, rather than importing them from

oauth_token = "563118238-aVS68vGHeiWuoLCHIOudAPa6hmhnwIBsSkUfeBXt"
oauth_secret = "M6h51pETL8CWkowEeyh6cb7gNpNTyBpl7fLJk45J4Y"
CONSUMER_KEY = "PCMmY6ERIWJM9tgjIiQRwA"
CONSUMER_SECRET = "YWeRQPivyjc9ZUSLQbaFj8enJviPZ8cw55mu3qSuJdk"

t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

maxtweeted = 10 # Initially we don't want to send more than 10.




if __name__ == "__main__": #If we're calling the entire module, as opposed to a specific function

    if len(sys.argv) == 1: #If no rate number was input in the call
        argin = "asaf1" #Just tweet asaf

    else:
        argin = sys.argv[1] #Corresponds to tweet rate

begin_time = time.time()


AutoTweet(argin) # Calls the main function which executes all the elements of the bot. 


print "Total time: " + str(time.time() - begin_time)





# The code related to command lines still needs to be tested in the AutoTweet function

def AutoTweet(argin): 

    already_tweeted = getTweeted()

    N = 3600/min(argin, 320) # Rate to tweet in seconds. 

    usernames = pullUsername(t) # Pull from stream

    if int(argin) == argin:
        numtweeted = 0
        
	while numtweeted < maxtweeted:

	    for user in usernames:

                #Don't tweet names that have been tweeted
                if user not in already_tweeted:


                    # Make sure that number doesn't exceed max within the loop.

                    if numtweeted < maxtweeted:

                        time.sleep(N) # Pause for N seconds to ensure desired rate

                        TweetUser(user,t)

                        numtweeted += 1


    #If numer, corresponding to twee rate, is input in a command, this can be considered a test sent to Asaf
    else:

        TweetUser(argin,t)



    

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
        toTweet.append(str(i)) # take off the leading u in the list, make all elements strings

    return toTweet





def TweetUser(username,t):


    k = random.randrange(0,3)

    if k == 0:
        message = '@' + username + ", You have been randomly selected to participate in survey on Group Identity on Twitter. \
Click here to participate:http://smallsocialsystems.com/asaf/AboutUs.php?1_flag=" + username

    elif k == 1:

        message = '@' + username + ", Please consider participating in our short experiment on how people express their identities on \
Twitter:http://smallsocialsystems.com/asaf/AboutUs.php?2_flag=" + username

    else:

        message = '@' + username + ", Please consider participating in our short survey on how people express their identities on \
Twitter: http://smallsocialsystems.com/asaf/AboutUs.php?3_flag=" + username

    
    try:
        result = t.statuses.update(status=message)
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
    f=open("Tweeted.txt", "a")
    f.write(username + "\n")
    f.close
    



        
                        
                    
                
    
    
