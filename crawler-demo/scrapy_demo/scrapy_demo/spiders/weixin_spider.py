# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
from scrapy_demo.items import WeixinItem
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class WeixinSpider(scrapy.Spider):
    name = 'weixin'
    allowed_domains = ['sogou.com']
    start_urls = ['http://weixin.sogou.com/weixin?query={0}&type=2&page=1'.format('python')]

    def parse(self, response):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36"
        )
        browser = webdriver.PhantomJS(desired_capabilities=dcap)
        browser.get(response.url)
        time.sleep(4)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        browser.quit()
        news_list = soup.find('ul', class_='news-list')

        for li in news_list.find_all('li'):
            item = WeixinItem()
            item['title'] = li.find('h3').get_text().strip()
            item['des'] = li.find('p', class_='txt-info').get_text().strip()
            item['link'] = li.find('h3').find('a').get('href')
            yield item

















