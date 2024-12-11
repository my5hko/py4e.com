# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
words = list()
for line in fh:
    line = line.rstrip()
    if not line.startswith("From") or line.startswith("From:") : continue
    words = line.split()
#    if len(words) == 0 or words[0] != "From": continue
    count = count + 1
    print(words[1])
print("There were", count, "lines in the file with From as the first word")
