#!/usr/bin/env python
import re
import requests

from bs4 import BeautifulSoup
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader

def utf8_html(text):
    """FIXME: Unicodeycorns"""
    return unicode(text).encode("utf-8")

def render_template(data, template_name, filters=None):
    """Render data using a jinja2 template"""
    env = Environment(loader=FileSystemLoader('/home/brianly/sites/blweb/jobscrape/'))

    if filters is not None:
        for key, value in filters.iteritems():
            env.filters[key] = value

    template = env.get_template(template_name)

    return template.render(jobs=data).encode('utf-8')

def get_description(url):
    """Fetch the details for a job posting"""
    r = requests.get(url)
    html = utf8_html(r.text)

    soup = BeautifulSoup(html)
    description = soup.findAll('div', { "class": "job_description"})

    return description[0]


headers = {
    'Referer': 'http://jobs.astrazeneca.com/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Accept-Encoding': 'gzip, deflate',
    'Pragma': 'no-cache',
    'Accept-Language': 'en-US',
    'Content-Length': '102',
    'Proxy-Connection': 'Keep-Alive',
    'Host': 'jobs.astrazeneca.com',
}

payload = {
    'search-type': 'category',
    'sort-type': 'date',
    'country-id': '',
    'location-id': '',
    'category-id': '16,50',
    'city-id=': '',
    'results_hid': '30'
}

r = requests.post("http://jobs.astrazeneca.com/results", data=payload, headers=headers)
html = utf8_html(r.text)

soup = BeautifulSoup(html)

result_count = soup.findAll('div', { "class" : "results_heading" })
print 'There are %s total postings' % result_count[0].find('span').getText()

postings = soup.findAll('div', { "class": "results_list_item"})
print 'There are %s postings on this page' % len(postings)

jobs = []

for posting in postings:
    # Find the job listing date
    results_list_date = posting.find('div', {"class": "results_list_date"})

    # Find the job number
    job_number = posting.find('div', {"class": "job_number"})

    # Find the title
    job_info = posting.find('div', {"class": "job_info"})
    job_title = posting.find('h2')

    # Use title to get URL to description
    job_url = job_title.find('a')
    job_description = get_description(job_url['href'])

    full_desc = unicode(get_description(job_url['href']))

    full_desc = full_desc.replace('<div class="job_description">\n', '<div><p>')
    full_desc = full_desc.replace('<div style="font-size:4px">', '<div>')
    full_desc = re.sub('<div>\s(.*)\s</div>', '', full_desc)
    full_desc = full_desc.replace(u'<div>\xa0</div>', '</p></p>')
    full_desc = full_desc.replace("</div>", "</p></div>")
    full_desc = full_desc.replace("* ", "<br />* ")

    job = {
        'date': results_list_date.getText().strip(),
        'number': job_number.getText().strip(),
        'title': job_title.getText().strip(),
        'description': full_desc,
        'url': unicode(job_url['href'])
    }

    # job['description'] = job['description'].replace("<div style=\"font-size:4px\"> </div>", "</p><p>")

    jobs.append(job)

result = render_template(jobs, 'job.tmpl')

with open('/home/brianly/sites/blweb/www/downloads/parker/jobs.json', 'w') as output:
    output.write(result)
