from googlesearch import search
import urllib2
from BeautifulSoup import BeautifulSoup


website_url = "http://www.foxnews.com/politics/2018/09/15/california-will-launch-its-own-damn-satellite-as-swipe-at-trump-governor-moonbeam-says.html"
soup = BeautifulSoup(urllib2.urlopen(website_url))

# to search
query = soup.title.string
query = query[:query.find('|')]
print ("article title is " + query)

for url in search(query, stop=20):
    print(url)


