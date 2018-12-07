#!/usr/bin/python
#coding:gbk

import xml.sax

class MovieHandle(xml.sax.ContentHandle):
    def __init__(self):
        self.CurrentData = ''
        self.type = ''
        self.format = ''
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # Ԫ�ؿ�ʼ�¼�����
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("*****Movie*****")
            title = attributes["title"]
            print("Title:" + title )
