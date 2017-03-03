import urllib.request
from bs4 import *
import re
# prompt to input the URL
url = input('Enter URL: - http://www.github.com or some such thing\n')
# if you bot a "expected a byte like object ..." error, put a b in front of this and
# try
html = urllib.request.urlopen(url).read()  # reads the page (all of it) as well
soup = BeautifulSoup(html, 'html.parser')

#tags = soup('a')
tags = soup('span')

myRE = re.compile(r'\d+')
mySum = 0
myCount = 0
for tag in tags:
    tmpList = myRE.findall(tag.string)
    myCount += 1
    if tmpList:
        tmpList = [int(x) for x in tmpList]
        mySum += sum(tmpList)

print('Count {0}'.format(myCount))
print('Sum {0}'.format(mySum))
    #print(tag)   #.get('href', None)
