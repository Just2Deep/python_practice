# numpy module in python
# essential for datascience, machine learning, deep learning.
"""" 
numpy uses nd arrays for faster access as it is written in C
usecases.
1. Array/Matrix operations - Linear Algebra
2. Dot Product
3. Matrix multiplications
4. Linear systems.
5. Inverse, determinant
6. Eigen Vectors
7. Random numbers
8. Working with images represented as array

pip install numpy
"""
from timeit import default_timer as timer
import numpy as np

print(np.__version__)

a = np.array([1, 2, 3])
print(f'a = {a}')
print(f'a.shape = {a.shape}')
print(f'a.dtype = {a.dtype}')
print(f'a.ndim = {a.ndim}')  # dimension of array
print(f'a.size = {a.size}')  # total elements
print(f'a.itemsize = {a.itemsize}')  # bytes of elements
print(f'a[0] = {a[0]}')

a[0] = 12
print(f'a[0] = {a[0]}')

# multiplication
print(f'a = {a}')
b = a * np.array([2, 0, 2])
print(f'b = {b}')


# list and numpy array look similar but are different
l = [1, 2, 3]
c = np.array([1, 2, 3])
print(f'l = {l}, c = {c}')

# operations are element wise
d = c * 2
print(f'd = {d}')
print(np.sqrt(d))  # square root
print(np.log(d))  # log

# dot product
# using lists

l1 = [1, 2, 3]
l2 = [4, 5, 6]
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(f'dot = {dot}')

dot = np.dot(a1, a2)
print(f'dot = {dot}')

# sum1 = a1*a2
# dot = np.sum(sum1)
# print(dot)

dot = a1 @ a2
print(f'dot = {dot}')


# checking the time for lists and numpy arrays


a = np.random.randn(1000)
b = np.random.randn(1000)

A = list(a)
B = list(b)

T = 1000


def dot1():
    dot = 0
    for i in range(len(A)):
        dot += A[i] * B[i]
    return dot


def dot2():
    return np.dot(a, b)


start = timer()

for i in range(T):
    dot1()

stop = timer()
t1 = stop - start

start = timer()

for i in range(T):
    dot2()

stop = timer()
t2 = stop - start

print(f'The time taken by lists: {t1}')
print(f'The time taken by arrays: {t2}')
print(f'ratio of lists/arrays: {t1/t2}')

# multi dimensional arrays

a = np.array([[1, 2, 6], [3, 7, 4], [5, 8, 2]])
print(a.shape)
print(a[0][1])  # or we can use a[0,1]
print(a)
print(a[:, 0])  # printing first column
print(a[0, :])  # printing first row

# transpose
print(a.T)

# inverse
print(np.linalg.inv(a))

# determinant
print(np.linalg.det(a))

# diagonal elements
print(np.diag(a))

# making diagonal matrix from elements
c = np.diag(a)
print(np.diag(c))

# slicing the arrays

# if we need only 1 row
print(a)
print(a[0:2, :])

# if we need only 1 or 2 col
print(a[:, 0:2])


# creating boolean indices for our condition to each element
bool_idx = a > 4
print(bool_idx)

# if we need elements only for which conditions are matching
print(a[bool_idx])
# or
print(a[a > 4])

# to retain matrix shape and return only elements satisying the condition
b = np.where(a > 3, a, 0)
print(b)


# printing elements based on indices of another list
a = np.array([10, 20, 12, 34, 5, 46, 231, 56])
print(a)
b = [1, 3, 5]
print(b)
print(a[b])

# finding like a even numbers
even = np.argwhere(a % 2 == 0).flatten()
print(a[even])
