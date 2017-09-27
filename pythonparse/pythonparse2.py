#! /usr/bin/env python
# -*- coding: utf-8 -*-

#google api key: AIzaSyALXbsofvWtVsM8rjO9xMyUWZezrB7oD5g


import hashlib
from lxml import etree
from googleapiclient.discovery import build


class Parse:    
    #def __init__(self):
        #self.main()
        
    def start(self):
        print "Hello, can I help you?"
        input_query = raw_input("Enter Query: ")        
        results = self.google_results(input_query)
        m = hashlib.md5()
        m.update(input_query)
        fileNamef = m.hexdigest()
        self.compareResults(fileNamef, results)
        #self.toFile("fileName", "results")
        print "Success"

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
            marker = False
            for r in res:   
                if results.index(r) != res.index(r):
                    marker = True
                    print('Site: ' + '\033[1m' + r + '\033[0m' + " was moved from the " + str(res.index(r) + 1) + " to the " + str(results.index(r) + 1))
            if marker == True:
                q = raw_input("Overwrite the file? (Y/N)")
                if q == 'Y' or q == 'y':
                    with open(fileName + ".txt","w") as out:                    
                        out.seek(0)
                        out.truncate()
                        for r in results:
                                out.write(r + "\n")
            else:
                print 'No changes'
                        
    def google_results(self, query):
        service = build("customsearch", "v1",
                        developerKey="AIzaSyALXbsofvWtVsM8rjO9xMyUWZezrB7oD5g")

        result = service.cse().list(
                q=query,
                cx='005832402539986471586:kovn4gg0rck'
            ).execute()
        results = []
        for channel in result["items"]:
            results.append(channel["link"])
        return results
    
if __name__ == "__main__":
    parse = Parse()
    parse.start()
    
