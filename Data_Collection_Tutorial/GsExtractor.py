#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version: 2.0
# Original Python version: 3.0

from urllib import request
from urllib.parse import quote
from lxml import etree
import time

class GsEtractor(object):
    def _init_(self):
        self.xslt = ""

    # extract xslt from file
    def setXsltFromFile(self, xsltFilePath):
        file = open(xsltFilePath, 'r', encoding='UTF-8')
        try:
            self.xslt = file.read()
        finally:
            file.close()

    # extract xslt from string
    def setXsltFromMem(self, xsltStr):
        self.xslt = xsltStr

    # extract xslt from GooSeeker API
    def setXsltFromAPI(self, APIKey, theme, middle=None, bname=None):
        apiurl = "http://www.gooseeker.com/api/getextractor?key="+APIKey+"&theme="+quote(theme)
        if (middle)
            apiurl = apiurl + "&middle=" + quote(middle)
        if (bname):
            apiurl = apiurl + "&bname=" + quote(bname)
        apiconn = request.urlopen(apiurl)
        self.xslt = apiconn.read()

    # return xslt
    def getXslt(self):
        return self.xslt

    # given HTML DOM, extract and return result
    def extract(self, html):
        xslt_root = etree.XML(self.xslt)
        transform = etree.XSLT(xslt_root)
        result_tree = transform(html)
        return result_tree