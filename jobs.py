#!/usr/bin/env python
import requests

payload = {
    'search-type': 'category',
    'sort-type': 'date',
    'country-id': '',
    'location-id': '',
    'category-id': '16,50',
    'city-id=': '',
    'results_hid': ''
}

headers = {
    'Referer': 'http://jobs.astrazeneca.com/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Accept-Encoding': 'gzip, deflate',
    'Pragma': 'no-cache',
    'Accept-Language': 'Accept-Language'
}

r = requests.post("http://jobs.astrazeneca.com/results", headers)
html = unicode(r.text).encode("utf-8")

#print html


from bs4 import BeautifulSoup
soup = BeautifulSoup(html)

result_count = soup.findAll('div', { "class" : "results_heading" })
print 'Result Count Soup'
print result_count

postings = soup.findAll('div', { "class": "results_list_item"})
print len(postings)

for posting in postings:
    print posting.findAll('div', { "class": "results_list_details"})
