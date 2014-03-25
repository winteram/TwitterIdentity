setwd('/Users/winteram/Documents/Research/CurrentResearch/TwitterIdentity/doc')

varnames <- read.csv('varnames.csv', header=T)

paste("SELECT ",paste(varnames[c(1,2:6),1],collapse=", ")," FROM survey;",sep='')
paste("SELECT ",paste(varnames[c(1,7:9),1],collapse=", ")," FROM survey;",sep='')
paste("SELECT ",paste(varnames[c(1,10:23),1],collapse=", ")," FROM survey;",sep='')
paste("SELECT ",paste(varnames[c(1,24:32),1],collapse=", ")," FROM survey;",sep='')
paste("SELECT ",paste(varnames[c(1,33:51),1],collapse=", ")," FROM survey;",sep='')
paste("SELECT ",paste(varnames[c(1,52:70),1],collapse=", ")," FROM survey;",sep='')
paste("SELECT ",paste(varnames[c(1,71:105),1],collapse=", ")," FROM survey;",sep='')
paste("SELECT ",paste(varnames[c(1,106:126),1],collapse=", ")," FROM survey;",sep='')
paste("SELECT ",paste(varnames[c(1,127:129),1],collapse=", ")," FROM survey;",sep='')
