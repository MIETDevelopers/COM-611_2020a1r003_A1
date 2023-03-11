import numpy
from scipy import linalg   #arrays and linear algebra, less memory consumption
a=numpy.array([[1,2,3],[4,5,6]])
b=numpy.array([[7,8,9],[11,12,13]])
y=numpy.arange(2)
z=a-b
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a[0])
print(a[-1])
print(y)
print(z)
print(a.mean())
print(a.sum())
x=numpy.cos(a)
print(x)
#table list datatypes and re-shape it into 2-D as well as 3-D matrix using numpy library ._.
#                                                                                         0