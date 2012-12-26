#setwd("/Users/winteram/Documents/Research/TwitterIdentity/analysis")

library(RMySQL)
library(ggplot2)
theme_set(theme_bw())

con <- dbConnect(MySQL(),
                 user="smalls7_groupid", password="letspublish",
                 dbname="smalls7_identity", host="smallsocialsystems.com")
on.exit(dbDisconnect(con))

survey_demogs <- dbGetQuery(con, "select Id, gender, yob, country, ethnicity, income, edu, party, nationality from survey")

cat("Percent male: ",100*signif(nrow(subset(survey_demogs, gender=="M"))/nrow(subset(survey_demogs, gender=="M" | gender=="F")),4))
cat("Percent female: ",100*round(nrow(subset(survey_demogs, gender=="F"))/nrow(subset(survey_demogs, gender=="M" | gender=="F")),4))
cat("Percent no gender given: ",100*round(nrow(subset(survey_demogs, gender!="M" & gender!="F"))/nrow(subset(survey_demogs, gender=="M" | gender=="F")),4))

