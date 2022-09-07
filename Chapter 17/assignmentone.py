import urllib
import json
import ssl
from urllib.request import urlopen

#https://www.py4e.com/code3/geojson.py
#Worked example linked above.

serviceurl = "http://py4e-data.dr-chuck.net/comments_1508339.json"
print("Retrieving the following URL: " + serviceurl)

with urlopen(serviceurl) as url:
    s = url.read()

json = json.loads(s)
#print(json)

count = 0
i = 0

for params in json["comments"]:
    num = int(params["count"])
    count = num + count
    i = i + 1

print("Count: " + str(i))
print("Sum: " + str(count))