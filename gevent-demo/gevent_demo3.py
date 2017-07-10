# -*- coding: utf-8 -*-

import requests
import gevent
from gevent import monkey, pool
monkey.patch_all()

jobs = []
p = pool.Pool(10)

urls = [
    'http://www.baidu.com',
    # ... another 100 urls
]

def get_links(url):
    r = requests.get(url)
    if r.status_code == 200:
        print r.text.encode('utf-8')

for url in urls:
    jobs.append(p.spawn(get_links, url))
gevent.joinall(jobs)
