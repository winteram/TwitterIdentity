

import re
from urllib import urlopen
from bs4 import BeautifulSoup
from nltk import *
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from nltk.collocations import *





def parseURLs(urllist):
    # verify the input is a list
    assert type(urllist) == type(list())
    urlText = ""
    for url in urllist:
        try:

            urlRaw = urlopen(url).read()
            urlSoup = BeautifulSoup(urlRaw)
            for para in urlSoup.find_all('p'):
                urlText += para.get_text()
            urlText += " " 
            urlText = re.sub('[^a-zA-Z ]', '', urlText)
            urlText = re.sub('(?P<endword>[a-z]+)(?P<begword>[A-Z])', '\g<endword> \g<begword>', urlText)
            urlText = urlText.lower().encode('utf8')
        except:
            pass
    # Create Frequency Distributions for bigrams
    # url_bigrams = BigramCollocationFinder._ngram_freqdist(urlText, 2)

    # Create Frequency Distributions for trigrams
    # url_trigrams = BigramCollocationFinder._ngram_freqdist(urlText, 3)

    return [w for w in word_tokenize(urlText) if w not in stopwords.words('english')]




def unshorten_url(url):
    try:
        parsed = urlparse.urlparse(url)
        h = httplib.HTTPConnection(parsed.netloc)
        h.request('HEAD', parsed.path)
        response = h.getresponse()
        if response.status/100 == 3 and response.getheader('Location'):
            return response.getheader('Location')
        else:
            return url
    except:
        pass


g=parseURLs(['www.nytimes.com/']) 



