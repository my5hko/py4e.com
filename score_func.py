def computegrade (score):

    try :
        s = float (score)
        if s > 1.0:
            print ("Enter correct value between 0.0 and 1.0")
            grade = -1
        elif s >= 0.9:
            grade = "A"
        elif s >= 0.8:
            grade = "B"
        elif s >= 0.7:
            grade = "C"
        elif s >= 0.6:
            grade = "D"
        else:
            grade = "F"

    except:
        print ("Enter numeric value between 0.0 and 1.0")
        grade = -1
    if grade != -1:
        print("Your grade:", grade)
    return grade


s = input("Enter Score: ")
computegrade (s)
