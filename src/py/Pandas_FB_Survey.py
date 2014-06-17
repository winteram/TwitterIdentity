import numpy as np

from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt

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
        
    
    
    
    