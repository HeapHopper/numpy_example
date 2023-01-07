import numpy as np

a = np.arange(6)
print(a)
a2 = a[np.newaxis, :]
print(a2)
print(a2.shape)