from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

## Function takes list of usernames, check if username has profile on instagram ##
## Returns pandas dataframe with username, if profile is found ##
def username_check(username_list):
	## initiate web driver ##
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	## uncomment this line for brave vvv ##
	# chrome_options.binary_location= r'path to brave.exe'
	driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
	username_list=pd.read_csv(username_list)
	usernamel=[]
	usernamevaluelist=[]
	## iterate through username list ##
	for username in username_list["0"]:
		# go to page
		driver.get("https://www.instagram.com/"+username)
		time.sleep(3)
		soup = BeautifulSoup(driver.page_source, 'html.parser')
		title=soup.find("title").get_text()
		## If page not found is returned, value is not found, otherwise is found
		if "Page Not Found" in title:
			usernamevalue='not found'
		else:
			usernamevalue='found'
		usernamel.append(username)
		usernamevaluelist.append(usernamevalue)
		print (username, usernamevalue)
	df=pd.DataFrame({"Username":usernamel,"IG Profile":usernamevaluelist})
	return(df)