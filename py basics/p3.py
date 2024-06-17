import numpy as np
# print(a)
b=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print(b)
# a.ndim
# b.shape
b[1][5]=78
b[:,2]=[1,2]
print(b)
c=np.full_like(b.shape,78)
print(c)
import pandas as pd