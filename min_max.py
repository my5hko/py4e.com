largest = None
smallest = None

while True:
    i = input ("Enter integer number:")
    if i == "done":
        break
    try:
        number = int(i)

    except:
        print ("ERROR: Not an integer number")
    if largest == None or largest < number:
        largest = number
    if smallest == None or smallest > number:
        smallest = number

print("Maximum is ", largest)
print("Minimum is ", smallest)
