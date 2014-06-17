

import sys, os

#reload(sys)
#sys.setdefaultencoding('utf-8') #The ensures that string output doesn't come back with a leading 'u', which is weird. 

#This is just specific to my computer. 
sys.path.append('C:\Users\Asaf\Documents\GitHub\TwitterIdentity\src\py')


import cPickle

import pickle

import subprocess


import multiprocessing 

path_files='C:\Users\Asaf\Documents\GitHub\TwitterIdentity\src\py'

#subprocess.Popen("script2.py 1", shell=True)

#os.system("script2.py 1")

def worker(files):
    os.system(files)



files=[path_files+'/job2.py',path_files+'/job3.py']

for i in files:
    p = multiprocessing.Process(target=worker(i))
    p.start()


    


