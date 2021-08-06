# site scraper general barebones design 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
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

def diva_scraper(website, countrylist, taglist):
	taglist=['Roads','Inland water'] 
	countrylist=['Denmark', 'Albania']
	website=[website]
	chrome_options = Options()
	driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
	time.sleep(2)
	try:
	    for country in countrylist:
	        for tag in taglist:
	            driver.get(website)
	            ctlistopen=driver.find_element_by_name('cnt')
	            selectcountry= Select(ctlistopen)
	            selectcountry.select_by_visible_text(country)
	            time.sleep(1)
	            subjlistopen=driver.find_element_by_name('thm')
	            selectsubj=Select(subjlistopen)
	            selectsubj.select_by_visible_text(tag)
	            time.sleep(1)
	            okbutton=driver.find_element_by_name('OK')
	            okbutton.click()
				
	            time.sleep(6)

	        
	except:
	    print('failed to scrape diva')

def scrape_sites(countrylist=['Denmark', 'Albania'], filetypelist=['CSV','Shapefile'], organizationlist=['Facebook','WorldPop'], taglist=['Roads', 'Inland Water'], querylist=[], sitelist=['https://data.humdata.org/search?ext_geodata=1&q=&ext_page_size=25', 'https://www.diva-gis.org/Data']):
	for site in sitelist:
		if 'humdata.org' in site:
			humdata_scraper(site, countrylist, organizationlist, filetypelist)
		if 'diva-gis' in site:
			diva_scraper(sitelist, countrylist, taglist)

scrape_sites()