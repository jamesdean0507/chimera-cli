# site scraper general barebones design 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd
import geopandas as gpd
from get_xpath import xpath_soup


def humdata_filter(items, section, driver):
	t=section
	user_data=items	
	list=t.findAll('li')
	for opt in user_data:
		search_box=t.find('div',{'class':'categ-search'})
		search_box=search_box.find('input')
		search_xpath=xpath_soup(search_box)
		search_bar=driver.find_element_by_xpath(search_xpath)
		more=t.find('span',{'class':'show-more'})
		more_xpath=xpath_soup(more)
		morebutton=driver.find_element_by_xpath(more_xpath)
		
		morebutton.click()
		time.sleep(1)
		search_bar.send_keys(opt)
		for option in list:
			countryname=option.get_text()
			if opt in countryname:
				try:
					checkbox=option.find('input')
					checkbox_xpath=xpath_soup(checkbox)
					check=driver.find_element_by_xpath(checkbox_xpath)
					time.sleep(1)
					# print(check)
					check.click()
				except:
						print('failed to input one or more country')

def humdata_scraper(website, countrylist, organizationlist, filetypelist):
	chrome_options = Options()
	# chrome_options.add_argument('--headless')
	 ## uncomment this line for brave vvv ##
	# chrome_options.binary_location= r'path to brave.exe'
	driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
	driver.get(website)
	time.sleep(2)
	soup=BeautifulSoup(driver.page_source, 'html.parser')	
	filters=soup.findAll('div',{'class':'filter-category'})	
	for t in filters:
		title=t.find('div',{'class':'categ-title'})
		titletext=title.get_text()
		if 'Location' in titletext:
			humdata_filter(countrylist, t, driver)


def scrape_sites(countrylist=['Denmark', 'Antartica'], filetypelist=['CSV','Shapefile'], organizationlist=['Facebook','WorldPop'], taglist=[], querylist=[], sitelist=['https://data.humdata.org/search?ext_geodata=1&q=&ext_page_size=25']):
	for site in sitelist:
		if 'humdata.org' in site:
			humdata_scraper(site, countrylist, organizationlist, filetypelist)

scrape_sites()