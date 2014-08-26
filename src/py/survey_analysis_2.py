import sys, os
import numpy as np
import math
from pandas import DataFrame, Series, concat
import pandas as pd
import matplotlib.pyplot as plt

import scipy.stats



os.chdir('C:/Users/Asaf/Documents/GitHub/TwitterIdentity/src/py')


survey=pd.read_pickle('DataFrames/survey')

traits=pd.read_pickle('DataFrames/traits')

aspects=pd.read_pickle('DataFrames/aspects')


#Later recreate histograms
#Need to create new subsets of data-frames to do analysis.

#First do independent and paired sample tests separately.
#Then do two stage analyis for some of the correlations- politics and religion- where you exclude the people who
#said they never express something in social media.
#Also, find function to check for normality of a distribution in python. 





#Subsetting.

#Get a set of all the people for whom there is is both twitter and fb data.Do it separately for each response.

 




#This will give Cohen's d for t-tests (uses pooled standard deviation)

def CohenD(group1, group2):
    diff = np.mean(group1) - np.mean(group2)

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    
    return d
    
#Code for t tests

#add a new field, where you can specificy if you want related samples or independent samples
def t_comparisons(DataFrame, pairs,kind='Independent'):
    for pair in pairs:
        one=DataFrame[pair[0]].dropna()
        two=DataFrame[pair[1]].dropna()
        mean1=np.mean(one)
        mean2=np.mean(two)
        Cohen=CohenD(one,two)
        if kind=='Independent':
            t, p = scipy.stats.ttest_ind(one, two)
        elif kind=='Paired':
            t, p = scipy.stats.ttest_rel(one, two)
        else:
            print 'unrecognized t sample type'     

        
        print "The Mean for %s is %s , and the mean for %s is %s ;The p-value for this comparison is %s ,and the t-value is %s , and Cohen's d = %s" %(pair[0],mean1,pair[1],mean2,p,t,Cohen) 
     

        
pair_list=[('fb_academic','tw_academic'),('fb_appearance','tw_appearance'),('fb_doing','tw_doing'),('fb_entertain','tw_entertain'),('fb_family','tw_family'),('fb_feel','tw_feel'),
            ('fb_god','tw_god'),('fb_political','tw_political'),('fb_where','tw_where')]
            
#Make a dataframe that includes all the people for whom there are both types of data-

#Might have to do this one with a loop, because the dataframe will be different for each pairwise comparison, given that not everyone answered both questions.

#Gives output for paired samples
for i in pair_list:
    dframe=survey[survey[i[0]].notnull() & survey[i[1]].notnull()]
    t_comparisons(dframe,[i],kind="Paired")
    
#Now I want output for non-paired samples

for i in pair_list:
    dframe=survey[survey[i[0]].isnull() | survey[i[1]].isnull()]
    t_comparisons(dframe,[i],kind="Independent")


#Now I want to do the independent and dependent  samples t-tests by category of self-aspect

#Sidenote- I suppose I can also make a graph of these distributions as I had previously


#I am modifying this function so that it can print out results for the between subjects analysis and within subjects.

 
w=Series(aspects['Label'].values.ravel()).unique() 

def Compare_GroupbyCat(Dframe,cat_name, cat_list, GroupNames, kind='Independent'):
    for i in cat_list:
        df_init=Dframe[Dframe[cat_name]==i]
        
        if kind=='Independent':
            df_init=df_init[df_init[GroupNames[0]].isnull() | df_init[GroupNames[1]].isnull()]
        elif kind=='Paired':
            df_init=df_init[df_init[GroupNames[0]].notnull() & df_init[GroupNames[1]].notnull()]
        else:
            print "Kind is not recognized"
        
        
        one=df_init[GroupNames[0]].dropna()
        two=df_init[GroupNames[1]].dropna() 
        mean1=np.mean(one)
        mean2=np.mean(two)
        
        Cohen=CohenD(one,two)
        
        try:
        
            if kind=='Independent':
                t, p = scipy.stats.ttest_ind(one, two)
            else:
                t, p = scipy.stats.ttest_rel(one, two)
                
    
            
            print "For the comparison of the category value %s, the mean for %s is %s , and the mean for %s is %s ;The p-value for this comparison is %s ,and the t-value is %s , and Cohen's d = %s" %(i,GroupNames[0], mean1,GroupNames[1],mean2,p,t,Cohen) 

        except:
            print "Something went wrong for %s"%(i)
    

Compare_GroupbyCat(aspects, 'Label',w,['Twitter','Facebook'])


#Now go back to the correlations, but make the two stage for religion and politics. Remove the people who are not believers and do the analysis.



def p_corr(df1, df2):
    """
    Computes Pearson correlation and its significance (using a t
    distribution) on a pandas.DataFrame.
 
    Ignores null values when computing significance. Based on
    http://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient#Testing_using_Student.27s_t-distribution
 
    Args:
        df1 (pandas.DataFrame): one dataset
        df2 (pandas.DataFrame): another dataset
 
    Returns:
        corr (float): correlation between the two datasets
        t (float): an associated t-value
        p (float): one-tailed p-value that the two datasets differ
    """
    corr = df1.corr(df2)
    N = np.sum(df1.notnull())
    t = corr*np.sqrt((N-2)/(1-corr**2))
    p = 1-scipy.stats.t.cdf(abs(t),N-2)  # one-tailed
    return corr, t, p   



 





 #Note- this relies on p_corr function above.  
  
pair_list_corr= [('fb_academic','academics'),('fb_appearance','appearance'),('fb_family','family_support'),
            ('fb_god','GodLove'),('tw_academic','academics'),('tw_appearance','appearance'),('tw_family','family_support'),
             ('tw_god','GodLove')]

def Pair_Cor(DataFrame,pair_list):
    for pair in pair_list:
        one=DataFrame[pair[0]]
        two=DataFrame[pair[1]]
        stats=p_corr(one,two)
        print 'The correlation between %s and %s is %s , the t statistic is %s and the p-value is %s' %(pair[0], pair[1],stats[0],stats[1],stats[2])


for i in pair_list_corr:
    df_init=survey[survey[i[0]].notnull()]
    tot=len(df_init)
    df_omit_one=df_init[df_init[i[0]] !=1]
    #portion_never=(tot-df_omit_one)/float(tot) # I put the float in because otherwise it only gives integer outputs. This is the portion of people who never express the topic. 
    #print "The portion of people who answered never in the category %s"%(i[0]) 
    Pair_Cor(df_omit_one,[(i[0],i[1])]) 
       

#Pair_Cor(survey,pair_list_corr)

