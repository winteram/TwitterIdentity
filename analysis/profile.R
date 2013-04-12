#setwd("/Users/winteram/Documents/Research/CurrentResearch/TwitterIdentity/analysis")

source("reorder.levels.R")
library(RMySQL)
library(ggplot2)
library(gdata)
theme_set(theme_bw())

m<-dbDriver("MySQL")
con <- dbConnect(m,
                 user="groupid", password="LetsPublish!",
                 dbname="group_identity", host="wmason.mgnt.stevens-tech.edu")

survey <- dbGetQuery(con, "select * from survey")
profile <- dbGetQuery(con, "select * from profile")
outdegrees.crawled <- dbGetQuery(con, "select survey.Id, count(*) from survey join relationship on survey.Id=relationship.TwitterAccountParentId group by survey.Id")
indegrees.crawled <- dbGetQuery(con, "select survey.Id, count(*) from survey join relationship on survey.Id=relationship.TwitterAccountNodeId group by survey.Id")
tweets.crawled <- dbGetQuery(con, "select survey.Id, count(tweet.Id) from survey join tweet on survey.Id=tweet.UserId group by survey.Id")
names(outdegrees.crawled) <- c("Id","out.crawl")
names(indegrees.crawled) <- c("Id","in.crawl")
names(tweets.crawled) <- c("Id","tweets.crawl")

# number of distinct users crawled
num.users <- dbGetQuery(con, "select count(a.Id) from (select TwitterAccountNodeId as Id from relationship UNION DISTINCT select TwitterAccountParentId as Id from relationship) a;")

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

ggplot(profile, aes(x=in.crawl)) + geom_histogram(color="black", fill="white") + scale_x_log10()
ggsave("fig/degree_friends_crawl.png")
ggplot(profile, aes(x=Friends_count)) + geom_histogram(color="black", fill="white") + scale_x_log10()
ggsave("fig/degree_friends.png")
ggplot(profile, aes(x=out.crawl)) + geom_histogram(color="black", fill="white") + scale_x_log10()
ggsave("fig/degree_followers_crawl.png")
ggplot(profile, aes(x=Followers_count)) + geom_histogram(color="black", fill="white") + scale_x_log10()
ggsave("fig/degree_followers.png")
ggplot(profile, aes(x=tweets.crawl)) + geom_histogram(color="black", fill="white") + scale_x_log10()
ggsave("fig/degree_tweets_crawl.png")
ggplot(profile, aes(x=Statuses_count)) + geom_histogram(color="black", fill="white") + scale_x_log10()
ggsave("fig/degree_tweets.png")

ggplot(profile, aes(x=Followers_count,y=out.crawl)) + geom_point()
ggplot(profile, aes(x=Friends_count,y=in.crawl)) + geom_point()
ggplot(profile, aes(x=Statuses_count,y=tweets.crawl)) + geom_point()

# gender
allgender = nrow(subset(survey, gender=="M")) + nrow(subset(survey, gender=="F")) + nrow(subset(survey, gender=="decline"))
paste("Males,",round(nrow(subset(survey, gender=="M"))/allgender,4),"(",nrow(subset(survey, gender=="M")),")")
paste("Females,",round(nrow(subset(survey, gender=="F"))/allgender,4),"(",nrow(subset(survey, gender=="F")),")")
paste("Declined,",round(nrow(subset(survey, gender=="decline"))/allgender,4),"(",nrow(subset(survey, gender=="decline")),")")

# politics
ndem = nrow(subset(survey, party=="democrat"))
nrep = nrow(subset(survey, party=="republican"))
nlib = nrow(subset(survey, party=="libertarian")) 
ngre = nrow(subset(survey, party=="green"))
ncon = nrow(subset(survey, party=="constitution"))
allpol = ndem + nrep + nlib + ngre + ncon
paste("Males,",round(nrow(subset(survey, gender=="M"))/allgender,4),"(",nrow(subset(survey, gender=="M")),")")


# own groups
own.forms <- subset(survey, !is.na(own_form1), select=c("Id","own_form1","own_form2","own_form3","own_form4","own_form5","own_form6"))
write.csv(own.forms, "own_forms.csv")
own1 <- subset(survey, !is.na(own_form1), select=c("Id","own_form1"))
names(own1) <- c("Id","own_form")
own3 <- subset(survey, !is.na(own_form3), select=c("Id","own_form3"))
names(own3) <- c("Id","own_form")
own5 <- subset(survey, !is.na(own_form5), select=c("Id","own_form5"))
names(own5) <- c("Id","own_form")
all.own <- rbind(own1,own3,own5)
rm(own1,own3,own5)

own.names <- as.vector(all.own$own_form)
own.names <- tolower(own.names)
own.names <- sort(own.names)

own.freq <- table(own.names)
own.freq <- sort(own.freq, decreasing = TRUE)
own.freq <- as.data.frame(own.freq)
write.csv(own.freq, "own_freq.csv")

ggplot(subset(own.freq, own.freq>1), aes(x=own.freq)) + geom_histogram(color="black", fill="white")

own.freq <- read.csv("own_freq.csv")
names(own.freq) <- c("own.group","freq")
own.freq.30 <- subset(own.freq, freq>30 & own.group != '')
own.freq.30$own.group <- drop.levels(own.freq.30$own.group)
own.freq.30$own.group.2 <- reorder(own.freq.30$own.group, own.freq.30$freq)
own.freq.30$own.group <- reorder.levels(own.freq.30$own.group, rev(own.freq.30$own.group.2))
ggplot(own.freq.30, aes(x=own.group,y=freq)) + geom_bar() + coord_flip() + labs(y="Frequency",x="Self-nominated Group Identity")
ggsave('own_group_freqs.png',width=6,height=5)
