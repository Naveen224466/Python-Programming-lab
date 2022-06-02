'''write a python program to merge the two list in to a list of tuples(pair of similar index).(don't use Zip() function)
sample input       sample output
[2,6,8,9]            [(2,3),(6,0),(8,7),(9,1)]
[3,0,7,1]                                    '''

n=int(input("enter length: "))
a,b,c=[],[],[]
for i in range(0,n):
    a.append(int(input("enter list1 value: ")))
for i in range(0,n):
    b.append(int(input("enetr list2 value: ")))
for i in range(0,n):
    c.append((a[i],b[i]))      
print(c)      
