
#3. Program to find the sum of digits of an entered number.

#METHOD=1

'''n=input("enter a number: ")
a=len(n)
sum=0
i=0
while i<a:
    sum+=(int(n[i]))
    i+=1
print(sum)   




#METHOD=2

n=int(input("enter a number: "))
sum=0
while n>0:
    a = n%10
    sum+=a
    n//=10

print(sum)    '''


#Method 3
n=input("enter a number : ")
s=0
for i in n:
    s+=int(i)

print(f"sum of digit is {s}")    


       







