#Your task is to print an array of size NxM with its main diagonal elements as 1’s and 0’s everywhere else.


import numpy as np
lst=list(map(int,input().strip().split()))
r,c=lst[0],lst[1]
ar=np.eye(r,c)
print(ar)
