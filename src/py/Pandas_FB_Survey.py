import numpy as np

from pandas import DataFrame, Series, concat
import pandas as pd
import matplotlib.pyplot as plt

import scipy.stats

import pymysql

from collections import defaultdict 


#I want to select the whole survey in a cur.fetch thing- then I can iterate through that and make each column a column in the data-frame- Then in the comments
#I can declare what each data-frame is. 
#But it looks I will have to make stuff into dictionaries before I can get these frames.  

#Let's start by pulling all the survey elements. 




# Making a function- takes in the name of a table and then creates a python dataframe out of it. 

def FrameMaker(tablename):
    conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='groupid', passwd='letspublish', db='gidb')
    cur = conn.cursor()
    query= "Describe " + tablename + ";"
    cur.execute(query)
    names1=cur.fetchall()
    names=[i[0] for i in names1]
    record=defaultdict(list)
    query="SELECT * FROM " + tablename + ";"
    cur.execute(query)
    Participant_data=cur.fetchall()
    cur.close()
    # For each participant you
    for i in Participant_data:
        for j, name in enumerate(names):
            record[name].append(i[j])
    return DataFrame(record)


# For some reason Independents were labeled as '' in the database. So, I'm changing this in the dataframe.

survey=FrameMaker('survey')

party=survey['party']

survey['party']=party.replace('','Independent')

#Also, for some reason when people didn't answer the questions- they got input as -1. I need to change this- at least for political party right now
#I could change it for the whole survey, but I need to be sure that negative values aren't somehow important in some way.

#Step 1 get the names of all the political identity related columns

all_cols=list(survey.keys()) # This gives a list of every column name in the survey. These appear in alphabetic order so really. Since every politically related column is labeled
# with the pol prefix, I can just do a bit of indexing and slicing.

#beginning index 

pol_start=all_cols.index('party0_bond')
pol_end=all_cols.index('party_com')

pol_list=all_cols[pol_start:pol_end]

#checked length pol_list is 14, which is the number of items in the political identity survey. All are present.

for i in pol_list:
    survey[i]=survey[i].replace(-1,None)   

 


'''
This is a generic function that takes in factor names and their associated items and whether or not these items are reverse scored- then it creates a new
column in the data frame with that scored item and the column name you chose.

Here is the format for inputs to this function: {'FactorName':[('item1,1),(item2,-1),(item3,1)]}

The input is just a dictionary where the key is the name of the factor, and the value is a list of tuples, where the first entry is the item name in the
dataframe. The 2nd entry indicates whether the item is to be reversed scored. 1= normal scoring, -1= reversese scoring. 

 Below I specify dictionaries, which will be input for the factor scoring function 

'''



# Factor inputs politics

solidarity={'solidarity':[('party0_bond',1),('party1_solidarity',1),('party2_committed',1)]}
satisfaction={'satisfaction':[(u'party3_glad',1), (u'party4_proud',1), (u'party5_pleasant',1), (u'party6_goodfeel',1)]}
centrality={'centrality':[(u'party7_think',1), (u'party8_identity',1), (u'party9_seemyself',1)]}
self_stereo={'self_stereo':[(u'party10_common_avg',1), (u'party11_similar_avg',1)]}
ingroup_homo={'ingroup_homo':[(u'party11_similar_avg',1), (u'party12_common_oth',1)]}

#Once these factors have all been run through, I will plot the composite score for all factors.


composite={'pol_composite':[('solidarity',1),('satisfaction',1), ('centrality',1),('self_stereo',1),('ingroup_homo',1)]}


# Factor inputs CSWs

appearance={'appearance':[('con_agree_0',1),('con_agree_3',-1),('con_agree_16',1),('con_agree_20',1),('con_agree_29',-1)]}
family_support={'family_support':[('con_agree_6',1),('con_agree_9',-1),('con_agree_15',1),('con_agree_23',1),('con_agree_28',1)]}
competition={'competition':[('con_agree_2',1),('con_agree_11',1),('con_agree_19',1),('con_agree_24',1),('con_agree_31',1)]}
GodLove={'GodLove':[('con_agree_1',1),('con_agree_7',1),('con_agree_17',1),('con_agree_25',1),('con_agree_30',1)]}
academics={'academics':[('con_agree_12',-1),('con_agree_18',1),('con_agree_21',1),('con_agree_26',1),('con_agree_32',1)]}
virtue={'virtue':[('con_agree_4',1),('con_agree_10',1),('con_agree_13',1),('con_agree_27',1),('con_agree_33',1)]}
approval={'approval':[('con_agree_5',-1),('con_agree_8',1),('con_agree_14',-1),('con_agree_22',-1),('con_agree_34',1)]}
#Function to take inputs and make columns out of those factors. 


