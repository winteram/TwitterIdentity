# Utility programs for use with the book,
#   Kruschke, J. K. (2014). Doing Bayesian Data Analysis: 
#   A Tutorial with R and JAGS, 2nd Edition. Academic Press / Elsevier.
# This file contains several functions that are called by other programs
# or can be called directly by the user. To load all the functions into
# R's working memory, at R's command line type:
# source("DBDA2E-utilities.R")

#------------------------------------------------------------------------------

bookInfo = "Kruschke, J. K. (2014). Doing Bayesian Data Analysis:\nA Tutorial with R and JAGS, 2nd Edition. Academic Press / Elsevier."
bannerBreak = "\n*******************************************************************\n"
cat(paste(bannerBreak,bookInfo,bannerBreak,"\n",sep=""))

# Make some data files for examples...
createDataFiles=FALSE
if ( createDataFiles ) {

  # Function for generating normal data with normal outliers:
  genYwithOut = function( N , pcntOut=15 , sdOut=3.0 ) {
    inl = rnorm( N-ceiling(pcntOut/100*N) )
    out = rnorm(   ceiling(pcntOut/100*N) )
    inl = (inl-mean(inl))/sd(inl)
    out = (out-mean(out))/sd(out) * sdOut
    return(c(inl,out))
  }
  
  # Two-group IQ scores with outliers 
  set.seed(47405)
  y1 = round(pmax(50,genYwithOut(63,20,3.5)*17.5+106))
  y2 = round(pmax(50,genYwithOut(57,20,3.5)*10+100))
  write.csv( file="TwoGroupIQ.csv" , row.names=FALSE ,
             data.frame( Score=c(y1,y2) , 
                         Group=c(rep("Smart Drug",length(y1)),
                                 rep("Placebo",length(y2))) ) )
  
  # One-group log-normal
  set.seed(47405)
  z = rnorm(123)
  logY = (z-mean(z))/sd(z) * 0.5 + 5.5 # logY has mean 5.5 and sd 0.5
  y = round( exp(logY) , 2 )
  write.csv( file="OneGroupLogNormal.csv" , row.names=FALSE ,
             cbind(y) )
  
  # One-group gamma
  desiredMode = 250
  desiredSD = 100
  desiredRate = (desiredMode+sqrt(desiredMode^2+4*desiredSD^2))/(2*desiredSD^2)
  desiredShape = 1+desiredMode*desiredRate
  set.seed(47405)
  y = round( rgamma( 153 , shape=desiredShape , rate=desiredRate ) , 2 )
  write.csv( file="OneGroupGamma.csv" , row.names=FALSE , cbind(y) )
  
} # end if createDataFiles

#------------------------------------------------------------------------------
# Functions for opening and saving graphics that operate the same for 
# Windows and Macintosh and Linux operating systems. At least, that's the hope.

openGraph = function( width=7 , height=7 , mag=1.0 , ... ) {
  if ( .Platform$OS.type != "windows" ) { # Mac OS, Linux
    X11( width=width*mag , height=height*mag , type="cairo" , ... )
  } else { # Windows OS
    windows( width=width*mag , height=height*mag , ... )
  }
}

saveGraph = function( file="saveGraphOutput" , type="pdf" , ... ) {
  if ( .Platform$OS.type != "windows" ) { # Mac OS, Linux
    if ( any( type == c("png","jpeg","jpg","tiff","bmp")) ) {
      sptype = type
      if ( type == "jpg" ) { sptype = "jpeg" }
      savePlot( file=paste(file,".",type,sep="") , type=sptype , ... )     
    }
    if ( type == "pdf" ) {
      dev.copy2pdf(file=paste(file,".",type,sep="") , ... )
    }
    if ( type == "eps" ) {
      dev.copy2eps(file=paste(file,".",type,sep="") , ... )
    }
  } else { # Windows OS
    file=paste(file,".",type,sep="") # force explicit extension
    savePlot( file=file , type=type , ... )
  }
}

#------------------------------------------------------------------------------
# Functions for computing limits of HDI's:

HDIofMCMC = function( sampleVec , credMass=0.95 ) {
  # Computes highest density interval from a sample of representative values,
  #   estimated as shortest credible interval.
  # Arguments:
  #   sampleVec
  #     is a vector of representative values from a probability distribution.
  #   credMass
  #     is a scalar between 0 and 1, indicating the mass within the credible
  #     interval that is to be estimated.
  # Value:
  #   HDIlim is a vector containing the limits of the HDI
  sortedPts = sort( sampleVec )
  ciIdxInc = floor( credMass * length( sortedPts ) )
  nCIs = length( sortedPts ) - ciIdxInc
  ciWidth = rep( 0 , nCIs )
  for ( i in 1:nCIs ) {
    ciWidth[ i ] = sortedPts[ i + ciIdxInc ] - sortedPts[ i ]
  }
  HDImin = sortedPts[ which.min( ciWidth ) ]
  HDImax = sortedPts[ which.min( ciWidth ) + ciIdxInc ]
  HDIlim = c( HDImin , HDImax )
  return( HDIlim )
}

