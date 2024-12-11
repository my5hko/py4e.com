try:
    F = input("enter temp in F\n")
    C = (5/9)*(float(F)-32)
    print ("temp in C", C)
except :
    print ("temp value is not valid:", F)
