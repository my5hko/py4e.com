# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
sum = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
#    if not line.startswith("X-DSPAM-Confidence:"):
#        continue
        pos = line.find(":")
        num = float(line[pos+2:].lstrip())
        sum = sum + num
        count = count + 1
avg = sum/count
print("Average spam confidence: ", avg)
