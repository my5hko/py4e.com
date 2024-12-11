# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh :
    line_up = line.rstrip().upper()
    print(line_up)
