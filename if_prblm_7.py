'''4. Design a program in python to display the number of days left in the current year (2019), when 
today’s date is entered by the user in format of your choice.'''


m=[31,28,31,30,31,30,31,31,30,31,30,31]
d=int(input("enter date: "))
mo=int(input("enter month: ")) - 1
a= m[mo] - d 
i=mo +1 
sum=0
while i<=11:
    sum+=m[i]
    i+=1
f=sum+a
print(f)



