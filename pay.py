def computepay (hours, rate):

    print ("Calcualte pay:", hours, rate)
    if hours > 40:
        reg = 40*rate
        over = (hours - 40)*(rate*1.5)
        pay = reg + over
        print ("Regular:", reg)
        print ("Overtime:", over)
        print ("Payment:", pay)
    else:
        pay = hours*rate
        print ("Regular:", pay)
        print ("Overtime: -")
        print ("Payment:", pay)
    return pay

h = float(input ("Enter hours: "))
r = float(input ("Enter rate: "))

computepay (h, r)
