
graphics.off()          # Clears all graphical displays.
rm(list=ls(all=TRUE))   # Removes all variables from memory!

#We need these packages
require(rjags)
require(runjags)

#fileNameRoot is for generating file names later
fileNameRoot = "BayesCorr"

source("DBDA2E-utilities.R")

#Load in the data
dataMat=read.csv("survey_clean_tw.csv",header=TRUE)
xRaw = cbind(dataMat[,"tot_affect_r"],dataMat[,"tw_vader_neg75_r"])
x = na.omit(xRaw)

#Convert x values to ranks
x[,1] = rank(x[,1])
x[,2] = rank(x[,2])

#check on the correlation of these values as a sanity check (compare with the output of Bayesian analysis)
print(cor(x))

#These are useful values for the prior
x1Mean = mean(x[,1])
x2Mean = mean(x[,2])
x1sd = sd(x[,1])
x2sd = sd(x[,2])


#Write the model
modelstring <- "
  model {
    for(i in 1:n) {
      x[i,1:2] ~ dmnorm(mu[], prec[ , ])
    }

    # Constructing the covariance matrix and the corresponding precision matrix.
    prec[1:2,1:2] <- inverse(cov[,])
    cov[1,1] <- sigma[1] * sigma[1]
    cov[1,2] <- sigma[1] * sigma[2] * rho
    cov[2,1] <- sigma[1] * sigma[2] * rho
    cov[2,2] <- sigma[2] * sigma[2]
    
    # Flat priors on all parameters which could, of course, be made more informative.
    sigma[1] ~ dunif(x1sd/100, x1sd*10) 
    sigma[2] ~ dunif(x2sd/100, x2sd*10)
    rho ~ dunif(-1, 1)
    mu[1] ~ dnorm(x1Mean, 1/(x1sd*10)^2)
    mu[2] ~ dnorm(x2Mean, 1/(x2sd*10)^2)

  }
"
writeLines(modelstring,con="model.txt")

#Data list (x is a two column matrix)
dataList = list(x = x, n = nrow(x), x1Mean = x1Mean, x2Mean = x2Mean, x1sd = x1sd,
                x2sd = x2sd)

# Use classical estimates of the parameters as initial values
# initsList = list(mu = c(x1Mean,x2Mean),
#                   rho = cor(x[, 1], x[, 2]),
#                   sigma = c(x1sd,x2sd))

parameters=c("mu","rho","sigma") #parameters to record
adaptSteps = 500              # Number of steps to "tune" the samplers.
burnInSteps = 500            # Number of steps to "burn-in" the samplers.
nChains = 4                   # Number of chains to run.
numSavedSteps=20000           # Total number of steps in chains to save.
thinSteps=1                 # Number of steps to "thin" (1=keep every step).
nPerChain = ceiling( ( numSavedSteps * thinSteps ) / nChains ) # Steps per chain.

runJagsOut <- run.jags(method = "parallel",
                       model = "model.txt",
                       monitor = parameters,
                       data = dataList,
                       #inits = initsList,
                       n.chains = nChains,
                       adapt = adaptSteps,
                       burnin = burnInSteps,
                       sample = ceiling(numSavedSteps/nChains),
                       thin = thinSteps,
                       summarise = FALSE,
                       plots = FALSE )

codaSamples = as.mcmc.list(runJagsOut)

save( codaSamples , file = paste(fileNameRoot,"Coda.Rdata",sep=""))

mcmcChain = as.matrix(codaSamples)

#Take a look at the parameter of interest, rho
DbdaMcmcDiag(codaSamples, parName="rho") #This is an autocorrelation plot

summarizePost(mcmcChain[,"rho"]) #This is a summary of important junk about the posterior

openGraph()
plotPost(mcmcChain[,"rho"]) #This is a plot of the posterior


