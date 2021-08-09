# Menu
# PROBABLY WONT COMPILE
from consolemenu import * 
from consolemenu.items import * 
from colorama import *
from termcolor import colored

from geo_scraper.site_scrapers import humdata_check_filter, humdata_scraper

print(colored(ascii-art.txt, 'green', 'on_red'))

menu = ConsoleMenu("chimera", "interface")

humdata_search_item = MenuItem("-h -s")
humdata_check_item = MenuItem("-h -c")
humdata_scraper_item = MenuItem("scrape -h")
diva_scraper_item = MenuItem("scrape -d")
scrape_sites_item = MenuItem("scrape -s")

function_humdata_search = FunctionItem("humdata_search_filter(humdata_search_item, section, driver)")
function_humdata_check = FunctionItem("humdata_check_filter(humdata_check_item, section, driver)")
function_humdata_scraper = FunctionItem("humdata_scraper(website, countrylist, organizationlist, filetypelist, taglist)")
function_diva_scraper = FunctionItem("diva_scraper_(website, countrylist, taglist)")
function_scrape_sites = FunctionItem("scrape_sites(countrylist=['Denmark', 'Albania'], filetypelist=['CSV','Shapefile'], organizationlist=['Facebook','WorldPop'], taglist=['Roads', 'Inland water', 'weather and climate'], querylist=[], sitelist=['https://data.humdata.org/search?ext_geodata=1&q=&ext_page_size=25', 'https://www.diva-gis.org/GData'])")

command_humdata_search = CommandItem("Command", "touch out.txt")
command_humdata_check = CommandItem("Command", "touch out.txt")
command_humdata_scraper = CommandItem("Command", "touch out.txt")
command_diva_scraper = CommandItem("Command", "touch out.txt")
command_scrape_sites = CommandItem("Command", "touch out.txt")

selection_menu = SelectionMenu(["-h", "-s", "object"])
selection_menu = SelectionMenu(["-h", "-c", "object"])
selection_menu = SelectionMenu(["scrape", "-h", "object"])
selection_menu = SelectionMenu(["scrape", "-s", "object"])
selection_menu = SelectionMenu(["scrape", "-d", "object"])

menu.append_item(humdata_search_item)
menu.append_item(humdata_check_item)
menu.append_item(humdata_scraper_item)
menu.append_item(diva_scraper_item)
menu.append_item(scrape_sites_item)
menu.append_item(function_humdata_search)
menu.append_item(function_humdata_check)
menu.append_item(function_humdata_scraper)
menu.append_item(function_diva_scraper)
menu.append_item(function_scrape_sites)

menu.show()