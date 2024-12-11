sum = 0
count = 0
while True:
    i = input ("Enter number:")
    if i == "Done":
        break
    try:
        number = float(i)
        sum = sum + number
        count = count + 1

    except:
        print ("ERROR: Not a number")
try:
    avg = sum/count
    print (sum, count, avg)

except:
    print (sum, count, 0)
