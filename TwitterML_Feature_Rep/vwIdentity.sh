#!/bin/bash
shopt -s expand_aliases

alias vw='/Users/winteram/Documents/Research/Miscellaneous/vowpal_wabbit/vowpalwabbit/vw'
alias perf='/Users/winteram/Documents/Research/Miscellaneous/perf_folder/perf'
# This script runs VW on a training and test set, then puts the predictions together and calculates AUC (using the perf tool)

# First we need to get the training and testing file. 
trainFile=$1
testFile=$2
outputPrefix=$3

modelName=${outputPrefix}.model
echo $trainFile

if [ -e ${trainFile}.cache ]
then
	echo "Deleting old cache file.."
	rm ${trainFile}.cache
fi

vw -d ${trainFile} --loss_function logistic -c -f $modelName --ngram 2 -b 25 --passes 5

if [ $? -ne 0 ]
then
	echo "Failed on training..";
	exit 1;
fi

vw -i $modelName -t $testFile -p $outputPrefix-output.txt

if [ $? -ne 0 ]
then
	echo "Failed on testing.."
	exit 1;
fi

cat ${testFile} | cut -d ' ' -f 1 | sed -e 's/^-1/0/' > $outputPrefix-labels.txt

perf -AUC -ACC -files $outputPrefix-labels.txt $outputPrefix-output.txt

