#Your task is to print a reversed Numpy array with the element type float.

import numpy as np
lst=list(map(int,input().split()))
arr=np.array(lst,dtype=float) 
print(arr[::-1])
