import numpy as np
A = np.array([[1, 2, 3],
              [3, 6, 9]])
rank = np.linalg.matrix_rank(A)
print("The rank of the matrix is:", rank)
