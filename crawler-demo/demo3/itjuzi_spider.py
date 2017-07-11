# -*- coding: utf-8 -*-

from downloader import Downloader
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag

def get_newcompany(tag):
    dict_ = {}
    company_name = tag.find('p', class_="title").get_text().strip()
    cat1 = tag.find_all('p')[1].find_all('span', class_='t-small')[0].get_text().strip()
    cat2 = tag.find_all('p')[1].find_all('span', class_='t-small')[1].get_text().strip()
    created_date = tag.find('i', class_="cell date").get_text().strip()
    addr = tag.find('i', class_="cell addr").select('span > a')[0].get_text().strip()
    status = tag.find('i', class_="cell status").select('span')[0].get_text().strip()

    dict_['company_name'] = company_name
    dict_['cat1'] = cat1
    dict_['cat2'] = cat2
    dict_['created_date'] = created_date
    dict_['addr'] = addr
    dict_['status'] = status
    return dict_

def parse_itjuzi_newcompany(page=1):
    url = "http://www.itjuzi.com/company?page=%s" % page
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20"
    proxies = ""

    D = Downloader(delay=0, user_agent=user_agent, proxies=proxies, num_retries=3, cache=None)
    html, code = D(url)
    soup = BeautifulSoup(html, 'lxml')

    list_main = soup.find('ul', class_='list-main-icnset list-main-com')
    for li in list_main.children:
        if type(li) is Tag:
            dict_ = get_newcompany(li)

def get_investment(tag):
    created_date = tag.find('i', class_='cell date').get_text().strip()
    company_name = tag.find('p', class_="title").get_text().strip()

    cat = tag.find_all('p')[1].find_all('span', class_='tags t-small c-gray-aset')[0].get_text().strip()
    addr = tag.find_all('p')[1].find_all('span', class_='loca c-gray-aset t-small')[0].get_text().strip()
    round_num = tag.find('i', class_='cell round').get_text().strip()
    money = tag.find('i', class_='cell money').get_text().strip()
    investor = tag.find('i', class_='cell name').get_text().strip()

    dict_ = {}
    dict_['created_date'] = created_date
    dict_['company_name'] = company_name
    dict_['cat'] = cat
    dict_['addr'] = addr
    dict_['round_num'] = round_num
    dict_['money'] = money
    dict_['investor'] = investor
    print dict_
    return dict_

def parse_itjuzi_investments(page=1):
    url = "http://www.itjuzi.com/investevents?page=%s" % page
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20"
    proxies = ""
    D = Downloader(delay=0, user_agent=user_agent, proxies=proxies, num_retries=3, cache=None)
    html, code = D(url)
    soup = BeautifulSoup(html, 'lxml')

    list_main = soup.find_all('ul', class_='list-main-eventset')[1]
    for li in list_main.children:
        if type(li) is Tag:
            dict_ = get_investment(li)


if __name__ == "__main__":
    # parse_itjuzi_newcompany()
    parse_itjuzi_investments()



