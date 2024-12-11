# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
emails = dict()
for line in fh:
    words = line.rstrip().split()
    if len(words) < 2 or words[0] != "From": continue
    emails[words[1]] = emails.get(words[1],0) + 1
maxnum = None
for email,count in emails.items():
    if maxnum == None or count > maxnum :
        maxmail = email
        maxnum = count
print(maxmail, maxnum)
