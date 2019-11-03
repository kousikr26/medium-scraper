from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time



read_file=open("read.txt","r")#contains articles which have been read or opened
articles_file=open("articles.txt","r")#contains the scraped articles
read_articles=read_file.read().splitlines()
unread_articles=articles_file.read().splitlines()
if(len(unread_articles)<10):
	print("Scrape more articles")
print(len(unread_articles)," articles are available")

read_file.close()
articles_file.close()
article_limit=5

to_read=[]
i=0
for article in unread_articles:
	if article not in read_articles:
		to_read.append(article)
		i+=1
	if i==article_limit:
		break
#open articles

driver = webdriver.Chrome()
driver.get("https://medium.com/")
time.sleep(3)
for article in to_read:
	print("NOW READING:")	
	print(article)
	driver.execute_script("window.open(\'{}\')".format(article))

	

	time.sleep(1)
read_file=open("read.txt","a")
for article in to_read:
	read_file.write(article)
	read_file.write("\n")
read_file.close()
with open("saved.txt","a") as save_file:
	while True:
		save_article=input("Enter article link to save or enter 'n' if there is none :  ")
		if save_article in ["n","N","No","no","NO"]:
			break
		save_file.write(save_article)
		save_file.write("\n")
driver.close()


