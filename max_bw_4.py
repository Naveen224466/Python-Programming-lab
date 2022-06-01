x=int(input("enter the no"))
y=int(input("enter the no"))
z=int(input("enter the no"))
w=int(input("enter the no"))
if(x>y and x>z and x>w):
    print('x ia maximum')
elif(y>x and y>z and y>w):
    print('y is maximum')
elif(z>x and z>y and z>w):
    print('z is maximum')
else:
    print('w is maximum')