"""
square root approximation
"""
N = int(input())
EP = 0.1
A = 0.0
A = int(A)
while (N - (A*A) > EP) and A < N:
    if N - (A*A) > EP:
        A = A+EP
print(A)
