# -*- coding: utf-8 -*-

from scrapy_demo.items import ItjuziItem
from scrapy.spider import BaseSpider
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class ItjuziSpider(BaseSpider):

    name = 'itjuzi'

    allowed_domains = ['itjuzi.com']
    start_urls = ['http://www.itjuzi.com/company?page={0}'.format(1)]

    def parse(self, response):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20"
        )
        browser = webdriver.PhantomJS(desired_capabilities=dcap)
        print 'url', response.url
        browser.get(response.url)
        time.sleep(4)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        browser.quit()
        list_main = soup.find('ul', class_='list-main-icnset list-main-com')

        for li in list_main.find_all('li'):

            company_name = li.find('p', class_="title").get_text().strip()
            cat1 = li.find_all('p')[1].find_all('span', class_='t-small')[0].get_text().strip()
            cat2 = li.find_all('p')[1].find_all('span', class_='t-small')[1].get_text().strip()
            created_date = li.find('i', class_="cell date").get_text().strip()
            addr = li.find('i', class_="cell addr").select('span > a')[0].get_text().strip()
            status = li.find('i', class_="cell status").select('span')[0].get_text().strip()

            item = ItjuziItem()
            item['company_name'] = company_name
            item['cat1'] = cat1
            item['cat2'] = cat2
            item['created_date'] = created_date
            item['addr'] = addr
            item['status'] = status
            yield item





























