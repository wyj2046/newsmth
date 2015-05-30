# -*- coding: utf-8 -*-
import json
import time
import codecs


class JsonPipeline(object):
    def open_spider(self, spider):
        cur_time = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
        url = spider.start_urls[0]
        board = url[url.rfind('/') + 1:]
        file_name = "%s_%s.json" % (board, cur_time)
        self.fd = codecs.open(file_name, 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.fd.write(line.decode("unicode_escape"))
        return item

    def close_spider(self, spider):
        self.fd.close()
