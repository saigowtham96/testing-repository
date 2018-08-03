s=input()
s=s+" "
z=0
len1=-1
while z<(len(s)-2):
    j=z
    while s[j]<=s[j+1] and (j)<(len(s)-2):
        j=j+1
    len2=j-z
    if len2>len1:
        len1=len2
        i=int(z)
        l=int(j)
    z=j+1
S1 = ""
while i<=l:
    S1 = S1 + S[i]
    i=i+1
print(S1)
