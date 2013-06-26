import cPickle
import re
from random import shuffle

object2=open('Seed_List','r')
seed_list=cPickle.load(object2)
object2.close()

object2=open('Seed_Follow','r')
seed_follow=cPickle.load(object2)
object2.close()

object2=open('Dev_List','r')
dev_list=cPickle.load(object2)
object2.close()

object2=open('Dev_Follow','r')
dev_follow=cPickle.load(object2)
object2.close()

object2=open('Test_List','r')
test_list=cPickle.load(object2)
object2.close()

object2=open('Test_Follow','r')
test_follow=cPickle.load(object2)
object2.close()

# could join and shuffle the lists here...

vwtrain = []
for i in range(len(seed_list[0])):
#	vwtrain.append('-1 |follow ' + ' '.join(seed_follow[0][i]))
#	vwtrain.append('-1 |tweet ' + ''.join(re.findall('[\w ]',' '.join(seed_list[0][i]))) )
	vwtrain.append('-1 |follow ' + ' '.join(seed_follow[0][i]) + ' |tweet ' + ''.join(re.findall('[\w ]',' '.join(seed_list[0][i]))) )


for i in range(len(dev_list[0])):
#	vwtrain.append('-1 |follow ' + ' '.join(seed_follow[0][i]))
#	vwtrain.append('-1 |tweet ' + ''.join(re.findall('[\w ]',' '.join(dev_list[0][i]))) )
	vwtrain.append('-1 |follow ' + ' '.join(seed_follow[0][i]) + ' |tweet ' + ''.join(re.findall('[\w ]',' '.join(dev_list[0][i]))) )

for i in range(len(seed_list[1])):
#	vwtrain.append('1 |follow ' + ' '.join(seed_follow[1][i]))
#	vwtrain.append('1 |tweet ' + ''.join(re.findall('[\w ]',' '.join(seed_list[1][i]))) )
	vwtrain.append('1 |follow ' + ' '.join(seed_follow[1][i]) + ' |tweet ' + ''.join(re.findall('[\w ]',' '.join(seed_list[1][i]))) )

for i in range(len(dev_list[1])):
#	vwtrain.append('1 |follow ' + ' '.join(dev_follow[1][i]))
#	vwtrain.append('1 |tweet ' + ''.join(re.findall('[\w ]',' '.join(dev_list[1][i]))) )
	vwtrain.append('1 |follow ' + ' '.join(dev_follow[1][i]) + ' |tweet ' + ''.join(re.findall('[\w ]',' '.join(dev_list[1][i]))) )

vwtest = []
for i in range(len(test_list[0])):
#	vwtest.append('-1 |follow ' + ' '.join(test_follow[0][i]))
#	vwtest.append('-1 |tweet ' + ''.join(re.findall('[\w ]',' '.join(test_list[0][i]))) )
	vwtest.append('-1 |follow ' + ' '.join(test_follow[0][i]) + ' |tweet ' + ''.join(re.findall('[\w ]',' '.join(test_list[0][i]))) )

for i in range(len(test_list[1])):
#	vwtest.append('1 |follow ' + ' '.join(test_follow[1][i]))
#	vwtest.append('1 |tweet ' + ''.join(re.findall('[\w ]',' '.join(test_list[1][i]))) )
	vwtest.append('1 |follow ' + ' '.join(test_follow[1][i]) + ' |tweet ' + ''.join(re.findall('[\w ]',' '.join(test_list[1][i]))) )



shuffle(vwtrain)
fh = open('vwtrain.txt','w')
for line in vwtrain:
	fh.write(line+'\n')
fh.close()

shuffle(vwtest)
fh = open('vwtest.txt','w')
for line in vwtest:
	fh.write(line+'\n')
fh.close()



