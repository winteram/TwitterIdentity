from twitter import *


oauth_token = "563118238-aVS68vGHeiWuoLCHIOudAPa6hmhnwIBsSkUfeBXt"
oauth_secret = "M6h51pETL8CWkowEeyh6cb7gNpNTyBpl7fLJk45J4Y"
CONSUMER_KEY = "PCMmY6ERIWJM9tgjIiQRwA"
CONSUMER_SECRET = "YWeRQPivyjc9ZUSLQbaFj8enJviPZ8cw55mu3qSuJdk"

t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

RPaul = t.statuses.user_timeline(id="RonPaul", count=200)
RPaul2 = t.statuses.user_timeline(id="RonPaul", count=200, max_id=RPaul[len(RPaul)-1]['id'])

# to pull the tweets from the timeline use the index "text"




    


