#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import hashlib
from lxml.html import fromstring
from requests import get

class Parse:    

    def __call__(self, site):
        input_query = site
        raw = get("https://www.google.com/search?q=" + input_query).text
        page = fromstring(raw)
        parse_page = page.xpath('//*[@id="ires"]/ol/div/h3/a')   
        results = []
        for link in parse_page:
            domain = re.search("([\w\-]+\.)*([\w\-]+\.\w{2,6})", link.get("href"))
            if domain: 
                results.append(domain.group())
        m = hashlib.md5()
        m.update(input_query)
        fileNamef = m.hexdigest()
        self.compareResults(fileNamef, results)
        
    def compareResults(self, fileName, results):
        try:
            file = open(fileName + '.txt')
        except IOError as e:
            print('First query, creating file...')
            with open(fileName + ".txt","w") as out:
                    for r in results:
                        out.write(r + "\n")
        else:
            with file:
                content = file.readlines()
            content = [x.strip() for x in content] 
            res = []
            for r in content:
                res.append(r)
            for r in res:   
                if results.index(r) != res.index(r):
                    print('Site: ' + '\033[1m' + r + '\033[0m' + " was moved from the " + str(res.index(r) + 1) + " to the " + str(results.index(r) + 1))
            
if __name__ == "__main__":
    parse = Parse()("ipad")
