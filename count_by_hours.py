# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)

hours = dict()
for line in fh:
    words = line.rstrip().split()
    if len(words) < 6 or words[0] != "From": continue
    time = words[5].split(":")
    hours[time[0]] = hours.get(time[0],0) + 1
#print(sorted(hours.items(), reverse=False))
sorted_hours=sorted(hours.items())
#print(sorted_hours[:5])
for hour,count in sorted(hours.items()):
#for hour,count in sorted_hours[:5]:
    print(hour, count)
