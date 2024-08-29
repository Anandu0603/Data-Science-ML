import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
print(a)
U,s,VT=np.linalg.svd(a)
print("left singular matrix")
print(U)
print("singular matrix")
print(s)
print("right singular matrix")
print(VT)
sigma=np.zeros((a.shape[0],a.shape[1]))
np.fill_diagonal(sigma,s)
B=U.dot(sigma.dot(VT))
print("reconstructed matrix:\n",B)


OUTPUT



[9.52551809 0.51430058]
right singular matrix
[[-0.61962948 -0.78489445]
 [-0.78489445  0.61962948]]
reconstructed matrix:
 [[1. 2.]
 [3. 4.]
 [5. 6.]]

