import urllib.request, urllib.parse, urllib.error
import json
from icecream import ic

import ssl

# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# serviceurl = 'http://py4e-data.dr-chuck.net/json?'
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
# serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'address': address, 'key' : 'AIzaSyDOGa10OyuqxdFhUnjL9dj9H8cqEwLrTQQ'})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    # print(data)
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    # ic(js)
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng'] 
    full_address = js['results'][0]['formatted_address']
    ic(full_address, lat, lng)