#I could make it so that this function simply changes values of -1 to None. Something like: item[0]=item[0].replace(-1,None)

def AddFactor(factors, dataframe):
    
    for factor in factors.keys():
        dataframe[factor]=0 #Initialize the dataframe with zeros
        for item in factors[factor]:
            dataframe[item[0]]=dataframe[item[0]].replace(-1,None)# Just putting this in here assuming that -1 shouldn't be a valid value for any of our factors which are recorded on a positive scale. 
            dataframe[factor]+=dataframe[item[0]]*item[1]


#Make a vector of the factors you want to add

factor_set=[solidarity,satisfaction, centrality,self_stereo,ingroup_homo, appearance, family_support, competition, GodLove, academics, virtue, approval]

# add these to the dataframe, specify name of dataframe here

dframe=survey

for factor in factor_set:
    AddFactor(factor,dframe)
    


#Add the composite score:

AddFactor(composite,dframe)






#Hm... I might have been able to put my factors in one big dictionary with the factor names as keys- as opposed to variables then I wouldn't have to go through this
#process of pulling them out like this- I could also then just put it into the same function so that it automatically plots whatever I'm after in histogram- add another
#variable for the name I want to give to the file with multiple factors. 

factor_names=['pol_composite', 'solidarity','satisfaction', 'centrality','self_stereo','ingroup_homo']

#CSW names
CSW_names=['appearance', 'family_support', 'competition', 'GodLove', 'academics', 'virtue', 'approval']


#When writing an abstract function that plots these treat even and odd numbers to be plotted as different cases. This is the case of an odd number of factors. It's the n-1 row, I believe that should be
#treated differently

fig, axes= plt.subplots(2,3)

count = 0
for j in range(2):
    for k in range(3):

        z= factor_names[count]
        axes[j,k].set_title(z)
        w=survey[z]
        w.hist(ax=axes[j,k])
        count += 1
        
#Make loop for contingencies of self-worth plot

fig, axes= plt.subplots(2,4)

count=0
for j in range(2):
    for k in range(4):
        
        if count < 7:  # don't plot the last one, where count = 7. 

            z= CSW_names[count]
            axes[j,k].set_title(z)
            w=survey[z]
            w.hist(ax=axes[j,k])
            count += 1
'''

for i in factor_names:
    for j in range(2):
        for k in range(3):
            if j==2 and k==3: #This is the case for which there should be no graph
                pass
            else:
'''
                



'''

fig=plt.figure()

ax1 = fig.add_subplot(2, 3, 1) 
ax1.set_title('Solidarity')

w=survey['solidarity']

w.hist(ax=ax1)

'''


#That generally works for graphing, but one thing- Must replace values in columns- marked -1 with NaN, 

#Should do a dictionary slice.
           
    
    





# Some Merges and merge functions

#Must mend some of the data. How will null data be dealth with in general? Also, the We don't have a place for Independent in the data frame. If we see a duplicate. Go through the fields and see
#which of the multiple has the most data- remove the ones that have less data. We know something is a duplicate because the facebook or twitter Id will appear 2 or more times.



'''

Now I'm just playing around

'''

# This is a nice function to get the lay of the land. 

survey['fb_academic'].describe()

  
#No make a function to create a correlation matrix of many of the things we are interested- correlation between Twitter and Facebook,

#explicit statements of expression and identies + CSW's.


#This is going to be a big matrix, let's see how it works


fb_corrs=['appearance', 'family_support', 'competition', 'GodLove', 'academics', 'virtue', 'approval', 'fb_academic', 'fb_appearance', 'fb_family', 'fb_god','fb_political','pol_composite', 'solidarity','satisfaction', 'centrality','self_stereo','ingroup_homo']
fb_pol_cor=['fb_political','pol_composite', 'solidarity','satisfaction', 'centrality','self_stereo','ingroup_homo']         
# Correlation function
tw_pol_cor=['tw_political','pol_composite', 'solidarity','satisfaction', 'centrality','self_stereo','ingroup_homo']
#Arguments, mainFrame= DataFrame you are wanting to take a subset of. item_list= the columns you want to be in the correlation matrix- pass this in as a python list

