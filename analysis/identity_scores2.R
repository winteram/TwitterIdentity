# Script to calculate composite scores and factor scores for identity. 
# Put them them into a new vector in the data frame, "data", of the survey.
source("FirstRMySQL.R")
library(ggplot2)
library(psych) # This requires the psych package
theme_set(theme_bw())


data <- ddply(rawdata, .(Id), transform,
              solidarityPol = sum(party1_bond,
                                  party2_solidarity,
                                  party3_committed),
              satisfactionPol = sum(party4_glad,
                                    party5_proud,
                                    party6_pleasant,
                                    party7_goodfeel),
              centralityPol = sum(party8_think,
                                  party9_identity,
                                  party10_seemyself),
              selfstereotypePol = sum(party11_common_avg,
                                      party12_similar_avg),
              homogeneityPol = sum(party13_common_oth,
                                   party14_similar_oth),
              solidarityNat = sum(nation1_bond,
                                  nation2_solidarity,
                                  nation3_committed),
              satisfactionNat = sum(nation4_glad,
                                    nation5_proud,
                                    nation6_pleasant,
                                    nation7_goodfeel),
              centralityNat = sum(nation8_think,
                                  nation9_identity,
                                  nation10_seemyself),
              selfstereotypeNat = sum(nation11_common_avg,
                                      nation12_similar_avg),
              homogeneityNat = sum(nation13_common_oth,
                                   nation14_similar_oth)
)

data <- ddply(data, .(Id), transform, compPol=sum(solidarityPol,
                                                  satisfactionPol,
                                                  centralityPol,
                                                  selfstereotypePol,
                                                  homogeneityPol),
              compNat = sum(solidarityNat,
                            satisfactionNat,
                            centralityNat,
                            selfstereotypeNat,
                            homogeneityNat))

data <- ddply(data, .(Id), transform, sdNat = sd(c(nation1_bond,
                                                 nation2_solidarity,
                                                 nation3_committed,
                                                 nation4_glad,
                                                 nation5_proud,
                                                 nation6_pleasant,
                                                 nation7_goodfeel,
                                                 nation8_think,
                                                 nation9_identity,
                                                 nation10_seemyself,
                                                 nation11_common_avg,
                                                 nation12_similar_avg,
                                                 nation13_common_oth,
                                                 nation14_similar_oth)),
              sdPol = sd(c(party1_bond,
                           party2_solidarity,
                           party3_committed,
                           party4_glad,
                           party5_proud,
                           party6_pleasant,
                           party7_goodfeel,
                           party8_think,
                           party9_identity,
                           party10_seemyself,
                           party11_common_avg,
                           party12_similar_avg,
                           party13_common_oth,
                           party14_similar_oth)))

#show distribution of select scores. 


#Fancier-using ggplot, graphs stored to file called "fig"

# National Idenity Composite score distribution

ggplot(data, aes(x=data$compNat,y=..density..)) + 
  geom_histogram(binwidth=1,color="gray60",fill="white") + 
  geom_density() + 
  labs(x="Composite National Identity",y="Density") +
  opts(axis.title.x=theme_text(vjust=-0.2,size=14),axis.title.y=theme_text(vjust=0.2,angle=90,size=14))
ggsave("fig/Composite_Nationality.pdf",width=5,height=5)

# Political Identity Composite Score distribution

ggplot(data, aes(x=data$compPol,y=..density..)) + 
  geom_histogram(binwidth=1,color="gray60",fill="white") + 
  geom_density() + 
  labs(x="Composite Political Identity",y="Density") +
  opts(axis.title.x=theme_text(vjust=-0.2,size=14),axis.title.y=theme_text(vjust=0.2,angle=90,size=14))
ggsave("fig/Composite_Political_Id.pdf",width=5,height=5)

# Political Solidarity Factor Distribution

ggplot(data, aes(x=data$solidarityPol,y=..density..)) + 
  geom_histogram(binwidth=1,color="gray60",fill="white") + 
  geom_density() + 
  labs(x="Solidarity with Party",y="Density") +
  opts(axis.title.x=theme_text(vjust=-0.2,size=14),axis.title.y=theme_text(vjust=0.2,angle=90,size=14))
ggsave("fig/Solidarity_Political_Id.pdf",width=5,height=5)

# Satisfaction factor for politics

ggplot(data, aes(x=data$satisfactionPol,y=..density..)) + 
  geom_histogram(binwidth=1,color="gray60",fill="white") + 
  geom_density() + 
  labs(x="Satisfaction with Political ID",y="Density") +
  opts(axis.title.x=theme_text(vjust=-0.2,size=14),axis.title.y=theme_text(vjust=0.2,angle=90,size=14))
ggsave("fig/Satisfaction_Political_Id.pdf",width=5,height=5)

# Centrality Factor for Politics

ggplot(data, aes(x=data$centralityPol,y=..density..)) + 
  geom_histogram(binwidth=1,color="gray60",fill="white") + 
  geom_density() + 
  labs(x="Centrality of Political ID",y="Density") +
  opts(axis.title.x=theme_text(vjust=-0.2,size=14),axis.title.y=theme_text(vjust=0.2,angle=90,size=14))
