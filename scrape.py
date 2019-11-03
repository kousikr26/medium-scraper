import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

#change your google sign in username and password
user="#####"
password="######"


driver = webdriver.Chrome()
driver.get('https://medium.com/m/signin?redirect=https%3A%2F%2Fmedium.com%2F&source=--------------------------nav_reg&operation=login')
elem=driver.find_element_by_css_selector(".button.button--large.button--withChrome.js-googleButton")


elem.click()
time.sleep(3)
elem = driver.find_element_by_id("identifierId")
elem.send_keys(user)
elem.send_keys(Keys.RETURN)
time.sleep(3)
elem = driver.find_element_by_name("password")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)

time.sleep(10)#Increase this time if you want to save more articles

article_elems=[]
article_elems=driver.find_elements_by_css_selector(".extremePostPreview-post.u-minWidth0.u-flex1.u-marginRight24.u-textAlignLeft.js-trackPostPresentation")
articles=[]
count=0
for elem in article_elems:
	try:
		article=elem.find_element_by_css_selector(".ds-link.ds-link--stylePointer.u-overflowHidden.u-flex0.u-width100pct")
		count+=1
	except:
		pass
	link=article.get_attribute('href')
	print(link)
	articles.append(link)
	print("\n")
print(count," articles found\n\n\n")

print("writing to file")
filename="articles.txt"#create a file of this name
write_con=[]
readfile=open(filename,"r")
present_articles=readfile.read().splitlines()
for article in articles:
	if article in present_articles:
		write_con.append(0)
	else:
		write_con.append(1)

readfile.close()
outfile=open(filename,"a")
for i in range(len(articles)):
	if write_con[i]:
		outfile.write(articles[i])
		outfile.write("\n")
		
outfile.close()
driver.close()
os.system('python read.py')
