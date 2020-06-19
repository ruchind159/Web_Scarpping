#sample json http://py4e-data.dr-chuck.net/comments_42.json
#test json http://py4e-data.dr-chuck.net/comments_682949.json
import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Url: ")
data = urllib.request.urlopen(url, context=ctx).read()

info = json.loads(data)
tot=0
for i in range(len(info['comments'])):
  tot+=int(info['comments'][i]['count'])

print(tot)
# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])