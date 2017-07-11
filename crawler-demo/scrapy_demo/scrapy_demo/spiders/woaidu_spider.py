from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from scrapy_redis.spiders import RedisSpider
from scrapy_demo.utils.select_result import list_first_item, strip_null, deduplication, clean_url
from scrapy_demo.items import WoaiduItem

class WoaiduSpider(RedisSpider):
    name = 'woaidu'
    # start_urls = ('http://www.woaidu.org/sitemap_1.html', )
    redis_key = 'woaidu-crawler:start_urls'

    def parse(self, response):
        response_selector = HtmlXPathSelector(response)
        for detail_link in response_selector.select(u'//div[contains(@class,"sousuolist")]/a/@href').extract():
            if detail_link:
                detail_link = clean_url(response.url,detail_link,response.encoding)
                yield Request(url=detail_link, callback=self.parse_detail)

    def parse_detail(self, response):
        item = WoaiduItem()

        response_selector = HtmlXPathSelector(response)
        item['book_name'] = list_first_item(response_selector.select('//div[@class="zizida"][1]/text()').extract())
        item['author'] = list_first_item(response_selector.select('//div[@class="xiaoxiao"][1]/text()').extract())[5:].strip()
        item['original_url'] = response.url

        yield item
