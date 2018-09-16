# -*- coding: utf-8 -*-
from nltk.tag import pos_tag
from googlesearch import search
from bs4 import BeautifulSoup
import requests

def function (website_url):
    soup = BeautifulSoup(requests.get(website_url).content, "html.parser")
    title = soup.title.string
    title = title[:title.find('|')]

    tagged_sent = pos_tag(title.split())
    nouns = [word for word, pos in tagged_sent if pos == 'NNP']
    query = nouns

    def parseASCII(text):
        chars = ['.', ',', '/', '-', '!', '?', '\'', '"']

        for i, w in enumerate(text):
            for j, l in enumerate(chars):
                w = w.replace(l, '')
            text[i] = w

        return text

    query = parseASCII(query)
    query = "".join(query)

    site_prefix = ["site:foxnews.com ", "site: businessinsider.com ", "site: wsj.com ", "sites: nytimes.com ", "site: washingtonpost.com "]

    query_list = []
    i = 0
    while i<5:
        query_list.append(site_prefix[i] + query)
        i+=1
    print (query_list)

    url_list_fox=[]
    url_list_business = []
    url_list_wall = []
    url_list_new = []
    url_list_washington = []

    for url in search(query_list[0], stop=5):
        (url_list_fox.append(url))

    for url in search(query_list[1], stop=5):
        url_list_business.append(url)

    for url in search(query_list[2], stop=5):
        url_list_wall.append(url)

    for url in search(query_list[3], stop=5):
        url_list_new.append(url)

    for url in search(query_list[4], stop=5):
        url_list_washington.append(url)


    url_list_fox = url_list_fox[0]
    url_list_business = url_list_business[0]
    url_list_wall = url_list_wall[0]
    url_list_new = url_list_new[0]
    url_list_washington = url_list_washington[0]

    def par (website_url):
        page = requests.get(website_url)
        soup = BeautifulSoup(page.text, 'html.parser')
        page = soup.findAll('p')
        return page

    body_of_text_fox = par(url_list_fox)
    body_of_text_business = par(url_list_business)
    body_of_text_wall = par(url_list_wall)
    body_of_text_new = par(url_list_new)
    body_of_text_washington = par(url_list_washington)