HDIofICDF = function( ICDFname , credMass=0.95 , tol=1e-8 , ... ) {
  # Arguments:
  #   ICDFname is R's name for the inverse cumulative density function
  #     of the distribution.
  #   credMass is the desired mass of the HDI region.
  #   tol is passed to R's optimize function.
  # Return value:
  #   Highest density iterval (HDI) limits in a vector.
  # Example of use: For determining HDI of a beta(30,12) distribution, type
  #   HDIofICDF( qbeta , shape1 = 30 , shape2 = 12 )
  #   Notice that the parameters of the ICDFname must be explicitly named;
  #   e.g., HDIofICDF( qbeta , 30 , 12 ) does not work.
  # Adapted and corrected from Greg Snow's TeachingDemos package.
  incredMass =  1.0 - credMass
  intervalWidth = function( lowTailPr , ICDFname , credMass , ... ) {
    ICDFname( credMass + lowTailPr , ... ) - ICDFname( lowTailPr , ... )
  }
  optInfo = optimize( intervalWidth , c( 0 , incredMass ) , ICDFname=ICDFname ,
                      credMass=credMass , tol=tol , ... )
  HDIlowTailPr = optInfo$minimum
  return( c( ICDFname( HDIlowTailPr , ... ) ,
             ICDFname( credMass + HDIlowTailPr , ... ) ) )
}

HDIofGrid = function( probMassVec , credMass=0.95 ) {
  # Arguments:
  #   probMassVec is a vector of probability masses at each grid point.
  #   credMass is the desired mass of the HDI region.
  # Return value:
  #   A list with components:
  #   indices is a vector of indices that are in the HDI
  #   mass is the total mass of the included indices
  #   height is the smallest component probability mass in the HDI
  # Example of use: For determining HDI of a beta(30,12) distribution
  #   approximated on a grid:
  #   > probDensityVec = dbeta( seq(0,1,length=201) , 30 , 12 )
  #   > probMassVec = probDensityVec / sum( probDensityVec )
  #   > HDIinfo = HDIofGrid( probMassVec )
  #   > show( HDIinfo )
  sortedProbMass = sort( probMassVec , decreasing=T )
  HDIheightIdx = min( which( cumsum( sortedProbMass ) >= credMass ) )
  HDIheight = sortedProbMass[ HDIheightIdx ]
  HDImass = sum( probMassVec[ probMassVec >= HDIheight ] )
  return( list( indices = which( probMassVec >= HDIheight ) ,
                mass = HDImass , height = HDIheight ) )
}

#------------------------------------------------------------------------------
# Function(s) for plotting properties of mcmc coda objects.

DbdaAcfPlot = function( codaObject , parName=varnames(codaObject)[1] ) {
  if ( all( parName != varnames(codaObject) ) ) { 
    stop("parName must be a column name of coda object")
  }
  nChain = length(codaObject)
  xMat = NULL
  yMat = NULL
  for ( cIdx in 1:nChain ) {
    acfInfo = acf(codaObject[,c(parName)][[cIdx]],plot=FALSE) 
    xMat = cbind(xMat,acfInfo$lag)
    yMat = cbind(yMat,acfInfo$acf)
  }
  matplot( xMat , yMat , type="o" , pch=20 , col=1:nChain , 
           main=parName , xlab="Lag" , ylab="Autocorrelation" )
  abline(h=0,lty="dashed")
  EffChnLngth = effectiveSize(codaObject[,c(parName)])
  text( x=max(xMat) , y=max(yMat) , adj=c(1.0,1.0) , cex=1.5 ,
        labels=paste("Eff. Ttl. Chn. Lng. \n=",round(EffChnLngth,1)) )
}

DbdaDensPlot = function( codaObject , parName=varnames(codaObject)[1] ) {
  if ( all( parName != varnames(codaObject) ) ) { 
    stop("parName must be a column name of coda object")
  }
  nChain = length(codaObject)
  xMat = NULL
  yMat = NULL
  hdiLims = NULL
  for ( cIdx in 1:nChain ) {
    densInfo = density(codaObject[,c(parName)][[cIdx]]) 
    xMat = cbind(xMat,densInfo$x)
    yMat = cbind(yMat,densInfo$y)
    hdiLims = cbind(hdiLims,HDIofMCMC(codaObject[,c(parName)][[cIdx]]))
  }
  matplot( xMat , yMat , type="l" , col=1:nChain , 
           main=parName , xlab="Param. Value" , ylab="Density" )
  abline(h=0)
  points( hdiLims[1,] , rep(0,nChain) , col=1:nChain , pch="|" )
  points( hdiLims[2,] , rep(0,nChain) , col=1:nChain , pch="|" )
  text( mean(hdiLims) , 0 , "95% HDI" , adj=c(0.5,-0.2) )
  #EffChnLngth = effectiveSize(codaObject[,c(parName)])
  #text( max(xMat) , max(yMat) , adj=c(1.0,1.0) ,
  #      paste("Eff. Ttl. Chn. Lng. =",round(EffChnLngth,1)) )
}

