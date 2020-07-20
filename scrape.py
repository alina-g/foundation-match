import requests
from bs4 import BeautifulSoup
import json
from pandas import DataFrame as df
import pandas as pd

def scrape_products():
	product_dict = {}
	
	page = requests.get("https://www.sephora.com/shop/foundation-makeup")
	soup = BeautifulSoup(page.text, 'html.parser')

	# find all products on the foundations page
	products = soup.find_all('a', {'class': 'css-ix8km1'})

	# store found titles and link in the lists AND IMAGES
	product_links = []
	product_titles = []

	for i in products:
		title = i.get('aria-label') # titles of the foundation product
		href = i.get('href') # link to the foundation product
		
		product_dict[title] = href
		
		product_links.append(hrefs)
		product_titles.append(title)
	

def scrape_swatches(link):
	swatch_titles = []
	swatch_links = []
	swatch_dict = {}

# find swatched for selected product
	page = requests.get('https://www.sephora.com' + link)
	soup = BeautifulSoup(page.text, 'html.parser')
	swatches = soup.find_all('button', {'data-at': 'selected_swatch'}) # find all shades of foundation 
# 	swatch_imgs = soup.find_all('img') #find all images of the shades of foundations 
	
	for swatch in swatches:
		swatch_name = swatch.get('aria-label') # name of the shade
		swatch_imgs = soup.find_all('img') #find all images of the shades of foundations 
		
		for img in swatch_imgs:
			swatch_img = img.get('src')
			if swatch_img.startswith('/productimages/sku/') and swatch_img.endswith('+sw.jpg'):
			# 'www.sephora/...' + swatch_link
			#swatch_links.append(swatch_img)
			#print(swatch_img)
				swatch_dict[swatch_name] = swatch_img
	print(swatch_dict)
	


	
scrape_products()
scrape_swatches('/product/pro-filtr-soft-matte-longwear-foundation-P87985432?icid2=products%20grid:p87985432')