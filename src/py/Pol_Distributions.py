
from nltk import*

from nltk.corpus import PlaintextCorpusReader



#Assign a directory for corpus to be used.

corpus_Dem = '/Users/asaf/Documents/politics/Dem'
corpus_Rep = '/Users/asaf/Documents/politics/Rep'


# Load the corpus into nltk and store files as separate file ID, which
#can be accessed by name.

words_Dem=PlaintextCorpusReader(corpus_Dem, '.*')
words_Rep=PlaintextCorpusReader(corpus_Rep, '.*')

#to see which files are in the corpus use the command: wordlists.fileids()

#pull the tokenized words from each corpus

Dem_wordlist = words_Dem.words()
Rep_wordlist = words_Rep.words()

#Create Frequency Distributions for each of these
DemDist = FreqDist(Dem_wordlist)
RepDist = FreqDist(Rep_wordlist)



# Put in collocation code with the import











