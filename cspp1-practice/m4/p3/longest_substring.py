S = input()
S = S + " "
Z = 0
LEN1 = -1
while Z < (len(S) - 2):
    I = Z
    while S[I] <= S[I+1] and (I) < (len(S)-2):
        I = I + 1
    LEN2 = I - Z
    if LEN2 > LEN1:
        LEN1 = LEN2
        K = int(Z)
        L = int(I)
    Z = I + 1
S1 = ""
while K <= L:
    S1 = S1 + S[K]
    K = K + 1
print(S1)
