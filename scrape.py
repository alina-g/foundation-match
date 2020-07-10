import requests
from bs4 import BeautifulSoup
import json
from pandas import DataFrame as df
import pandas as pd


page = requests.get("https://www.sephora.com/shop/foundation-makeup")
soup = BeautifulSoup(page.text, 'html.parser')

# find all products links
products = soup.find_all('a', {'class': 'css-ix8km1'})


product_links = []
product_titles = []

for i in products:
	title = i.get('aria-label') # titles of the foundation product
	hrefs = i.get('href') # link to the foundation product
	product_links.append(hrefs)
	product_titles.append(title)
	

# data = {'Product Title': product_titles, 'Product Links': product_links}
# product_df = pd.DataFrame(data)
# print(product_df)

swatch_titles = []
swatch_links = []
count_names = 0
img_count = 0
dictionary = {}
count = 0

for link in product_links:
	page = requests.get('https://www.sephora.com' + link)
	soup = BeautifulSoup(page.text, 'html.parser')
	swatches = soup.find_all('button', {'data-at': 'selected_swatch'}) # find all shades of foundation 
	swatch_imgs = soup.find_all('img') #find all images of the shades of foundations 
	
	for swatch in swatches:
		swatch_name = swatch.get('aria-label') # name of the shade
		swatch_titles.append(swatch_name)
		count_names += 1

	for img in swatch_imgs:
		swatch_img = img.get('src')
		
		if swatch_img.startswith('/productimages/sku/') and swatch_img.endswith('+sw.jpg'):
			#download the img w/ 'www.sephora/...'
# 			print(swatch_img)
			img_count += 1
			swatch_links.append(swatch_img)
		
	swatch_data = {'Swatch Title': swatch_titles, 'Swatch Links': swatch_links}	
	#swatch_df = pd.DataFrame(swatch_data)
	dictionary[count] = pd.DataFrame(swatch_data)
		
		
print(dictionary[2])		

