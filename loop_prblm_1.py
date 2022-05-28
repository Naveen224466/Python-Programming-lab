#1. Program to find whether an entered number is prime or not.

#method:-1
'''n=int(input("enter a number: "))
i=2
while i<n:
    if n%i==0:
        print("not prime")
        break
    i+=1    
else:
    print("prime")  '''


#method:-2
n=int(input("enter a number: "))
a=range(2,n)
count=0
for i in a:
    if n%2==0:
        count+=1
if count==0:
    print("enter number is prime number.")

else:
    print("enter number is not prime number.")    

