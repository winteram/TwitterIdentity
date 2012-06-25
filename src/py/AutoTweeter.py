# coding: utf-8
"""
AutoTweeter
Authors: Winter Mason
    Asaf Beasley

Requires installing twitter tools: http://mike.verdone.ca/twitter
https://github.com/sixohsix/twitter/blob/master/README

to run: $ python AutoTweeter.py username
OR $ python AutoTweeter.py rate

if username, makes one tweet mentioning username
if rate (integer between 1 - 350), tweets constantly at rate tweets / hour

"""
__author__ = "Winter Mason"
__version__ = "0.1"
__license__ = "public domain"

import sys, re, time, urllib
from twitter import *

#     (function) Pull tweeted names into file and turn into dictionary
def getTweeted():
    
#     Construct tweet & post (with “&flag=username” after URL)
def tweetUser(username):
    #  urllib.quote_plus('string_of_characters_like_these:$#@=?%^Q^$')
    # 'string_of_characters_like_these%3A%24%23%40%3D%3F%25%5EQ%5E%24'
    safe_url = urllib.quote_plus(url)
    #     Check for errors
    #     (function) Append tweeted names to file

def AutoTweet(username):
    #     Authenticate with GroupIdentity credentials
    t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

    # get already tweeted usernames
    already_tweeted = getTweeted()

    if int(username) == username:
        # Every N seconds
        username = pullUsername()
        # Remove already tweeted names from input names 
        if username not in already_tweeted:
            tweetUser(username)
        else:
            # Remove already tweeted names from input names 
            if username not in already_tweeted:
                tweetUser(username)



#     Read input:
#     1. Default value (single twitter handle)
#     2. Command-line input (single twitter handle)
#     3. Pull usernames from API (using rate of mentions parameter)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        username = "winteram"
    else:
        username = sys.argv[1]

    begin_time = time.time()
    AutoTweet(username)
    print "Total time: " + str(time.time() - begin_time)