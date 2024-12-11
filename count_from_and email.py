# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    words = line.rstrip().split()
    if len(words) < 2 or words[0] != "From": continue
    count = count + 1
    print(words[1])
print("There were", count, "lines in the file with From as the first word")
