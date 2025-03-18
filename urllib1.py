import urllib.request, urllib.parse, urllib.error
from icecream import ic

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
ic(fhand)
count = dict()
for line in fhand:
    words = line.decode().strip()
    print(words)
    for word in words.split():
        count[word] = count.get(word, 0) + 1
ic(count)

