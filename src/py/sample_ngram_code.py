


from nltk.collocations import *

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

finder = BigramCollocationFinder.from_words(wordlist)

finder.apply_freq_filter(20)

finder.nbest(trigram_measures.pmi,10)
