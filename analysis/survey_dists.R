#setwd("/Users/winteram/Documents/Research/TwitterIdentity/analysis")

source("reorder.levels.R")
library(RMySQL)
library(ggplot2)
theme_set(theme_bw())

con <- dbConnect(MySQL(),
                 user="smalls7_groupid", password="letspublish",
                 dbname="smalls7_identity", host="smallsocialsystems.com")
on.exit(dbDisconnect(con))

demogs <- dbGetQuery(con, "select Id, gender, yob, country, ethnicity, income, edu, party, nationality from survey")

# Percent male and female respondents
cat("Percent male: ",100*round(nrow(subset(demogs, gender=="M"))/nrow(subset(demogs, gender=="M" | gender=="F")),4))
cat("Percent female: ",100*round(nrow(subset(demogs, gender=="F"))/nrow(subset(demogs, gender=="M" | gender=="F")),4))
cat("Percent no gender given: ",100*round(nrow(subset(demogs, gender!="M" & gender!="F"))/nrow(subset(demogs, gender=="M" | gender=="F")),4))

# Age distribution
age <- subset(demogs, !is.na(yob) & yob != "0000", select="yob")
age <- transform(age, yob=2012-as.integer(yob))
ggplot(age, aes(x=yob,y=..density..)) + 
  geom_histogram(binwidth=1,color="gray60",fill="white") + 
  geom_density() + 
  labs(x="Age",y="Density") +
  opts(axis.title.x=theme_text(vjust=-0.2,size=14),axis.title.y=theme_text(vjust=0.2,angle=90,size=14))
ggsave("../fig/survey_age.pdf",width=5,height=5)

# education distribution
education <- subset(demogs, !is.na(edu) & edu!="", select=edu)
education$edu <- as.factor(education$edu)
education$edu <- reorder.levels(education$edu, c("none","hs","hsgrad","college","as","bs","ms","phd","md"))
ggplot(education, aes(x=edu)) + 
  geom_bar(fill="gray60") + 
  labs(x="Education",y="Count") + 
  coord_flip() +
  opts(axis.title.x=theme_text(vjust=-0.2,size=14),axis.title.y=theme_text(vjust=0.2,angle=90,size=14))
ggsave("../fig/survey_edu.pdf",width=5,height=5)

# Country distribution
country <- within(demogs, country <- factor(country, levels=names(sort(table(country)))))
ggplot(country, aes(x=country)) + 
  geom_bar(fill="white",color="gray20") + 
  labs(x="Country",y="Count") + 
  coord_flip() +
  opts(axis.title.x=theme_text(vjust=-0.2,size=14),axis.title.y=theme_text(vjust=0.2,angle=90,size=14))
ggsave("../fig/survey_country.pdf",width=5,height=5)

# Nationality distribution
nation <- subset(demogs, !is.na(nationality),select="nationality")
nationality <- list()
for(i in 1:nrow(nation))
{
  nationality <- c(nationality, strsplit(nation[i,"nationality"],"-"))
}
nationality <- unlist(nationality)
nationality <- lapply(nationality, function(s) gsub("(^ +)|( +$)|[^A-Za-z]", "", s))
nationality <- unlist(nationality)
nation <- as.data.frame(nationality)
nation <- within(nation, nationality <- factor(nationality, levels=names(sort(table(nationality)))))
ggplot(nation, aes(x=nationality)) + 
  geom_bar(fill="white",color="gray20") + 
  labs(x="Nationality",y="Count") + 
  coord_flip() +
  opts(axis.title.x=theme_text(vjust=-0.2,size=14),axis.title.y=theme_text(vjust=0.2,angle=90,size=14))
ggsave("../fig/survey_nation.pdf",width=5,height=10)

# party distribution
party <- subset(demogs, !is.na(party) & party!="", select=party)
party$party <- as.factor(party$party)
party$party <- reorder.levels(party$party, c("constitution","green","libertarian","republican","democrat"))
ggplot(party, aes(x=party,fill=party)) + 
  scale_fill_manual(values=c("purple","green","orange","red","blue")) +
  geom_bar() +
  labs(x="Party",y="Count") + 
  coord_flip() +
  opts(axis.title.x=theme_text(vjust=-0.2,size=14),axis.title.y=theme_text(vjust=0.2,angle=90,size=14))
ggsave("../fig/survey_party.pdf",width=5,height=5)

