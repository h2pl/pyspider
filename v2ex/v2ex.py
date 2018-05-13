#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-08-17 11:11:46
# Project: v2ex

from pyspider.libs.base_handler import *
import random
import MySQLdb




class Handler(BaseHandler):
    crawl_config = {
    }
    
    def __init__(self):
        self.db = MySQLdb.connect('localhost', 'root', '1234', 'wenda', charset='utf8')
    
    def add_question(self, title, content):
        try:
            cursor = self.db.cursor()
            sql = 'insert into question(title, content, user_id, created_date, comment_count) values ("%s","%s",%d, %s, 0)' % (title, content, random.randint(1, 10) , 'now()');
            print sql
            cursor.execute(sql)
            self.db.commit()
        except Exception, e:
            print e
            self.db.rollback()

    #首先进入首页
    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://v2ex.com', callback=self.index_page, validate_cert=False)

    #然后爬取标签tab，比如技术，生活，url是?tab=*
    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="https://www.v2ex.com/?tab="]').items():
            self.crawl(each.attr.href, callback=self.tab_page, validate_cert=False)

    # 爬取子节点，比如技术下的程序员，java等，url是go开头
    @config(age=10 * 24 * 60 * 60)
    def tab_page(self, response):
        for each in response.doc('a[href^="https://www.v2ex.com/go/"]').items():
            self.crawl(each.attr.href, callback=self.board_page, validate_cert=False)

    # 爬取子节点下的每篇文章。url都是t开头
    @config(priority=2)
    def board_page(self, response):
        for each in response.doc('a[href^="https://www.v2ex.com/t/"]').items():
            url = each.attr.href
            # 此处过滤url中的回复编号，防止重复爬取
            if url.find('#reply') > 0:
                url = url[0:url.find('#')]
            self.crawl(url, callback=self.detail_page, validate_cert=False)
        # 获取相同节点下不同页的文章页面
        for each in response.doc('a.page_normal').items():
            self.crawl(each.attr.href, callback=self.board_page, validate_cert=False)

    # 已经到最后的节点：文章，直接获取标题，url，以及内容，存到数据库
    @config(priority=20)
    def detail_page(self, response):
        title = response.doc('h1').text()
        content = response.doc('div.topic_content').html()
        self.add_question(title, content)
        return {
            'url': response.url,
            'title': title,
            'content': content
        }

