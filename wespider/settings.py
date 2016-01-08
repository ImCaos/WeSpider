<<<<<<< Updated upstream
#!/usr/bin/env python
# -*- coding=utf-8 -*-

__author__ = 'Caos'


# 测试专用
settings = {

    'userName': '',
    'password': '',
    'urls': 'http://weibo.com',
    'cookie_file': 'weibo_login_cookies.dat',
    'imageFlag': 'False',
    'fetchNum': '100'

}



class Config(dict):

    def __init__(self, names=(), values=(), **kw):
        super(self, Config).__init__(**kw)

        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise ArithmeticError(r"'Config' object has no attribute '%s' " % key)



    def __setattr__(self, key, value):
        self[key] = value
        
    def test_function():
        pass:

=======
# -*- coding: utf-8 -*-

# Scrapy settings for weibo_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'weSpider'

SPIDER_MODULES = ['wespider']
NEWSPIDER_MODULE = 'wespider'
DOWNLOAD_DELAY = 2
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weibo_spider (+http://www.yourdomain.com)'
>>>>>>> Stashed changes
