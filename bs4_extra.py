from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


count=7
pos=18
tags=soup('a')
for i in range (0,count):
	print('Contents:', tags[pos-1].contents[0])
	url=tags[pos-1].get('href',None)
	html = urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, "html.parser")
	tags=soup('a')

# Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     # Look at the parts of a tag
#     #print('TAG:', tag)
#     #print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     #print('Attrs:', tag.attrs)
