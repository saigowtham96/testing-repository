"""
square root approximation
"""
M = int(input())
EP = 0.1
A = 0
A = int(A)
while (M - (A*A) > EP) and A < M:
    if M - (A*A) > EP:
        A = A+EP
print(A)


