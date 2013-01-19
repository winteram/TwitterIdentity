#setwd("/Users/winteram/Documents/Research/TwitterIdentity/analysis")

require(lme4)
require(e1071)
require(RWeka)
require(ROCR)
require(rpart)
require(ggplot2)
theme_set(theme_bw())

pols <- read.csv("ML_test.csv")
pols <- subset(pols, select=-X)
pols <- ddply(pols, .(IDs), transform, isrep=(Party=="republican"), 
              isdem=(Party=="democrat"),islib=(Party=="libertarian"),
              isgrn=(Party=="green"),iscon=(Party=="constitution"))


pols.lm <- lm(CompParty~RepScore+DemScore+abs(RepScore-DemScore), pols)
summary(pols.lm)

## Predicting if republican
# Logistic regression
isrep.lm <- glm(isrep~RepScore+DemScore+abs(RepScore-DemScore), subset(pols, !is.na(isrep)), family="binomial")
summary(isrep.lm)
pols$lm.p <- predict(isrep.lm, pols, type="response")
pred <- prediction(pols$lm.p, pols$isrep)
#binary_eval(pols$lm.p, pols$isrep)
#isrep.tab <- table(pred = pols$lm.p>0.5, true = pols$isrep)
#print(isrep.tab)

## Predicting if democrat
# Logistic regression
isdem.lm <- glm(isdem~RepScore+DemScore, subset(pols, !is.na(isdem)), family="binomial")
summary(isdem.lm)
pols$lm.dem.p <- predict(isdem.lm, pols, type="response")

## Predicting if libertarian
# Logistic regression
islib.lm <- glm(islib~RepScore+DemScore, subset(pols, !is.na(isrep)), family="binomial")
summary(islib.lm)
pols$lm.lib.p <- predict(islib.lm, pols, type="response")


perf <- performance(pred,"tpr", "fpr")
print(performance(pred,"auc"))
pdf('isrep_ROC.pdf')
plot(perf, colorize=TRUE)
dev.off()



## SVM (not Weka)
is.rep.df <- subset(pols, !is.na(isrep) & !is.na(CompParty))
index <- 1:nrow(is.rep.df)
trainindex <- sample(index, trunc(length(index)/2))
trainset <- is.rep.df[trainindex, ]
testset <- is.rep.df[-trainindex, ]

pols.svm <- svm(isrep~RepScore+DemScore+CompParty, trainset, type="C-classification", probability=T)

isrep.predict <- predict(pols.svm, testset, decision.values = TRUE, probability = TRUE)
isrep.probs <-  attr(isrep.predict, "probabilities")[,1]
pred <- prediction(isrep.probs,testset[,"isrep"])

perf <- performance(pred,"tpr", "fpr")
print(performance(pred,"auc"))
plot(perf, colorize=TRUE)

### SVM (Weka)
is.rep.smo <- SMO(isrep~RepScore+DemScore, trainset)

is.rep.probs <- predict(pols.smo, testset, type="probability")
is.rep.class <- predict(pols.smo, testset, type="class")
pred <- prediction(win.probs[,2],testset[,"isrep"])
perf <- performance(pred,"tpr", "fpr")
print(performance(pred,"auc"))
plot(perf, colorize=TRUE)

# CART
is.rep.tree <- rpart(isrep~RepScore+DemScore+CompParty,data=pols)
summary(is.rep.tree)
plot(is.rep.tree, uniform=TRUE, main="Classification tree for republican")
text(is.rep.tree, use.n=TRUE, all=TRUE, cex=.8)

