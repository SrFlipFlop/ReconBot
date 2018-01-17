from requests import get
from BeautifulSoup import BeautifulSoup
from logging import warning
from sys import exit
from urlparse import urljoin

from utils import utils
from utils import storage

def search_assets_p1(url):
	page = 1
	items = []
	pagination = True
	while pagination:
		res = get('{0}?page={1}'.format(url, page))
		soup = BeautifulSoup(res.content)
		items += soup.findAll('div', {'rel': True})
		pagination = have_pagination_p1(soup)
		page += 1

	if not items:
		warning('Error HTML assets from {0}'.format(url))
		exit()

	assets = {}
	for item in items:
		asset_path = item.find('a', {'class': 'propertyImgLink '})['href']
		res = get(urljoin(url, asset_path))
		soup = BeautifulSoup(res.content)

		price = soup.find('p', {'class':'price'})
		url = soup.find('a', {'class': 'propertyImgLink '})['href']
		assets[item['rel']] = {
			'url': url,
			'money': price.text if price else 'None',
		}

	return assets

def have_pagination_p1(html):
	ul = html.find('ul', {'class': 'pagination'})
	if ul:
		if ul.find('ul', {'class': 'next disabled'}):
			return False
		if ul.find('ul', {'class': 'next'}):
			return True
	return False

def save_assets_database(assets):
	pass

def save_assets_local(assets):
	pass

if __name__ == '__main__':
	config = load_config()