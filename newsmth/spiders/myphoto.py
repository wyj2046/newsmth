# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from newsmth.items import MyPhotoItem


class MyphotoSpider(scrapy.Spider):
    name = "myphoto"
    allowed_domains = ["newsmth.net"]
    start_urls = (
        'http://www.newsmth.net/nForum/board/MyPhoto',
    )

    def parse(self, response):
        img_post_urls = response.xpath('//tbody/tr[not(@class)]/td[2]/samp/../a/@href').extract()
        for url in img_post_urls:
            post_url = 'http://www.newsmth.net%s' % url
            yield Request(post_url, callback=self.img_down)

        next_page = u'下一页'
        pages = response.xpath('//section[@id="body"]/div[@class="t-pre"]/div/ul/li[not(@class)]/ol/li[@class="page-normal"]/a[@title="%s"]/@href' % (next_page)).extract()
        for page in pages:
            page_url = 'http://www.newsmth.net%s' % page
            yield Request(page_url, callback=self.parse)

    def img_down(self, response):
        img_urls = response.xpath('//img[@border="0"]/@src').extract()
        item = MyPhotoItem()
        item['url'] = response.url
        item['title'] = ''.join(response.xpath('//div[@class="b-head corner"]/span[@class="n-left"]/text()').re('.*:(.*)'))
        item['image_urls'] = img_urls
        yield item
