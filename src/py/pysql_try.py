
import pymysql



conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='smalls7_groupid', passwd='letspublish', db='smalls7_identity')

cur = conn.cursor()

cur.execute("Use smalls7_identity")
cur.execute("SHOW TABLES")


r = cur.fetchall()

cur.execute("SELECT COUNT(Id) FROM survey WHERE Date(ended) = Date(NOW())")

num_today = cur.fetchall()

cur.execute("SELECT Id, comments FROM survey WHERE Date(ended) = Date(NOW())")

comments_today = cur.fetchall()

cur.execute("SELECT SUM(username REGEXP '_1$') AS message1, SUM(username REGEXP '_2$') AS message2, SUM(username REGEXP '_3$') AS message3 FROM (SELECT DISTINCT(username) FROM visitors) v")
something = cur.fetchall()

cur.execute("SELECT * FROM survey")

surveycont = cur.fetchall()

cur.execute("SELECT Id FROM survey")

ids = cur.fetchall()



















    

  

 
