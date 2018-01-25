#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get
from BeautifulSoup import BeautifulSoup
from logging import warning
from sys import exit, argv
from urlparse import urljoin

from utils import load_config
from storage import *

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

def search_assets_p2(url):
	pass

if __name__ == '__main__':
	conf = load_config()
	for platform, url in conf['platforms']:
		locals()["search_assets_{0}".format(platform)](url)
		#Save to database