# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.rstrip().split()
    lst = lst + words
nodub = list()
for i in lst:
    if i in nodub : continue
    nodub.append(i)
nodub.sort()
print(nodub)
