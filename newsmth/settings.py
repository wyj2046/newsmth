# -*- coding: utf-8 -*-

# Scrapy settings for newsmth project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'newsmth'

SPIDER_MODULES = ['newsmth.spiders']
NEWSPIDER_MODULE = 'newsmth.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'newsmth (+http://www.yourdomain.com)'

DEPTH_LIMIT = 30
RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOAD_TIMEOUT = 10
RETRY_TIMES = 20
COOKIES_ENABLES = False

ITEM_PIPELINES = {
    'newsmth.json_pipeline.JsonPipeline': 300,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'newsmth.rotate_useragent.RotateUserAgentMiddleware': 400
}
