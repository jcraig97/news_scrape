# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Imports

import requests
from bs4 import BeautifulSoup
import os
#%% =============================================================================
# Web scraping
# =============================================================================

urls = [r'https://www.bbc.co.uk/news',
        r'https://edition.cnn.com/', 
        r'https://www.dailymail.co.uk/home/index.html',
        r'https://www.independent.co.uk/'
]


for i in urls:
    curr_dir = os.getcwd()
    r    = requests.get(i)
    soup = BeautifulSoup(r.text, 'html.parser') 
    title_ = str(soup.find('title'))
    title_ = title_[7:-8]
    f = open(curr_dir + '\webscrape_output.txt', 'a')
    f.write("{}\n".format(title_))
    f.close()



