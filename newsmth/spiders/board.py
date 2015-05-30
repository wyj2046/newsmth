# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from newsmth.items import NewsmthItem


class BoardSpider(scrapy.Spider):
    name = "board"
    allowed_domains = ["newsmth.net"]

    def __init__(self, board='Career_Upgrade', *args, **kwargs):
        super(BoardSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.newsmth.net/nForum/board/%s' % board]

    def parse(self, response):
        records = response.xpath('//tbody/tr[not(@class)]')
        for record in records:
            item = NewsmthItem()
            item['url'] = ''.join(record.xpath('td[@class="title_9"]/a/@href').extract())
            item['title'] = ''.join(record.xpath('td[@class="title_9"]/a/text()').extract())
            item['post_time'] = ''.join(record.xpath('td[@class="title_10"]/text()').extract())
            item['author'] = ''.join(record.xpath('td[@class="title_12"]/a[@class="c63f"]/text()').extract())
            yield item

        next_page = u'下一页'
        pages = response.xpath('//section[@id="body"]/div[@class="t-pre"]/div/ul/li[not(@class)]/ol/li[@class="page-normal"]/a[@title="%s"]/@href' % (next_page)).extract()
        for page in pages:
            page_url = 'http://www.newsmth.net%s' % page
            yield Request(page_url, callback=self.parse)
