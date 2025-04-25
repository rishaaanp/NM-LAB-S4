import numpy as np

def gauss_elimination_pivoting(A, b):
    n = len(b)
    A = A.astype(float)
    b = b.astype(float)

    Ab = np.hstack([A, b.reshape(-1, 1)])

    for i in range(n):
        max_row = np.argmax(abs(Ab[i:n, i])) + i
        if i != max_row:
            Ab[[i, max_row]] = Ab[[max_row, i]]

        for j in range(i+1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    
    return x

# Example 
A = np.array([[3, -2, 5], [4, 5, 8], [1, 1, 3]])
b = np.array([3, 4, 7])

solution = gauss_elimination_pivoting(A, b)
print("Solution:", solution)