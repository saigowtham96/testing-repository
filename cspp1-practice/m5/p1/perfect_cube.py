"""
perfect Cube
"""
GUESS = 1
M = int(input(""))
FLAG = 0
while GUESS < M+1:
    if GUESS**3 == M:
        print(str(M) + " " + "is a perfect cube")
        FLAG = 1
        break
    GUESS = GUESS + 1
if FLAG == 0:
    print(str(M) + " " + "is not a perfect cube")

