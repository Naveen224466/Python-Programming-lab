#You are given a space separated list of nine integers. Your task is to convert this list into 3x3 numpy array.


import numpy as np
lst=list(map(int,input().split()))
ar=np.array(lst)
ar.shape=3,3 #also use ar.reshape(3,3)
print(ar)