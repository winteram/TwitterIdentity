library(RMySQL)
m<-dbDriver("MySQL")
con<-dbConnect(m,user='smalls7_groupid',password='letspublish',host='smallsocialsystems.com',dbname='smalls7_identity')
res<-dbSendQuery(con, "select * from survey")


rawdata<-fetch(res, n=-1)

dbClearResult(res)

on.exit(dbDisconnect(con))