import urllib2
from BeautifulSoup import BeautifulSoup

website_url = "https://weather.com/storms/hurricane/news/2018-09-14-hurricane-florence-forecast-north-carolina-south-carolina-southeast"
soup = BeautifulSoup(urllib2.urlopen(website_url))
print soup.title.string