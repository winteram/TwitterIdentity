setwd("/Users/winteram/Documents/Research/TwitterIdentity/src/py")

require(ggplot2)
theme_set(theme_bw())


partyscores <- read.delim('partydist.txt',sep=' ',header=F,stringsAsFactors=T)
names(partyscores) <- c("Id","party","scoreDem","scoreRep","scoreLP")

partynonzero <- subset(partyscores, scoreDem + scoreRep + scoreLP > 0)
partymeans <- ddply(partynonzero, .(party), summarize, Demavg=mean(scoreDem), Repavg=mean(scoreRep), LPavg=mean(scoreLP))
