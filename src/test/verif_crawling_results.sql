use smalls7_identity;

select tan.Id, fr.Id, count(frTw.Id)
from twitteraccountnode as tan
INNER JOIN relationship as frRel
On frRel.TwitterAccountNodeId = tan.Id
INNER JOIN twitteraccountnode as fr
ON fr.Id = frRel.TwitterAccountParentId
INNER JOIN tweet as frTw
ON frTw.UserId= fr.Id
where tan.Seed = 1
GROUP BY tan.Id, fr.Id;

select tan.Id, fo.Id, count(foTw.Id), count(foRtw.Id)
from twitteraccountnode as tan
INNER JOIN relationship as foRel
On foRel.TwitterAccountParentId = tan.Id
INNER JOIN twitteraccountnode as fo
ON fo.Id = foRel.TwitterAccountNodeId
INNER JOIN tweet as foTw
ON foTw.UserId= fo.Id
INNER JOIN tweet as foRtw
ON foRtw.UserId= fo.Id
where tan.Seed = 1 AND foTw.IsRetweet = 0 AND foRtw.IsRetweet = 1
GROUP BY tan.Id, fo.Id;

-- Number of mentions
select tan.Id, count(m.Id)
from twitteraccountnode as tan
INNER JOIN mention as m
on m.UserId = tan.Id
where tan.Seed = 1
GROUP BY tan.Id;

-- number of friends crawled
select tan.Id, count(frRel.Id)
from twitteraccountnode as tan
INNER JOIN relationship as frRel
On frRel.TwitterAccountNodeId = tan.Id
where tan.Seed = 1
GROUP BY tan.Id;

-- number of followers crawled

