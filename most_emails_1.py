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
for email in emails:
    if maxnum == None or emails[email] > maxnum :
        maxmail = email
        maxnum = emails[email]
print(maxmail, maxnum)
