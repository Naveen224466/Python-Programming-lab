#flatten and transpose of user enter n*m array


import numpy as np
n,m=list(map(int,input().split()))
a=np.zeros((n,m),int)
for i in range(n):
    a[i]=np.array(input().split(),int)
print(a.transpose())
print(a.flatten())  