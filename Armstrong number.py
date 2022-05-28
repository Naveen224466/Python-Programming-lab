#4. Program to find the series of all three digits Armstrong numbers.
'''i=int(input("enter a number : "))
a=i
sum=0
while i>0:
    b=i%10
    sum += b**3
    i//=10
if a==sum:
    print(a,"is armstrong number")'''



d=int(input("enter digit you want: "))
for i in range(10**(d-1) , 10**d):
    a=i 
    sum=0
    while i>0:
        b=i%10
        sum+=b**d
        i//=10
    if a==sum:
        print(a)        



    