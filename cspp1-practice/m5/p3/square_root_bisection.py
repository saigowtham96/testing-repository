"""Bisectionmethod"""
A = int(input())
EP = 0.01
L = 0.0
H = A
ANS = (H + L)/2.0
while abs(ANS**2 - A) >= EP:
    if ANS**2 < A:
        L = ANS
    else:
        H = ANS
    ANS = (H + L)/2.0
print(ANS)
