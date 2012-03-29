AZ Job Scraper
==============

This is a simple tool written in Python showing how a job site that only supports queries using POST can be scraped. Unfortunately,
the results are returned in HTML format with sections only identified by CSS classes so we have to do some work to get the data
we need. Once we have the data we use a jinja2 template to output in the JSON format required. There are probably libraries
that will do this automatically but this is simple for non-developer to tweak.

[Requests](http://docs.python-requests.org) is used to pull down results from the site, and
[BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) is used to extract useful parts from the document.

It is best to use a [virtualenv](http://www.virtualenv.org/en/latest/index.html) for managing dependencies. Anyone who
already knows about this tool shouldn't have a problem with the running this.

Dependencies on Linux
---------------------

Open a terminal or SSH into a remote machine as root, or with an account that can is member of the sudoers group. On
many machines you can execute pip immediately. If it is not installed then get it using easy_install:

    easy_install pip (if you are root) or sudo easy_install pip (if you need sudo)

Next install the dependencies using pip:

    sudo pip install requests
    sudo pip install beautifulsoup4
    sudo pip install jinja2

Dependencies on Windows
-----------------------
Open an administrator command prompt. Run easy_install to check if it is configured.

Install pip by executing the following command if you don't have pip already:

    easy_install pip

Next install the dependencies using pip:

    pip install requests
    pip install beautifulsoup4
    pip install jinja2

Usage
-----

To return output to the console run:

    python jobs.py

To output to a file execute:

    python jobs.py > output.json

Neither of these options is very good for handling non-ASCII pages so a future update will fix that and allow you
specify an output file without going through the console.