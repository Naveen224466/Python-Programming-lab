#6. Write a Python program to read a file line by line store it into a variable.

f=open(r"E:\FILE H\hell.txt",'r')
a=""
for i in f:
    a+=i.strip("\n")
print(a)
