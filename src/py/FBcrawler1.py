# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pymysql
import facebook
from encrypt import *

# <codecell>

conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='groupid', passwd='letspublish', db='gidb')
cur = conn.cursor()

# <codecell>

query = "SELECT * FROM fbconnectionaccounts c JOIN fb_profile p ON c.Id=p.Id WHERE username='%s'" % encode_salt('winteram')
cur.execute(query)

# <codecell>

res = cur.fetchall()
print res

# <codecell>

userid = decode_salt(res[0][7])
oauth_access_token = decode_salt(res[0][1])

# <codecell>

print oauth_access_token

# <codecell>

graph = facebook.GraphAPI(oauth_access_token)

# <codecell>

profile = graph.get_object(userid)

# <codecell>

print profile

# <codecell>

friends = graph.get_connections(userid, "friends")

# <codecell>

print len(friends['data'])

# <codecell>

likes = graph.get_connections(userid, "likes")

# <codecell>

print likes

# <codecell>