ggsave("fig/Centrality_Political_Id.pdf",width=5,height=5)

# Self Stereotyping for Politics

ggplot(data, aes(x=data$selfstereotypePol,y=..density..)) + 
  geom_histogram(binwidth=1,color="gray60",fill="white") + 
  geom_density() + 
  labs(x="Self-Stereotyping of Party",y="Density") +
  opts(axis.title.x=theme_text(vjust=-0.2,size=14),axis.title.y=theme_text(vjust=0.2,angle=90,size=14))
ggsave("fig/Self-Stereotyp_Political_Id.pdf",width=5,height=5)

# ingroup homogeneity for politics

ggplot(data, aes(x=data$homogeneityPol,y=..density..)) + 
  geom_histogram(binwidth=1,color="gray60",fill="white") + 
  geom_density() + 
  labs(x="Perceived Homogeneity of Party",y="Density") +
  opts(axis.title.x=theme_text(vjust=-0.2,size=14),axis.title.y=theme_text(vjust=0.2,angle=90,size=14))
ggsave("fig/Homogeneity_Political_Id.pdf",width=5,height=5)


# Subsetting to get a more fine-grained view of things:

RepubNatId<-subset(data, !is.na(compNat) & party=="republican")

ggplot(RepubNatId, aes(x=RepubNatId$compNat,y=..density..)) + 
  geom_histogram(binwidth=1,color="gray60",fill="white") + 
  geom_density() + 
  labs(x="National Identity for Republicans",y="Density") +
  opts(axis.title.x=theme_text(vjust=-0.2,size=14),axis.title.y=theme_text(vjust=0.2,angle=90,size=14))
ggsave("fig/Republican_National_Id.pdf",width=5,height=5)

#Graph for Democrat National Identity
DemNatId<-subset(data, !is.na(compNat) & party=="democrat")

ggplot(DemNatId, aes(x=DemNatId$compNat,y=..density..)) + 
  geom_histogram(binwidth=1,color="gray60",fill="white") + 
  geom_density() + 
  labs(x="National Identity for Democrats",y="Density") +
  opts(axis.title.x=theme_text(vjust=-0.2,size=14),axis.title.y=theme_text(vjust=0.2,angle=90,size=14))
ggsave("fig/Democrat_National_Id.pdf",width=5,height=5)

#Distribution for Indian National Identity

IndianNatId<-subset(data, !is.na(compNat) & nationality=="Indian",select="compNat")

ggplot(IndianNatId, aes(x=IndianNatId$compNat,y=..density..)) + 
  geom_histogram(binwidth=1,color="gray60",fill="white") + 
  geom_density() + 
  labs(x="National Identity for Indians",y="Density") +
  opts(axis.title.x=theme_text(vjust=-0.2,size=14),axis.title.y=theme_text(vjust=0.2,angle=90,size=14))
ggsave("fig/Indian_National_Id.pdf",width=5,height=5)

#Distribution for American National Identity

AmericanNatId<-subset(data, !is.na(compNat) & nationality=="American",select="compNat")

ggplot(AmericanNatId, aes(x=AmericanNatId$compNat,y=..density..)) + 
  geom_histogram(binwidth=1,color="gray60",fill="white") + 
  geom_density() + 
  labs(x="National Identity for Americans",y="Density") +
  opts(axis.title.x=theme_text(vjust=-0.2,size=14),axis.title.y=theme_text(vjust=0.2,angle=90,size=14))
ggsave("fig/American_National_Id.pdf",width=5,height=5)


#Some quick histograms for distributions of national identity factors- not saved in the fig file, but just in some console windows.

hist(data$solidarityNat)
hist(data$satisfactionNat)
hist(data$homogeneityNat)
hist(data$selfstereotypeNat)
hist(data$centralityNat)

#Histograms for National identity for Democrats

hist(DemNatId$solidarityNat)
hist(DemNatId$satisfactionNat)
hist(DemNatId$homogeneityNat)
hist(DemNatId$selfstereotypeNat)
hist(DemNatId$centralityNat)

#Histograms for National Identity for Republicans

hist(RepubNatId$solidarityNat)
hist(RepubNatId$satisfactionNat)
hist(RepubNatId$homogeneityNat)
hist(RepubNatId$selfstereotypeNat)
hist(RepubNatId$centralityNat)

cat(paste("Skewness for the composite political identity distribution is",skew(data$compPol, na.rm=TRUE),"\n"))
cat(paste("kurtosis for the the composite political identity distribution is", kurtosi(data$compPol, na.rm=TRUE),"\n"))
cat("These scores are in range of normality")

cat("There appear to be significant differences in National identity among Democrats and Republican. Here is the output from a T-test :")
print(t.test(DemNatId$compNat,RepubNatId$compNat))
cat("There also appear to be differences among Indian's National Identity and Americans. Here is the T-test: ")
print(t.test(AmericanNatId,IndianNatId))


