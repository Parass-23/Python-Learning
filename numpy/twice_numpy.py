import numpy as np
a=[2,3,4,5,6]
a_np=np.array(a)
b_np=a_np*2
b_np[1] += 90
print(b_np)