DbdaMcmcDiag = function( codaObject , parName=varnames(codaObject)[1] ,
                         saveName=NULL , saveType="jpg" ) {
  openGraph(height=5,width=7)
  layout(matrix(1:4,nrow=2))
  par( mar=c(3.5,3.5,2.5,1.5) , mgp=c(2.25,0.7,0) , cex.lab=1.5 )
  # traceplot and gelman.plot are from CODA package:
  traceplot(codaObject[,c(parName)],main=parName,ylab="Param. Value") 
  gelman.plot(codaObject[,c(parName)],main=parName,auto.layout=FALSE)
  DbdaAcfPlot(codaObject,parName)
  DbdaDensPlot(codaObject,parName)
  if ( !is.null(saveName) ) {
    saveGraph( file=paste(saveName,"Diag",parName,sep=""), type=saveType)
  }
}

#------------------------------------------------------------------------------
# Functions for summarizing and plotting distribution of a large sample; 
# typically applied to MCMC posterior.

normalize = function( v ){ return( v / sum(v) ) }

summarizePost = function( paramSampleVec , 
                          compVal=NULL , ROPE=NULL , credMass=0.95 ) {
  meanParam = mean( paramSampleVec )
  medianParam = median( paramSampleVec )
  dres = density( paramSampleVec )
  modeParam = dres$x[which.max(dres$y)]
  hdiLim = HDIofMCMC( paramSampleVec , credMass=credMass )
  if ( !is.null(compVal) ) {
    pcgtCompVal = ( 100 * sum( paramSampleVec > compVal ) 
                    / length( paramSampleVec ) )
  } else {
    compVal=NA
    pcgtCompVal=NA
  }
  if ( !is.null(ROPE) ) {
    pcltRope = ( 100 * sum( paramSampleVec < ROPE[1] ) 
                 / length( paramSampleVec ) )
    pcgtRope = ( 100 * sum( paramSampleVec > ROPE[2] ) 
                 / length( paramSampleVec ) )
    pcinRope = 100-(pcltRope+pcgtRope)
  } else { 
    ROPE = c(NA,NA)
    pcltRope=NA 
    pcgtRope=NA 
    pcinRope=NA 
  }  
  return( c( Mean=meanParam , Median=medianParam , Mode=modeParam , 
             HDImass=credMass , HDIlow=hdiLim[1] , HDIhigh=hdiLim[2] , 
             CompVal=compVal , PcntGtCompVal=pcgtCompVal , 
             ROPElow=ROPE[1] , ROPEhigh=ROPE[2] ,
             PcntLtROPE=pcltRope , PcntInROPE=pcinRope , PcntGtROPE=pcgtRope ) )
}

