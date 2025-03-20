import urllib.request, urllib.parse
import json, http
from icecream import ic

import ssl

# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# serviceurl = 'http://py4e-data.dr-chuck.net/json?'
# serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

while True:
    address = input('Enter location: ').strip()
    if len(address) < 1 : break

    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    # print(data)
    # print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    # ic(js)
    if not js or 'features' not in js:
        print('==== Download error ====')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break

    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('lat', lat, 'lon', lon)
    location = js['features'][0]['properties']['formatted']
    plus_code = js['features'][0]['properties']['plus_code']
    print('Plus code', plus_code)
    print(location)
 




