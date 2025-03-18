import urllib.request, urllib.parse, urllib.error
from icecream import ic
from bs4 import BeautifulSoup
import ssl

# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

ic(soup)

tags = soup('span')
ic(tags)

sum = 0
for tag in tags:
    # print(tag.get('href', None)) # type: ignore
    print('Contents:', tag.contents[0]) # type: ignore
    # print('Attr:', tag.attrs) # type: ignore
    # print(tag.get('class', None))
    sum += int(tag.contents[0]) # type: ignore
print(sum)