from twitter import *

import re 


oauth_token = "563118238-aVS68vGHeiWuoLCHIOudAPa6hmhnwIBsSkUfeBXt"
oauth_secret = "M6h51pETL8CWkowEeyh6cb7gNpNTyBpl7fLJk45J4Y"
CONSUMER_KEY = "PCMmY6ERIWJM9tgjIiQRwA"
CONSUMER_SECRET = "YWeRQPivyjc9ZUSLQbaFj8enJviPZ8cw55mu3qSuJdk"

t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

RPaul = t.statuses.user_timeline(id="RonPaul", count=200)
RPaul2 = t.statuses.user_timeline(id="RonPaul", count=200, max_id=RPaul[len(RPaul)-1]['id'])

# to pull the tweets from the timeline use the index "text"

LibNames=["RonPaul","LPNational"]
DemNames=["TheDemocrats", "BarackObama"]
RepNames=["MittRomney", "Senate_GOPs"]


FullList=[{'party':'dem', 'names': DemNames}, {'party':'rep', 'names': RepNames}, {'party':'lib', 'names': LibNames}]


for parties in FullList:
    f=open(parties['party'] + '.txt', 'a')

    for names in parties['names']:
        
        tweets1= t.statuses.user_timeline(id = names, count = 200)
        tweets2= t.statuses.user_timeline(id = names, count = 200, max_id = tweets1[len(tweets1)-1]['id'])
        tweets3= t.statuses.user_timeline(id = names, count = 200, max_id = tweets2[len(tweets2)-1]['id'])

    
    tweets4= tweets1 + tweets2 + tweets3
    
    statusesList = []

    for i in range(len(tweets4)):
        statusesList.append(tweets4[i]['text'])
        
    

    x= str(statusesList)

    clean_two = re.sub('[^a-zA-Z #]', '', x) #takes everything but alpha characters and hashtags from the string

    # this leaves u's at the beginning of things, so we need pull these out. 

    clean_two = re.sub('u(?P<beg>[A-Z])', '\g<beg>', clean_two)

    # there are still also n's, those should be removed.

    clean_two = re.sub(' n ', '', clean_two)

    clean_two = re.sub('n(?P<beg>[A-Z])', '\g<beg>', clean_two)

    clean_two = clean_two.lower()


    f.write(clean_two) 

    f.close()














    


