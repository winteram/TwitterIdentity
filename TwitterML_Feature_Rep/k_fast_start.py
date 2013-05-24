
import pickle
import cPickle 
import random
import numpy
from random import shuffle
import pymysql


conn = pymysql.connect(host='smallsocialsystems.com', port=3306, user='smalls7_groupid', passwd='LetsPublish!', db='smalls7_identity')

cur = conn.cursor()




object2=open('Seed_List','r')
Seed_List=cPickle.load(object2)


object3=open('IdList','r')
IdList=cPickle.load(object3)


object4=open('Dev_List', 'r')
Dev_List=cPickle.load(object4)

fileObject=open("Test_List",'r')
Test_List=cPickle.load(fileObject)


#Create the full list- which you can randomize later and divide up. 

full_object = [Seed_List[0] + Dev_List[0] + Test_List[0], Seed_List[1] + Dev_List[1] + Test_List[1]]


#randomization requires shuffling paralell arrays. This a little tricky because I there are separate lists for democrats
#and Republicans want to mix up Dems and republicans and hence have to d





IdList_0=[]
full_0=[]


index_shuf = range(len(IdList[0]))
shuffle(index_shuf)
for i in index_shuf:
    IdList_0.append(IdList[0][i])
    full_0.append(full_object[0][i])


IdList_1=[]
full_1=[]


index_shuf = range(len(IdList[1]))
shuffle(index_shuf)
for i in index_shuf:
    IdList_1.append(IdList[1][i])
    full_1.append(full_object[1][i])


full_update=[full_0,full_1]

Id_update=[IdList_0,IdList_1]

Seed_Split=len(Seed_List[0])
Dev_Split= Seed_Split+len(Dev_List[0])



Seed_List=[full_0[0:Seed_Split],full_1[0:Seed_Split]]
Dev_List=[full_0[Seed_Split:Dev_Split],full_1[Seed_Split:Dev_Split]]
Test_List=[full_0[Dev_Split:],full_1[Dev_Split:]]
IdList=[IdList_0,IdList_1]


#create a vector of the number of tweets for each test user. 


Test_Count_0=[]
Test_Count_1=[]

Test_Id0=IdList[0][Dev_Split:]
Test_Id1=IdList[1][Dev_Split:]

for user in Test_Id0:
	#the below command (without the fetchall(), will give the count of items from the query- this is a simple way to extract counts)

	count=cur.execute("SELECT TweetText FROM tweet WHERE UserId='"+ user +"';")
	
	Test_Count_0.append(count)


for user in Test_Id1:
	count=cur.execute("SELECT TweetText FROM tweet WHERE UserId='"+ user +"';")
	
	Test_Count_1.append(count)


Test_Count=[Test_Count_0,Test_Count_1]



	
fileObject=open("Test_Count",'w+')
cPickle.dump(Test_Count,fileObject)

fileObject.close()

fileObject=open("Seed_List",'w+')
cPickle.dump(Seed_List,fileObject)

fileObject.close()

fileObject=open("Dev_List",'w+')
cPickle.dump(Dev_List,fileObject)

fileObject.close()

fileObject=open("Test_List",'w+')
cPickle.dump(Test_List,fileObject)

fileObject.close()

fileObject=open("IdList",'w+')
cPickle.dump(IdList,fileObject)

fileObject.close()


cur.close()
conn.close()








