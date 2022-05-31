'''You are given two integer arrays, A and B of dimensions NxM.
Your task is to perform the following operations:
1. Add (A +B )
2. Subtract ( A-B )
3. Multiply ( A*B )
4. Integer Division (A //B )
5. Mod ( A%B )
6. Power ( A**B '''

import numpy as np
n,m=list(map(int,input().split()))
a=np.zeros((n,m),int)
b=np.zeros((n,m),int)
for i in range(n):
    a[i]=np.array(input().split(),int)
for i in range(n):
    b[i]=np.array(input().split(),int) 

print("add: \n",np.add(a,b))
print("substarct: \n",np.subtract(a,b))
print("multiply: \n",np.multiply(a,b))
print("integer division: \n",np.divide(a,b))
print("power:\n ",np.power(a,b))
print("mod:\n",np.mod(a,b))
