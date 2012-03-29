AZ Job Scraper
==============

This is a simple tool written in Python showing how a job site that only supports queries using POST. Unfortunately, the
results are returned in HTML format with sections only identified by CSS classes. The BeautifulSoup parser is used to
extract these sections.

Dependencies on Linux
---------------------

Open a terminal or SSH into a remote machine as root, or with an account that can is member of the sudoers group. On most
machines you can execute pip directly. If it is not installed then get it using easy_install:

    easy_install pip (if you are root) or sudo easy_install pip (if you need sudo)

Next install the dependencies using pip:

    sudo pip install requests
    sudo pip install beautifulsoup4
    sudo pip install jinja2

Dependencies on Windows
-----------------------
Open an administrator command prompt. Run easy_install to check if it is configured.

Install pip by executing the following command:

    easy_install pip

Next install the dependencies using pip:

    pip install requests
    pip install beautifulsoup4
    pip install jinja2