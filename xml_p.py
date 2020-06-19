import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Url: ")
data = urllib.request.urlopen(url, context=ctx).read()

#print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)
tot=0
counts = tree.findall('.//count')
for count in counts:
    tot+=int(count.text)
print(tot)
# results = tree.findall('result')
# lat = results[0].find('geometry').find('location').find('lat').text
# lng = results[0].find('geometry').find('location').find('lng').text
# location = results[0].find('formatted_address').text

# print('lat', lat, 'lng', lng)
# print(location)