'''10. Write a Python program to print the even numbers from a given list.
Sample List:[1, 2, 3, 4, 5, 6, 7, 8, 9] 
Expected Result: [2, 4, 6, 8]'''

n=int(input("enter length of string: "))
lst=[]
list=[]
for i in range(0,n):
    lst.append(int(input("enter value: ")))
for i in lst:
    if i%2==0:
        list.append(i)
print("result",list)        
