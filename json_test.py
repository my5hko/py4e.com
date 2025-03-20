import json
import urllib.request
from icecream import ic
import ssl

# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

info = json.loads(data)
ic(info)

count = 0
for comment in info['comments']:
    count += comment['count']
print(count)