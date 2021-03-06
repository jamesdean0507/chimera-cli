# site scraper general barebones design 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
import re
import pandas as pd
import geopandas as gpd
from get_xpath import xpath_soup

class site:
    def humdata_search_filter(item, section, driver):
        # time.sleep(2)
        t=section
        opt=item    
        list=t.findAll('li')
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
            listname=option.get_text()
            if opt in listname:
                try:
                    checkbox=option.find('input')
                    checkbox_xpath=xpath_soup(checkbox)
                    check=driver.find_element_by_xpath(checkbox_xpath)
                    time.sleep(0)
                    # print(check)
                    check.click()
                except:
                    print('failed to input' + opt)

    def humdata_check_filter(item, section, driver):
        t=section
        opt=item    
        list=t.findAll('li')
        for listitem in list:
            listname=listitem.get_text()
            if opt in listname:
                try:
                    checkbox=listitem.find('input')
                    checkbox_xpath=xpath_soup(checkbox)
                    check=driver.find_element_by_xpath(checkbox_xpath)
                    time.sleep(0)
                    # print(check)
                    check.click()
                except:
                    pass


    def humdata_scraper(website, countrylist, organizationlist, filetypelist, taglist):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        driver.get(website)
        time.sleep(1)
        soup=BeautifulSoup(driver.page_source, 'html.parser')   
        filters=soup.findAll('div',{'class':'filter-category'})
        for country in countrylist:
            driver.get(website)
            for t in filters:
                title=t.find('div',{'class':'categ-title'})
                titletext=title.get_text()
                if 'Location' in titletext:
                    humdata_search_filter(country, t, driver)
                else:
                    pass
                # for organization in organizationlist:
                #   if 'Organisation' in titletext:
                #      try:
                #         humdata_search_filter(organization, t, driver)
                #      except:
                #         humdata_check_filter(organization, t, driver)
                #   for tag in taglist:
                #      if 'Tag'in titletext:
                #         try:    
                #            humdata_search_filter(tag, t, driver)
                #         except:
                #            humdata_check_filter(tag, t, driver)
                #      for format in filetypelist:
                #         try:
                #            humdata_search_filter(format, t, driver)
                #         except:
                #            humdata_check_filter(format, t, driver)
        driver.quit()


    def diva_scraper(website, countrylist, taglist):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        try:
            for country in countrylist:
                for tag in taglist:
                    try:
                        driver.get(website)
                        # print(country,tag)
                        time.sleep(1)
                        ctlistopen=driver.find_element_by_name('cnt')
                        selectcountry= Select(ctlistopen)
                        selectcountry.select_by_visible_text(country)
                        time.sleep(0)
                        subjlistopen=driver.find_element_by_name('thm')
                        selectsubj=Select(subjlistopen)
                        selectsubj.select_by_visible_text(tag)
                        time.sleep(0)
                        okbutton=driver.find_element_by_name('OK')
                        time.sleep(0)  
                        okbutton.click()
                        print(country,tag,' Found on Diva-GIS')
                    except:
                        # print('failed to input', country, tag)
                        print(country,tag,' Not Found on Diva-GIS')
                        pass
        except:
            pass
        driver.quit()

    def poi_scraper(website, countrylist,organizationlist,taglist,querylist):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        matchlist=[]
        driver.get(website)
        time.sleep(1)
        soup=BeautifulSoup(driver.page_source, 'html.parser')
        links=soup.findAll('li')    

        for link in links:
            linktitle=link.get_text()
            for tag in taglist:
                if tag in linktitle:
                    matchlist.append(link)
            for query in querylist:
                if query in linktitle: 
                    matchlist.append(link)
            for country in countrylist:
                if country in linktitle:
                    matchlist.append(link)
            for org in organizationlist:
                if org in linktitle:
                    matchlist.append(link)
        matchlist=list(dict.fromkeys(matchlist))
        # print (matchlist)
        regex = re.compile(r'">.*')
        for x in matchlist:
            pagelink=str(x)
            pagelink=pagelink.replace('<li><a href="','')
            pagelink=re.sub('">.*', '', pagelink)
            driver.get('http://www.poi-factory.com'+pagelink)
            time.sleep(0.1)
            soup=BeautifulSoup(driver.page_source, 'html.parser')
            pagetitle=soup.find('h1').get_text()
            print(pagetitle)
        driver.quit()

    def scrape_sites(countrylist=['Denmark', 'Albania'], filetypelist=['CSV','Shapefile'], organizationlist=['Facebook','WorldPop'], taglist=['Roads', 'Inland water', 'weather and climate'], querylist=['gay', 'grocer', 'Restaurant'], sitelist=['http://www.poi-factory.com/poifiles/alpha','https://data.humdata.org/search?ext_geodata=1&q=&ext_page_size=25', 'https://www.diva-gis.org/GData']):
        for site in sitelist:
            if 'humdata.org' in site:
                humdata_scraper(site, countrylist, organizationlist, filetypelist, taglist)
            if 'diva-gis' in site:
                diva_scraper(site, countrylist, taglist)
            if "poi-factory" in site:
                poi_scraper(site, countrylist, organizationlist,taglist,querylist)

if __name__ == "__main__":
    site.scrape_sites()