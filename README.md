## News Scan Chrome Extensions

**Inspiration**

As a generation that reads a lot of political news, it is important to be able to get a wide range of information on a certain event. This lead us to make News Scan.

##What it does
With News Scan, when someone opens a news article on NYT for example, the extension will scrape the web for similar articles and then use APIs to compare articles and find sentences that are not in the current article and sentences that are similar to check the reliability of the article as well as to find information not in the current article that may have been left out accidentally or on purpose.

##How we built it
We used a Flask server that runs a python backend, in addition to a Javascript frontend which handles user input through a chrome extension. The backend processes the similar articles using Natural Language Processing libraries available on python and then feeds that through to the frontend chrome extension built using Javascript, HTML and CSS. This displays a similarity score as well as similar phrases from multiple articles that give more info to the user.

##Challenges we ran into
This project was extremely difficult because we had to scrape the web with python using the BeautifulSoup library and then used the nltk library to perform natural language processing in understanding the articles and then we compared the articles using Cosine similarity and finally had to output the data that was on a server to the extension using JSON so that it displays on the chrome extension that was built using javascript. Connecting all the services was an extremely difficult process especially since we were using them for the first time. We managed to get a lot of the services integrated but getting the completely different Flask server and Javascript extension to interact was a big challenge we're still on the verge to solve.

##Accomplishments that we're proud of
We were able to learn how to use web scraping from scratch and successfully used natural language processing libraries as well to compare articles and learnt a lot during this. We still think this idea has great potential and are hoping to work on this in the future.

##What we learned
We learnt a lot of API calls and a lot about web scraping and fully learnt how to make a chrome extension from the ground up. Getting to know how to use a python flask server was also very amazing.

##What's next for News Scan
We really hope to publish this extension and then finalise the service integrations so that it works seamlessly. We can publish the servers online so that they are not local and then hope that everyone can use the extension. We've got a lot of strong backend algorithms working on finding and comparing articles and we think it's a great product.
