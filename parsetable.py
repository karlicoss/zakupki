#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"Searches zakupki.gov.ru for suspicious letter combinations"

__author__    = "Dmitry Gerasimov"
__date__      = "2012"
__email__     = "karlicoss@gmail.com"

from BeautifulSoup import BeautifulSoup
import sys
import urllib
import re
import itertools

SEARCH_QUERY = u"http://zakupki.gov.ru/pgz/public/action/search/simple/run?orderName={}"
LINK_REGEX = r"/pgz/public/action/orders/info/common_info/show\?notificationId=(\d+)"
NOTIFICATION_PAGE = "http://zakupki.gov.ru/pgz/public/action/orders/info/common_info/show?notificationId={}"

RUSSIAN_LETTERS = map(unichr, range(ord(u'а'), ord(u'я') + 1)) + map(unichr, range(ord(u'А'), ord(u'Я') + 1))
BAD_LETTERS = ['a', 'c', 'e', 'm', 'o', 'p', 'x', 'y', 'A', 'B', 'C', 'E', 'H', 'O', 'P', 'T', 'X']
CHEAT_CANDIDATES = map(lambda p: p[0] + p[1], itertools.product(RUSSIAN_LETTERS, BAD_LETTERS)) + map(lambda p: p[0] + p[1], itertools.product(BAD_LETTERS, RUSSIAN_LETTERS))

def get_search_results(query):
	link = SEARCH_QUERY.format(query)
	soup = BeautifulSoup(urllib.urlopen(link.encode('utf-8')))

	container = soup.find(id = "searchResultContainer")
	items = container.findAll('a', {'class': "iceOutLnk"})
	result = []
	for item in items:
		notification_id = re.search(LINK_REGEX, str(item)).group(1)
		result.append(NOTIFICATION_PAGE.format(notification_id))
	return result

result = []
for query in CHEAT_CANDIDATES:
	print(u"Testing {}".format(query))
	res = get_search_results(query)
	result.extend(res)
	print("Got {} results".format(len(res)))

result = sorted(list(set(result))) # making links unique

for link in result:
	print(link)
