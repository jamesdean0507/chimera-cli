from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd


def username_check(username_list):
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	# chrome_options.binary_location= r'path to brave.exe'
	driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
	username_list=pd.read_csv(username_list)
	usernamel=[]
	usernamevaluelist=[]
	for username in username_list["0"]:
		
		driver.get("https://www.instagram.com/"+username)
		time.sleep(3)
		soup = BeautifulSoup(driver.page_source, 'html.parser')
		title=soup.find("title").get_text()

		if "Page Not Found" in title:
			usernamevalue='not found'
		else:
			usernamevalue='found'
		usernamel.append(username)
		usernamevaluelist.append(usernamevalue)
		print (username, usernamevalue)