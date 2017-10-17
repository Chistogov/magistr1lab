#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import hashlib
from lxml import etree
from lxml.html import fromstring
from requests import get

class Parse:    
    #def __init__(self):
        #self.main()

    def start(self):
        print "test"
        input_query = raw_input("Enter Query: ")
        raw = get("https://www.google.com/search?q=" + input_query).text
        page = fromstring(raw)
        #self.getTree(raw)
        parse_page = page.xpath('//*[@id="ires"]/ol/div/h3/a')   
        results = []
        for link in parse_page:
            domain = re.search("([\w\-]+\.)*([\w\-]+\.\w{2,6})", link.get("href"))
            if domain: #Зачем я тут написал IF???
                print domain.group() 
                results.append(domain.group())
        m = hashlib.md5()
        m.update(input_query)
        fileNamef = m.hexdigest()
        self.compareResults(fileNamef, results)
        #self.toFile("fileName", "results")
        
    def getTree(self, tree):
        html = etree.HTML(tree)
        result = etree.tostring(html, pretty_print=True, method="html")
        print (result) 
        
    def toFile(self, fileName, results):
        print "No Realization"
        
    def compareResults(self, fileName, results):
        try:
            file = open(fileName + '.txt')
        except IOError as e:
            print('First query, creating file...')
            with open(fileName + ".txt","w") as out:
                    for r in results:
                        out.write(r + "\n")
        else:
            print('********\nCompare results')
            with file:
                content = file.readlines()
            content = [x.strip() for x in content] 
            res = []
            for r in content:
                res.append(r)
            for r in res:   
                if results.index(r) != res.index(r):
                    print('!!!' + r)
                
      
if __name__ == "__main__":
    parse = Parse()
    parse.start()
