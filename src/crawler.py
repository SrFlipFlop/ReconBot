#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get
from BeautifulSoup import BeautifulSoup
from logging import warning
from sys import exit, argv
from urlparse import urljoin

from utils.utils import load_config
from utils.storage import *

def search_platforms(url):
	res = get(url)
	soup = BeautifulSoup(res.content)
	table = soup.find('table', {'class':'table-body-style-highlighted'})
	
	platforms = {}
	for row in table.findAll('tr'):
		a = row.find('a')
		name = row.find('a').text
		url = row.find('a')['href']
		platforms['name'] = url

	return platforms

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

if __name__ == '__main__':
	if len(argv) == 2:
		if argv[1] == 'p': #platforms	
			config = load_config()
			platforms = search_platforms(config['platforms_url'])

		if argv[1] == 'a': #assets			
			#Crawl each platform dinamically from configuration
			#locals()["f{0}".format(x)]()
			pass
	else:
		warning('Incorrect arguments using Crawler {0}'.format(argv))