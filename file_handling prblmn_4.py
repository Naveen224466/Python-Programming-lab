# WAP to read the content pf file and count "a" comes in a file
f=open(r"E:\File H\ff.txt","r")
a=f.read()
print(a)
print("total 'a' occuring in file is: ",a.count("a"))