''' 7. Given a non-empty array, return true if there is a place to split the array so that the sum of the numbers 
on one side is equal to the sum of the numbers on the other side.'''

a=int(input("enter length of list: "))
lst=[]
for i in range(0,a):
    lst.append(int(input("enter value:")))
for i in range(0,a):
    c=lst[:i+1]
    d=lst[i+1:]
    if sum(c)==sum(d):
        print('True')
        break
else:
    print("false")
    




    

