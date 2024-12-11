# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
datetimes = list()
datehours =list()
hours = dict()
for line in fh:
    words = line.rstrip().split()
    if len(words) < 6 or words[0] != "From": continue
    time = words[5].split(":")
    date = words[3] + " " + words[4]
    datetime = [date, time[0]]
    datehour = [date + " " + time[0]]
    datetimes.append(datetime)
    datehours.append(datehour)

print(datetimes)
print(datehours)
dates = dict()

for datetime in datetimes:
    dates[datetime[0]] = dates.get(datetime[0],0) + 1
    hours[datetime[1]] = hours.get(datetime[1],0) + 1

datehours_d = dict()
for datehour in datehours:
    datehours_d[datehour[0]] = datehours_d.get(datehour[0],0) + 1
#        print(date)

#    for date in datetimes:
#        print(date)
#        hours[datetime[2]] = hours.get(datetime[2],0) + 1

print(dates)
print(hours)
print(datehours_d)
#print(datehours)
#print(sorted(hours.items(), reverse=False))
#sorted_hours=sorted(hours.items())
#print(sorted_hours[:5])
#for hour,count in sorted(hours.items()):
#for hour,count in sorted_hours[:5]:
#    print(hour, count)