def CorMatrix(mainFrame, item_list):
    concatlist=[] #Initialize a new list that will be used to create a separate dataframe.
    for i in item_list:
        concatlist.append(mainFrame[i])
    corFrame=pd.concat(concatlist,axis=1) # He I am just making new dataframe- axis=1 specifies that I want this to be a dataframe and not a Series object. 
    return corFrame.corr() 
    
    
 #The above function works, but there is no way to get significance values for the correlation from PANDAS. So, I found this function for computing pairwise correlations. Maybe, I can use the previous
 # function to find interesting correlations, then I can look at their significance using the following function:
 
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

    
        # Here is a simple function for doing a number of pair-wise t-tests (later I can figure out how to generate tables for these)- right now, I can just print.
        # Assume these all come from the same data_frame, make a tuple that represents the pairs of columns you are comparing. 

#Here is example input

pair_list=[('fb_academic','tw_academic'),('fb_appearance','tw_appearance'),('fb_doing','tw_doing'),('fb_entertain','tw_entertain'),('fb_family','tw_family'),('fb_feel','tw_feel'),
            ('fb_god','tw_god'),('fb_political','tw_political'),('fb_where','tw_where')]

def t_comparisons(DataFrame, pairs):
    for pair in pairs:
        one=DataFrame[pair[0]].dropna()
        two=DataFrame[pair[1]].dropna()
        mean1=mean(one)
        mean2=mean(two)
        t, p = scipy.stats.ttest_ind(one, two)

        
        print "The Mean for %s is %s , and the mean for %s is %s ;The p-value for this comparison is %s ,and the t-value is %s" %(pair[0],mean1,pair[1],mean2,p,t,) 
     
     
t_comparisons(survey,pair_list)

#Now I'm making a new function for generating output for a list of correlations. I want to to do this to see how well contingencies of self-worth correlate with corresponding questions about how frequently people
#express these on FB or Twitter.

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
        
Pair_Cor(survey,pair_list_corr)


#Now for self-aspects stuff- first I might need to join self-aspects with other survey data. 
#Make a dataframe from the table aspects

aspects=FrameMaker('aspects')

traits=FrameMaker('aspects_traits')

#Looks like this table stores the corresponding

#code for plotting frequency tables

 g=aspects['Label'].value_counts()
 g.plot(kind='barh', stacked=True)
 
 
 #Right now I'm just going to make a quick and dirty function that shows me differences between Twitter and Facebook in terms of expression of self, aspects using a T-test.
 
 
#This function gives me the unique values 

 w=Series(aspects['Label'].values.ravel()).unique()
 
 #This also works and might be easier to understand and do later :  k=aspects['Label'].value_counts(),j=k.keys()
 
 
 #Dframe= the dataframe you are using, cat_name= the name of the of the general category- basically the column name in the data frame from which you will be breaking down the analysis. cat_list= all the specific values of the
 #category, which will represent different comparisons using the t-test.  
 
 #Let me make the inputs for this function
 
 
 #For some reason this function is crashing when the category label ='public', I'm going to have to investigate that. 

def Compare_GroupbyCat(Dframe,cat_name, cat_list, GroupNames):
    for i in cat_list:
        df_init=Dframe[Dframe[cat_name]==i]
        
        one=df_init[GroupNames[0]].dropna()
        two=df_init[GroupNames[1]].dropna()
        mean1=mean(one)
        mean2=mean(two)
        t, p = scipy.stats.ttest_ind(one, two)

        
        print "For the comparison of the category value %s, the mean for %s is %s , and the mean for %s is %s ;The p-value for this comparison is %s ,and the t-value is %s" %(i,GroupNames[0], mean1,GroupNames[1],mean2,p,t,) 

Compare_GroupbyCat(aspects, 'Label',w,['Twitter','Facebook'])


#Now I want to see if there is a relationship between 1) how positive or negative someone feels about a self-aspect and the relative proportion of positive or negative traits present for that aspect 2) The relationship between relative
#positivity or negativity of an aspect (based on traits) and how much people report expressing these things on FB or Twitter.  


#Step 1- map the trait numbers to positivity or negativity. 
positive_traits=[(1,'capable'),(2,'comfortable'),(3,'comunicative'),(4,'confident'),(7,'energetic'),(8,'friendly'),(9,'fun and entertaining'),(10,'giving'),(11,'happy'),(12,'hardworking'),
(17,'independent'),(20,'intelligent'),(21,'interested'),(27,'lovable'),(28,'mature'),(29,'needed'),(30,'optimistic'),(31,'organized'),(32,'outgoing'),(35,'successful')]
negative_traits=[(5,'disagreeing'),(6,'disorganized'),(13,'hopeless'),(14,'immature'),(15,'incompetent'),(16,'indecisive'),(18,'inferior'),(19,'insecure'),(22,'irresponsible'),(23,'irritable'),(24,'isolated'),(25,'lazy'),
(26,'like a failure'),(33,'sad and blue'),(34,'self-centered'),(36,'tense'),(37,'uncomfortable'),(38,'unloved'),(39,'weary'),(40,'worthless')]

