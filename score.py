score = input("Enter Score: ")
try :
    s = float (score)
    if s >= 1.0:
        print ("Enter correct value between 0.0 and 1.0")
    elif s >= 0.9:
        print ("A")
    elif s >= 0.8:
        print ("B")
    elif s >= 0.7:
        print ("C")
    elif s >= 0.6:
        print ("D")
    else:
        print ("F")

except:
    print ("Enter numeric value between 0.0 and 1.0")
