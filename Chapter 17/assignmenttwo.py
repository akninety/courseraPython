import urllib.request, urllib.parse, urllib.error
import json
import ssl

#Link from Dr. Chuck: https://www.py4e.com/code3/geojson.py?PHPSESSID=ee5c0cc306fd36b049ea0f8a45de09ca

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'foobar'
# I tried this but I'm getting billing account requests setting this up. Will default to the 'api_key = False' setting.
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print(json.dumps(js, indent=4))

    location = js["results"][0]["place_id"]
    print("Place ID: " + str(location))