from googlesearch import search
import urllib2
from BeautifulSoup import BeautifulSoup
from nltk.tag import pos_tag

def parseNouns(title):
    tagged_sent = pos_tag(title.split())
    nouns = [word for word,pos in tagged_sent if pos == 'NNP']
    return nouns

website_url = "https://www.bloomberg.com/news/articles/2018-09-14/trump-said-to-want-200-billion-in-china-tariffs-despite-talks"
soup = BeautifulSoup(urllib2.urlopen(website_url))
title = soup.title.string
print title

query =  parseNouns(title)


query = query[:query.find('|')]
print ("article title is " + query)

for url in search(query, stop=20):
    print(url)


