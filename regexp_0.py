import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    
    if re.search('^From:', line) :
        print(re.findall(r'\S+@\S+', line)[0])

#        match = re.findall(r'^F.*?\@', line)
        name = re.findall('([^ ]*)@', line)
        domain = re.findall('@([^ ]*)', line)
        if name or domain:  print(name[0]); print(domain[0])
        else: print(line)
        