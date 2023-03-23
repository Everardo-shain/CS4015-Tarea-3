import numpy as np
a = np.array([[1, 3], [1.5, 2]])
b = np.array([300, 350])
x = np.linalg.solve(a, b)
print("Solución: \n",x)  
    
    