# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pysqlite2 import dbapi2 as sqlite
from os import path
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher

class DmozPipeline(object):

    def process_item(self, item, spider):
        conn = sqlite.connect("dmoz.db")
        cur = conn.cursor()
        cur.execute("drop table if exists dmoz ")
        cur.execute("create table dmoz(id integer primary key autoincrement,title text,link text,desc text) ")
        cur.execute('insert into dmoz values(?,?,?,?)',(None,item['title'][0],item['link'][0],item['desc'][0]))
        cur.execute('select * from dmoz')
        rs = cur.fetchall()
        print rs
        cur.close()
        conn.close()
        return item
