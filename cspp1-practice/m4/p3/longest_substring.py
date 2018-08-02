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
t1=i
t2=l

print(i,l)
while i<=l:
    print(s[i])
    i=i+1
