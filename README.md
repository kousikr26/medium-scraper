# medium-scraper
**An article scraper and opener for medium to bypass the article limit for non members**<br/>
Medium limits the number of articles non-members can read to only a few per month. If you are not signed in you can read as many as you want, however you miss out the recommendations tailored to you.
This program signs in and scrapes out your daily recommendations based on your reading history and stores them. Then it opens these in a logged out window so that the number of articles are not limited and you also get to read your recommendations.
## Dependencies and requirements
* Python 3.7.3
* Selenium 3.141.0
* ChromeDriver 2.41.578700
## Usage
* First change the username and password to match yours in the scrape.py(Currently only google sign in is supported).
* Increase the delay time and scroll down when the medium home page opens if you want to load more articles.
* All the scraped article's links will be stored in articles.txt.
* To read run read.py(Change the article limit if you want to open more articles at once)
* All the opened articles will be stored in read.py and not opened again
