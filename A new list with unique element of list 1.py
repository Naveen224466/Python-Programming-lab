'''9. Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List: [1,2,3,3,3,3,4,5]
Unique List: [1, 2, 3, 4, 5]'''


n=int(input("enter length of list: "))
lst=[]
list=[]
for i in range(0,n):
    lst.append(int(input("enter a value: ")))
for i in range(0,n):
    if lst[i] not in lst[i+1:n]:
        list.append(lst[i])
print("not repeated value list: ",list)        
