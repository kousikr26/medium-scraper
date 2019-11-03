import os
import pdfkit
import re
def find_name(url):
	url_rev=url[::-1]
	for i in range(len(url)):
		if url_rev[i]=='/':
			break
	return url_rev[:i][::-1][:40]
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
if(len(to_read)<article_limit):
	print("SCRAPE MORE")

read_file=open("read.txt","a")
for article in to_read:
	read_file.write(article)
	read_file.write("\n")
read_file.close()
article_names=[]
for i in to_read:
	
	article_name=find_name(i)
	re.sub('[^A-Za-z0-9]+', '', article_name)
	article_path="./pdfs/"+article_name+".pdf"
	article_names.append(article_name+".pdf")
	
	pdfkit.from_url(i,article_path)

for j in article_names:
	os.system('python send.py'+" "+j)