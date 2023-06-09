import numpy as np
import sys

# Reading number of unknowns
n = int(input('Enter number of unknowns: '))

# Making numpy array of n x n+1 size and initializing 
# to zero for storing augmented matrix
a = np.zeros((n,n+1))

# Making numpy array of n size and initializing 
# to zero for storing solution vector
x = np.zeros(n)

# Reading augmented matrix coefficients
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))
print("Ax = b: \n",a)
D=np.delete(a, n, 1)
delta = np.linalg.det(D)
for k in range(n):
    Dk=np.matrix.copy(D);
    Dk[:, k] =  a[:, n]
    x = np.linalg.det(Dk)/delta
    print("x"+str(k+1)+":\n",round(x,3))
    
    
    