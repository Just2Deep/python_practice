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

# arange in numpy

a = np.arange(1, 7)
print(a)
print(a.shape)
b = a.reshape(2, 3)
print(b)

c = a[np.newaxis, :]
print(c)
print(c.shape)

d = a[:, np.newaxis]
print(d)
print(d.shape)


# concatenation

a = np.array([[1, 2], [3, 4]])
print(a)
b = np.array([[5, 6]])

c = np.concatenate((a, b.T), axis=1)
print(c)

# hstack & vstack

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

c = np.vstack((a, b))
d = np.hstack((a, b))
print(c, d)

# array and vector

x = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6]])
a = np.array([1, 0, 1])

print(x)
print(x+a)

# datascience important things

a = np.array([[7, 8, 9, 10, 11, 12, 13], [17, 181, 19, 20, 21, 22, 23]])
print(a)
print(a.sum(axis=1))
print(a.sum(axis=0))
print(a.sum(axis=None))


# setting data types

x = np.array([1.0, 2.0], dtype=np.int32)
print(x)
print(x.dtype)

# copying arrays

a = np.array([1, 2, 3])
b = a.copy()
b[0] = 42
print(a, b)

# generating arrays
a = np.zeros((2, 3))
print(a)

b = np.ones((2, 3))
print(b)

a = np.full((2, 3), 5.0)
print(a)

a = np.eye(3)
print(a)

b = np.arange(20)
print(b)

c = np.linspace(0, 10, 5)
print(c)

# random numbers

a = np.random.random((3, 2))  # (0-1)
print(a)

a = np.random.random(1000)  # normal/gaussian
print(a.mean(), a.var())

a = np.random.randint(1, 10, size=(3, 3))
print(a)

a = np.random.choice([-8, -2, -5, 1, 5], size=10)
print(a)


# linalg modules
# eigen values

a = np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = np.linalg.eig(a)

print(eigenvalues)
print(eigenvectors)  # column vector

b = eigenvectors[:, 0] * eigenvalues[0]
print(b)

c = a @ eigenvectors[:, 0]
print(c)

print(np.allclose(b, c))


# solving linear algebra
# x1 + x2 = 2200
# 1.5x1 + 4x2 = 5050

# A = ([1 1], [1.5 4]) b = ([2200 5050])
# Ax = b == x = A^-1 b

A = np.array([[1, 1], [1.5, 4.0]])
b = np.array([2200, 5050])

x = np.linalg.inv(A).dot(b)
print(x)


# alternate method
x = np.linalg.solve(A, b)
print(x)

# loading data from csv
#np.loadtxt, np.genfromtxt

#data = np.loadtxt('filename.csv', delimiter=',', dtype=np.float32)
#data = np.genfromtxt('filename.csv', delimiter=',', dtype=np.float32)
