# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import twitter
from encrypt import *

# <codecell>

api = twitter.Api(consumer_secret=CONSUMER_SECRET,consumer_key=CONSUMER_KEY,access_token_key=oauth_token,access_token_secret=oauth_secret)

# <codecell>

user = api.GetUser('135813153')

# <codecell>

print user.screen_name

# <codecell>


