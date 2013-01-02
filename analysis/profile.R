#setwd("/Users/winteram/Documents/Research/TwitterIdentity/analysis")

source("reorder.levels.R")
library(RMySQL)
library(ggplot2)
theme_set(theme_bw())

m<-dbDriver("MySQL")
con <- dbConnect(m,
                 user="smalls7_groupid", password="letspublish",
                 dbname="smalls7_identity", host="smallsocialsystems.com")

profile <- dbGetQuery(con, "select * from profile")
outdegrees.crawled <- dbGetQuery(con, "select survey.Id, count(tweet.Id) from survey join relationship on survey.Id=relationship.TwitterAccountParentId group by survey.Id")
indegrees.crawled <- dbGetQuery(con, "select survey.Id, count(tweet.Id) from survey join relationship on survey.Id=relationship.TwitterAccountNodeId group by survey.Id")
tweets.crawled <- dbGetQuery(con, "select survey.Id, count(tweet.Id) from survey join tweet on survey.Id=tweet.UserId group by survey.Id")
names(outdegrees.crawled) <- c("Id","out.crawl")
names(indegrees.crawled) <- c("Id","in.crawl")
names(tweets.crawled) <- c("Id","tweets.crawl")

on.exit(dbDisconnect(con))

profile <- merge(profile, outdegrees.crawled, by="Id", all.x=TRUE)
profile <- merge(profile, indegrees.crawled, by="Id", all.x=TRUE)
profile <- merge(profile, tweets.crawled, by="Id", all.x=TRUE)

crawled <- subset(profile, !is.na(tweets.crawl), select=c("Id",
                                                            "Followers_count",
                                                            "out.crawl",
                                                            "Friends_count",
                                                            "in.crawl",
                                                            "Statuses_count",
                                                            "tweets.crawl"))