plotPost = function( paramSampleVec , credMass=0.95 , compVal=NULL ,
                     HDItextPlace=0.7 , ROPE=NULL , yaxt=NULL , ylab=NULL ,
                     xlab=NULL , cex.lab=NULL , cex=NULL , xlim=NULL , main=NULL ,
                     col=NULL , border=NULL , showMode=F , showCurve=F , breaks=NULL , 
                     ... ) {
  # Override defaults of hist function, if not specified by user:
  # (additional arguments "..." are passed to the hist function)
  if ( is.null(xlab) ) xlab="Spearman's rho"
  if ( is.null(cex.lab) ) cex.lab=1.5
  if ( is.null(cex) ) cex=1.4
  if ( is.null(xlim) ) xlim=range( c( compVal , paramSampleVec ) )
  if ( is.null(main) ) main="Correlation of Vader Composite FB and PANAS (full sample)"
  if ( is.null(yaxt) ) yaxt="n"
  if ( is.null(ylab) ) ylab=""
  if ( is.null(col) ) col="skyblue"
  if ( is.null(border) ) border="white"
  
  postSummary = matrix( NA , nrow=1 , ncol=11 , 
                        dimnames=list( c( xlab ) , 
                                       c("mean","median","mode",
                                         "hdiMass","hdiLow","hdiHigh",
                                         "compVal","pcGTcompVal",
                                         "ROPElow","ROPEhigh","pcInROPE")))              
  postSummary[,"mean"] = mean(paramSampleVec)
  postSummary[,"median"] = median(paramSampleVec)
  mcmcDensity = density(paramSampleVec)
  postSummary[,"mode"] = mcmcDensity$x[which.max(mcmcDensity$y)]
  
  HDI = HDIofMCMC( paramSampleVec , credMass )
  postSummary[,"hdiMass"]=credMass
  postSummary[,"hdiLow"]=HDI[1]
  postSummary[,"hdiHigh"]=HDI[2]
  
  # Plot histogram.
  if ( is.null(breaks) ) {
    breaks = c( seq( from=min(paramSampleVec) , to=max(paramSampleVec) ,
                     by=(HDI[2]-HDI[1])/18 ) , max(paramSampleVec) )
  }
  if ( !showCurve ) {
    par(xpd=NA)
    histinfo = hist( paramSampleVec , xlab=xlab , yaxt=yaxt , ylab=ylab ,
                     freq=F , border=border , col=col ,
                     xlim=xlim , main=main , cex=cex , cex.lab=cex.lab ,
                     breaks=breaks , ... )
  }
  if ( showCurve ) {
    par(xpd=NA)
    histinfo = hist( paramSampleVec , plot=F )
    densCurve = density( paramSampleVec , adjust=2 )
    plot( densCurve$x , densCurve$y , type="l" , lwd=5 , col=col , bty="n" ,
          xlim=xlim , xlab=xlab , yaxt=yaxt , ylab=ylab ,
          main=main , cex=cex , cex.lab=cex.lab , ... )
  }
  cenTendHt = 0.9*max(histinfo$density)
  cvHt = 0.7*max(histinfo$density)
  ROPEtextHt = 0.55*max(histinfo$density)
  # Display mean or mode:
  if ( showMode==F ) {
    meanParam = mean( paramSampleVec )
    text( meanParam , cenTendHt ,
          bquote(mean==.(signif(meanParam,3))) , adj=c(.5,0) , cex=cex )
  } else {
    dres = density( paramSampleVec )
    modeParam = dres$x[which.max(dres$y)]
    text( modeParam , cenTendHt ,
          bquote(mode==.(signif(modeParam,3))) , adj=c(.5,0) , cex=cex )
  }
  # Display the comparison value.
  if ( !is.null( compVal ) ) {
    cvCol = "darkgreen"
    pcgtCompVal = round( 100 * sum( paramSampleVec > compVal )
                         / length( paramSampleVec )  , 1 )
    pcltCompVal = 100 - pcgtCompVal
    lines( c(compVal,compVal) , c(0.96*cvHt,0) ,
           lty="dotted" , lwd=1 , col=cvCol )
    text( compVal , cvHt ,
          bquote( .(pcltCompVal)*"% < " *
            .(signif(compVal,3)) * " < "*.(pcgtCompVal)*"%" ) ,
          adj=c(pcltCompVal/100,0) , cex=0.8*cex , col=cvCol )
    postSummary[,"compVal"] = compVal
    postSummary[,"pcGTcompVal"] = ( sum( paramSampleVec > compVal ) 
                                    / length( paramSampleVec ) )
  }
  # Display the ROPE.
  if ( !is.null( ROPE ) ) {
    ropeCol = "darkred"
    pcInROPE = ( sum( paramSampleVec > ROPE[1] & paramSampleVec < ROPE[2] )
                 / length( paramSampleVec ) )
    lines( c(ROPE[1],ROPE[1]) , c(0.96*ROPEtextHt,0) , lty="dotted" , lwd=2 ,
           col=ropeCol )
    lines( c(ROPE[2],ROPE[2]) , c(0.96*ROPEtextHt,0) , lty="dotted" , lwd=2 ,
           col=ropeCol)
    text( mean(ROPE) , ROPEtextHt ,
          bquote( .(round(100*pcInROPE))*"% in ROPE" ) ,
          adj=c(.5,0) , cex=1 , col=ropeCol )
    
    postSummary[,"ROPElow"]=ROPE[1] 
    postSummary[,"ROPEhigh"]=ROPE[2] 
    postSummary[,"pcInROPE"]=pcInROPE
  }
  # Display the HDI.
  lines( HDI , c(0,0) , lwd=4 )
  text( mean(HDI) , 0 , bquote(.(100*credMass) * "% HDI" ) ,
        adj=c(.5,-1.7) , cex=cex )
  text( HDI[1] , 0 , bquote(.(signif(HDI[1],3))) ,
        adj=c(HDItextPlace,-0.5) , cex=cex )
  text( HDI[2] , 0 , bquote(.(signif(HDI[2],3))) ,
        adj=c(1.0-HDItextPlace,-0.5) , cex=cex )
  par(xpd=F)
  #
  return( postSummary )
}

#------------------------------------------------------------------------------


