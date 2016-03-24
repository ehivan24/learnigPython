
from bs4 import BeautifulSoup
import urllib2
import os

import unicodedata
import re 

print "look for: "
x = raw_input().title()


lookFor = re.sub(' ', '_', x)

readFile = urllib2.urlopen("http://en.wikipedia.org/wiki/%s" % (lookFor))
readHtml = readFile.read()
readFile.close()

soup = BeautifulSoup(readHtml)

all = soup.find('p').getText()

newS = unicodedata.normalize('NFKD', all).encode('ascii', 'replace' )


newS = re.sub('[^0-9a-zA-Z \,\. \- \_]+',' ', newS)

string = str("say According to Wikipedia " + newS)
print string

os.system(string)

