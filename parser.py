# /!usr/bin/env python
# -*- coding: UTF-8 -*-
import urllib2
from bs4 import BeautifulSoup


def openurl(url):
    response = urllib2.urlopen(url)
    return response.read()


# parse pod catalog
def parseUc(url):
    s = BeautifulSoup(openurl(url), 'html.parser')
    for t in s.find_all('div', class_='brand-item'):
        for k in t.find_all('button'):
            kk = k.text.lower().replace(' ', '')
            if k.text == str('ДНС').decode('utf-8'):
                kk = 'dns'
            # parse item of Catalog
            parseSubItem(openurl(url+'?brand='+kk+'&mode=list'))


# parse item of Catalog
def parseSubItem(html):
    sq = BeautifulSoup(html, 'html.parser')
    for t in sq.find_all('div', class_='product'):
        id = t.find('div', class_='item-desc')
        # haracteristics
        har = id.find('a',class_='ec-price-item-link').text
        # cena
        cena = t.find('div',class_='price_g').text
        # foto
        ssilka = t.find('img').get('src')
        print (t.find('div', class_='item-name').text+" --- "+har+" --- "+cena+" --- "+ssilka)


# parse all catalog of products
def parseCatalog(html):
    s = BeautifulSoup(html, 'html.parser')
    # find all <a> with text
    t = s.find('div', class_='catalog-content-desktop')
    for a in t.find_all('a'):
        # Del <span> from <a>
        for sp in a.find_all('span'):
            sp.clear()
        # Is it catalog
        # if '#' not in a.get('href'):
        #print(a.get('href') +'   '+ unicode(a.text.replace('\n', '')))
        parseUc('http://www.dns-shop.ru'+a.get('href'))


if __name__ == '__main__':
    parseCatalog(openurl('http://www.dns-shop.ru/catalog/'))
