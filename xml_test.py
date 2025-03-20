import xml.etree.ElementTree as ET
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

info = ET.fromstring(data)
# xml_string = ET.tostring(info, encoding="utf-8").decode("utf-8")
# print(xml_string)

counts = info.findall('.//count')


sum = 0
for count in counts:
    ic(count.text)
    if count.text is not None:
        sum += int(count.text)
print(sum)
#     count += comment['count']
# print(count)