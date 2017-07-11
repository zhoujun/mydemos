# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib2
import requests
import re
from lxml import etree

# get ip
# url: http://www.xici.net.co/
# 因为不能通过 request 和 urlopen 打开网页，于是选择从浏览器将网页保存为 mypage.html。
f = open('mypage.html', 'r')
myPage = "".join(f.readlines())
myPage = "".join(myPage.split())
dom = etree.HTML(myPage)
x = dom.xpath('//td/text()')
x = [a.strip() for a in x]
elements = []
for a in x:
    if a != '':
        elements.append(a)

# 抓取 ip
ip = re.compile('[0-9]+.[0-9]+.[0-9]+.[0-9]+')
#port = re.compile('^[0-9]{4}$')
ip_list = []
port_list = []
flag = False
for i in elements:
    if flag :#and (re.search(port, i)):
        port_list.append(i)
        flag = False
    if (re.search(ip, i)):
        ip_list.append(i)
        flag = True



tuples = zip(ip_list, port_list)
ip_port = [t[0] + ":" + t[1] for t in tuples]
PROXIES = []
# format {'ip_port': '183.149.199.162:8998', 'user_pass': ''}
'''
for i in ip_port:
    prox = dict()
    prox['ip_port'] = i
    prox['user_pass'] = ''
    PROXIES.append(prox)
'''

# format http://host1:port
PROXIES=['http://'+i+'\n' for i in ip_port]
f=open('list.txt','w')
f.writelines(PROXIES)

print PROXIES
