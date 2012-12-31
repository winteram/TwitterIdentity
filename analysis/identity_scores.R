#Script to calculate composite scores and factor scores for idenity. Put them them into a new vector in the data frame, "data", of the survey.

#Note: I should source the file that gets the data frame "data"

source("FirstRMySQL.R")
library(ggplot2)
library(psych) # This requires the psych package
data$compNat=rep(NA,nrow(data)) # Vector for composite score for Nationality questions
data$compPol=rep(NA,nrow(data))# Composite score for politics

#Scores for Political Identity factors

data$solidarityPol=rep(NA,nrow(data)) 
data$satisfactionPol=rep(NA,nrow(data))
data$centralityPol=rep(NA,nrow(data))
data$selfstereotypePol=rep(NA,nrow(data))
data$homogeneityPol=rep(NA,nrow(data))

#Scores for National Idenity factors
data$solidarityNat=rep(NA,nrow(data)) 
data$satisfactionNat=rep(NA,nrow(data))
data$centralityNat=rep(NA,nrow(data))
data$selfstereotypeNat=rep(NA,nrow(data))
data$homogeneityNat=rep(NA,nrow(data))




attach(data)

for(i in 1:nrow(data))
{ 
  #simply making a vector with all the score for a given participant
  
  tempPol=c(party1_bond[i],party2_solidarity[i],party3_committed[i],party4_glad[i],party5_proud[i],party6_pleasant[i],party7_goodfeel[i],party8_think[i],party9_identity[i],party10_seemyself[i],party11_common_avg[i],party12_similar_avg[i],party13_common_oth[i],party14_similar_oth[i])
  
  tempNat=c(nation1_bond[i],nation2_solidarity[i],nation3_committed[i],nation4_glad[i],nation5_proud[i],nation6_pleasant[i],nation7_goodfeel[i],nation8_think[i], nation9_identity[i],nation10_seemyself[i],nation11_common_avg[i],nation12_similar_avg[i],nation13_common_oth[i],nation14_similar_oth[i])
  
  #Note: I could have just indexed tempNat- for these. 
  tempPolsolid=tempPol[1:3]
  tempPolsatis=tempPol[4:7]
  tempPolcentral=tempPol[8:10]
  tempPolself=tempPol[11:12]
  tempPolhomo=tempPol[13:14]
  
  tempNatsolid=tempNat[1:3]
  tempNatsatis=tempNat[4:7]
  tempNatcentral=tempNat[8:10]
  tempNatself=tempNat[11:12]
  tempNathomo=tempNat[13:14]
  
  
  
  #If there are missing values the composite score is rather misleading, so I will just keep the score as NA (initially assigned) for these instances. 
  if(!(NA %in% tempPol))
  {
    data$compPol[i]=sum(tempPol)
  }
  
  if(!(NA %in% tempNat))
  {
    data$compNat[i]=sum(tempNat)
  }
  # Note, there is a way more efficient way to do this where I could have assigned variables through a loop and computed them- 
  # Or had the variables pre-assigned in sets which I could loop through in parallel. but I'm just settling
  # on this method for now. Next time..
  
  if(!(NA %in% tempPolsolid))
  {
    data$solidarityPol[i]=sum(tempPolsolid)
    
  }
     
  if(!(NA %in% tempPolsatis))
  {
    data$satisfactionPol[i]=sum(tempPolsatis)
       
  }
     
  if(!(NA %in% tempPolcentral))
  {
    data$centralityPol[i]=sum(tempPolcentral)
       
  }
  if(!(NA %in% tempPolself))
  {
    data$selfstereotypePol[i]=sum(tempPolself)
       
  }
     
  if(!(NA %in% tempPolhomo))
  {
    data$homogeneityPol[i]=sum(tempPolhomo)
       
  }
  
  #Now the same for Nationality
  
  if(!(NA %in% tempNatsolid))
  {
    data$solidarityNat[i]=sum(tempNatsolid)
    
  }
  
  if(!(NA %in% tempNatsatis))
  {
    data$satisfactionNat[i]=sum(tempNatsatis)
    
  }
  
  if(!(NA %in% tempNatcentral))
  {
    data$centralityNat[i]=sum(tempNatcentral)
    
  }
  if(!(NA %in% tempNatself))
  {
    data$selfstereotypeNat[i]=sum(tempNatself)
    
  }
  
  if(!(NA %in% tempNathomo))
  {
    data$homogeneityNat[i]=sum(tempNathomo)
    
  }
       
}


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

cat("Skewness for the composite political identity distribution is",skew(data$compPol, na.rm=TRUE))
cat("kurtosis for the the composite political identity distribution is. ", kurtosi(data$compPol, na.rm=TRUE))
cat("These scores are in range of normality")



cat("There appear to be significant differences in National identity among Democrats and Republican. Here is the output from a T-test :")
print(t.test(DemNatId$compNat,RepubNatId$compNat))
cat("There also appear to be differences among Indian's National Identity and Americans. Here is the T-test: ")
print(t.test(AmericanNatId,IndianNatId))


