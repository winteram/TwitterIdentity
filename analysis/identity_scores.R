#Script to calculate composite scores and factor scores for idenity. Put them them into a new vector in the data frame, "data", of the survey.

#Note: I should source the file that gets the data frame "data"

source("FirstRMySQL.R")

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
  # on this method for now. Next time...
  
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


