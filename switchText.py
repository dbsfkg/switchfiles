def swapFile():
    filename=input("Enter first file name")
    filename2=input("Enter second file name")
    with open(filename,'r') as a:
     data_a = a.read()
    with open(filename2,'r') as b:
     data_b = b.read()
    with open(filename,'w') as a:
     a.write(data_b)
    with open(filename2,'w') as b:
     b.write(data_a)
swapFile()