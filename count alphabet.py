#to find no. alphabets in given string.
a=input("enter string: ")
count=0
for i in range(0,len(a)):
    if a[i].isalpha():
        count+=1
print(count)

