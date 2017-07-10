# -*- coding: utf-8 -*-

"""
http://phantomjs.org/download.html
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.PhantomJS()
driver.get('http://www.baidu.com')
time.sleep(2)
print driver.page_source
# soup = BeautifulSoup(driver.page_source, 'xml')
# print soup
