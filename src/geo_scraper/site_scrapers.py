# site scraper general barebones design 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd
import geopandas as gpd



# pass in country, filetype, organization, tag, query search parameters. 
def scrape_site(*country, *filetype, *organization, *tag, query, site='https://data.humdata.org/search?ext_geodata=1&q=&ext_page_size=25'):
    chrome_options = Options()
	# chrome_options.add_argument('--headless')
	 ## uncomment this line for brave vvv ##
	# chrome_options.binary_location= r'path to brave.exe'
	driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
	driver.get('https://data.humdata.org/search?ext_geodata=1&q=&ext_page_size=25')
	time.sleep(2)
	soup=BeautifulSoup(driver.page_source, 'html.parser')	

	filters=soup.findAll('div',{'class':'filter-category'})	

	for t in filters:
	    title=t.find('div',{'class':'categ-title'})
	    titletext=title.get_text()
	    if 'Location' in titletext:
	        print(title.name)
	#         locationfiltersection=driver.find_element_by_css_selector('[name="q"])
	        print (t['class'])
