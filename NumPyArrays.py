import numpy as np

# Create a matrix
x = np.array([[1,2,4.5], [3.14,4, 4.3]])
y = np.array([[1,2.5, 2.71828],[3,4, 7.6]])

# Create a vector
u = np.array([1,2,3])
w = np.array([4,5,6])

# Sum of matrices
z = x + y

# Sum of vector
v = u + w

# Print number of dimensions in each array
print(f"a matrix is a {x.ndim}-dimensional array")
print(f"a vector is a {u.ndim}-dimensional array\n")

# Print results of sums of arrays
print(z)
print(v)

# Print data type of both arrays
print(f"\nthe matrix contains {z.dtype}")
print(f"the vector contains {v.dtype}")

print(f"\nmatrix shape (nrow, ncol): {z.shape}")
print(f"vector shape (nrow, ncol): {v.shape}")

j = np.array([1,2,3,4,5,6,])
j_sum = j.sum()
print(f"\nSum of all numbers from 1-6 inclusive is {j_sum}")

# Reshaping vector into a matrix
# Numpy follows row-major ordering
print('beginning j: \n', j)
j_reshape = j.reshape((2,3))
print("reshaped j:\n", j_reshape)

# Accessing the top left element of j_reshape
print(j_reshape[0][0])

# Accessing the element in the 2nd row and 3rd column
print(j_reshape[1][2])

# Modifying the matrix
j_reshape[0][0] = 6
j_reshape[1][2] = 1

print(j_reshape)

# Creating a tuple
t = (1,2,3)
print(f"You can access an index in a tuple such as {t}, but you can not modify it's elements.\nThe first element of the tuple is {t[0]}")
# t[0] = 3 raises a TypeError: 'tuple' object does not support item assignment

print(f"The shape and ndim of j_reshaped: {j_reshape.shape} {j_reshape.ndim}\n")
print(f"The transpose of j_reshape:\n{j_reshape.T}")

sqrtX = np.sqrt(x.T)
print(f"\nThe square root of x transpose:\n{sqrtX}")

s = np.array([1,2,3,4])
squares = s ** 2
fractionalExponent = s ** 0.5
print(f"\nThe squares of {s} are {squares}")
print(f"s to the 1/2 power is: {fractionalExponent}")

rng = np.random.default_rng(1303)

a = rng.normal(size=50)
b = rng.normal(loc=50, scale=1, size=50)
correlation = np.corrcoef(a,b)
print("The correlation of matrix a and b is:\n", correlation)

meanCor = np.mean(correlation)
varCor = np.var(correlation)
stdCor = np.std(correlation)

print(f"\nMean of corr matric is {meanCor}")
print(f"Variance of corr matric is {varCor}")
print(f"Standard Deviation of corr matric is {stdCor}")
