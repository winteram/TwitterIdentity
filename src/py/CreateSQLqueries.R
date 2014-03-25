setwd('/Users/winteram/Documents/Research/CurrentResearch/TwitterIdentity/doc')

varnames <- read.csv('varnames.csv', header=T)

paste("SELECT ",paste(varnames[c(1,2:7),1],collapse=", ")," FROM survey;",sep='')
paste("SELECT ",paste(varnames[c(1,8:10),1],collapse=", ")," FROM survey;",sep='')
paste("SELECT ",paste(varnames[c(1,11:24),1],collapse=", ")," FROM survey;",sep='')
paste("SELECT ",paste(varnames[c(1,25:33),1],collapse=", ")," FROM survey;",sep='')
paste("SELECT ",paste(varnames[c(1,34:47),1],collapse=", ")," FROM survey;",sep='')
paste("SELECT ",paste(varnames[c(1,48:66),1],collapse=", ")," FROM survey;",sep='')
paste("SELECT ",paste(varnames[c(1,67:85),1],collapse=", ")," FROM survey;",sep='')
paste("SELECT ",paste(varnames[c(1,86:131),1],collapse=", ")," FROM survey;",sep='')
paste("SELECT ",paste(varnames[c(1,132:141),1],collapse=", ")," FROM survey;",sep='')
paste("SELECT ",paste(varnames[c(1,142:144),1],collapse=", ")," FROM survey;",sep='')
