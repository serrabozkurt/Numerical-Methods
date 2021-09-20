import numpy as np

def combine(U, S, V):
   return np.dot(np.dot(U, S), V)

def required_operations(x, A): # x is the estimated eigenvector

    x = np.dot(A, x) # matrix multiplication
    
    # and then normalization: dividing every entry in a vector by 
    # its magnitude to create a UNIT VECTOR (vector of length 1)

    x = x/ np.linalg.norm(x)

    transpose = np.transpose(x)
    
    new_eigenvalue = combine(transpose, A, x)

    return new_eigenvalue, x


A = np.array([[-2,1,4],[1,1,1],[4,1,-2]])     # matrix A given to us
v01 = np.array([1,2,1])  # initial eigenvector 1 that is given to us
v02 = np.array([1,2,-1]) # initial eigenvector 2 that is given to us

print("\n")

print("Operation starting from eigenvector V0-1 =", v01)

for i in range(5):  # 0 1 2 3 4 => 5 iteration
    eigenvalue, v01 = required_operations(v01, A)
    print("Iteration:", i+1, "estimated eigenvalue:", eigenvalue, end="\n\n")


print("EIGENVALUE - 1:", eigenvalue)
print("EIGENVECTOR - 1:", v01, end="\n\n\n")


print("Operation starting from eigenvector V0-2 =", v02)

for i in range(5):  # 0 1 2 3 4 => 5 iteration
    eigenvalue2, v02 = required_operations(v02, A) 
    print("Iteration:", i+1, "estimated eigenvalue:", eigenvalue2, end="\n\n")


print("EIGENVALUE - 2:", eigenvalue2)
print("EIGENVECTOR - 2:", v02, end="\n\n")