pos_traitId=[i[0] for i in positive_traits]
neg_traitId=[i[0] for i in negative_traits]


#Create a new column in the traits dataframe, that will indicate whether a trait is positive or negative. Positive=1, Negative=-1

traits['Valence']=None #Initialize the column

for i,j in enumerate(traits.TraitId):
    if int(j) in pos_traitId:
        traits['Valence'][i]=1
    else:
        traits['Valence'][i]=-1
        
#Later make a bar graph showing the frequency of expression of different traits in self-aspects. 

#Now for some code that goes through each self-aspect and in the aspect table, then creates a new column that represents the average valence of the traits associated with it. 

aspects['avg_val']=None # Initialize a column in aspects called avg_val, stands for average valence. 

for i,j in enumerate(aspects.Id):
    k=traits[traits.aspectId==j]
    aspects['avg_val'][i]=mean(k.Valence)
    

#Now we can look at the average valence of self-aspects and how likely people are to express this on Twitter and Facebook.
#What is the relationship between how positively someone feels about an aspect and the relative proportion of positive and negative traits.

Pair_Cor(aspects,[('avg_val','Twitter'),('avg_val','Facebook'),('avg_val','Positive'),('avg_val','Important')])
        
            
#Let's make a graph of the frequency of each each trait listed in self-aspects. First we make a new column in the dataframe for traits that represent the name of the trait.

w=positive_traits+negative_traits
 
traits_dic={}
 
for i in w:
    traits_dic[str(i[0])]=i[1]

traits['names']=None

for i,j in enumerate (traits.TraitId):
    traits['names'][i]=traits_dic[j]
    



#Make a score of normative traits- more frequent = more normative.

#Start by making a new column in the dataframe traits that gives the relative proportion of a given trait in the population of traits.
traits['relative']=None

#Make a new dictionary that maps the name of a trait to its relative frequency:

traits_rel={}

k=traits.names.value_counts() # Gives a data frame with the names and frequencies of each trait. 
tot=float(sum(k)) # this gives the total number of counts
for name in k.keys():
    traits_rel[name]= k[name]/tot


for i,j in enumerate(traits.names):
    traits['relative'][i]=traits_rel[j]
    
#Going to recycle some code here:

aspects['norm_avg']=None # Initialize a column in aspects that represents how normative the traits listed in an aspect are. 

#In the aspects table assign this column a value that is the average normative score for the traits listed.
for i,j in enumerate(aspects.Id):
    k=traits[traits.aspectId==j]
    aspects['norm_avg'][i]=mean(k.relative)


Pair_Cor(aspects,[('norm_avg','Twitter'),('norm_avg','Facebook'),('norm_avg','Positive'),('norm_avg','Important')])


#What is the relationship between the relative positivity of these aspects and positivity or negativity on the PANAS scale?

#Must create PANAS scores first- one for positive affect. One for negative affect


#I will just use my AddFactor function for this and get the input in the right format:

#just make a quick function to get in the right format- since I have a list of the items.

PN_Positive={"PANAS_Pos":[("interested",1),("excited",1),("strong",1),("enthusiastic",1),("proud",1),("alert",1),("inspired",1),("determined",1),("attentive",1),("active",1)]}

PN_Negative={"PANAS_Neg":[("distressed",1),("upset",1),("guilty",1),("scared",1),("hostile",1),("tired",1),("irritable",1),("ashamed",1),("nervous",1),("jittery",1),("afraid",1)]}

#PANAS_facts=[PN_Positive,PN_Negative]

AddFactor(PN_Positive,survey)

AddFactor(PN_Negative,survey)

#Make another factor- Tot_Affect, that is a combination of both factors- (Positive Affect) - (Negative Affect)

tot_affect={'tot_affect':[('PANAS_Pos',1),('PANAS_Neg',-1)]}

AddFactor(tot_affect,survey)

#Now create a new column in survey that represents avg valence for self-aspects someone generated- all self aspects. This can the be correlated with PANAS. 

survey['aspect_val']=None

for i,j in enumerate(survey.Id):
    k=aspects[aspects.UserId==j]
    survey['aspect_val'][i]=mean(k.avg_val)
    
    #Now, let's correlate this new value with PANAS

Pair_Cor(survey,[('aspect_val','tot_affect'),('aspect_val','PANAS_Pos'),('aspect_val','PANAS_Neg')])