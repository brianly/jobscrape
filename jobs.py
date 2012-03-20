#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

def get_description(url):
    """Fetch the details for a job posting"""
    r = requests.get(url)
    html = unicode(r.text).encode("utf-8")

    soup = BeautifulSoup(html)
    description = soup.findAll('div', { "class": "job_description"})

    return description[0].getText().strip()


headers = {
    'Referer': 'http://jobs.astrazeneca.com/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Accept-Encoding': 'gzip, deflate',
    'Pragma': 'no-cache',
    'Accept-Language': 'Accept-Language'
}

payload = {
    'search-type': 'category',
    'sort-type': 'date',
    'country-id': '',
    'location-id': '',
    'category-id': '16,50',
    'city-id=': '',
    'results_hid': ''
}

r = requests.post("http://jobs.astrazeneca.com/results", headers)
html = unicode(r.text).encode("utf-8")

soup = BeautifulSoup(html)

result_count = soup.findAll('div', { "class" : "results_heading" })
print 'There are %s total postings' % result_count[0].find('span').getText()

postings = soup.findAll('div', { "class": "results_list_item"})
print 'There are %s postings on this page' % len(postings)

print

for posting in postings:
    results_list_date = posting.find('div', {"class": "results_list_date"})
    print results_list_date.getText().strip()

    job_number = posting.find('div', {"class": "job_number"})
    print job_number.getText().strip()

    job_info = posting.find('div', {"class": "job_info"})
    job_title = posting.find('h2')
    print job_title.getText().strip()

    job_url = job_title.find('a')
    print job_url['href']

    job_description = get_description(job_url['href'])
    print job_description

    print
    print '~~~~~~~~~~~~~'
    print

