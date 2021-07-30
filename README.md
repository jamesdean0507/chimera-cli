# chimera-cli

Current Goals:
	- Command line interface to automate the scraping of multiple social networks to generate business leads and target market/demographic info. 
	- have multiple queries for users to select from cli
	- multiprocessing/proxy support for each action (as required) to avoid blocks and action limits
	- Store scraped information in local SQL, at the end of scrape return data in csv5.

Future Goals:

	-Automate multiple data transform actions to allow user to manipulate and analyze returned data in various ways



Organization:

	Menu:
		- Have options of which site to scrape, which (or how many) actions to run per site, and possible user input if req

	Scrapers:
		- Py module for each site
		- Have different function for each action per site,
			- ie; all actions for facebook would be on facebook_scrape.py and you can call functions from there

	Multiprocessing Func:
		- Some options will call functions async
		- Some will ask if you want to multiprocess or run solo

	SQL:
		- data storage
		- be able to export to other server or dl as csv