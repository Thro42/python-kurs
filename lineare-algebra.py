import numpy as np

A = np.array([[5,7,14],[4,8,16],[6,10,15]])
b = np.array([20,28,65])

x = np.linalg.solve(A,b)
print(x)

#5x+7y+14z=20
#4x+8y+16z=28
#6x+10y+15z=65