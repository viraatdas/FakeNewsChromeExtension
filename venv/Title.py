from googlesearch import search
import urllib2
from BeautifulSoup import BeautifulSoup
from nltk.tag import pos_tag
from routes import url


def parseNouns(title):
    tagged_sent = pos_tag(title.split())
    nouns = [word for word,pos in tagged_sent if pos == 'NNP']
    return nouns

def parseASCII(text):
    chars = ['.', ',', '/', '-', '!', '?', '\'', '"']

    for i, w in enumerate(text):
        for j,l in enumerate(chars):
            w = w.replace(l,'')
        text[i] = w

    return text

def method ():
    website_url = "http://www.foxnews.com/politics/2018/09/15/california-will-launch-its-own-damn-satellite-as-swipe-at-trump-governor-moonbeam-says.html"
    soup = BeautifulSoup(urllib2.urlopen(website_url))
    title = soup.title.string
    title = title[:title.find('|')]
    print ("Article title: "+title)

    query = parseNouns(title)
    query = parseASCII(query)

    query = " ".join(query)
    print ("Query: "+query)

    for url in search(query, stop=20):
        print(url)

print method()
