s=input("enter the string")
count = 0
for letter in s:
    if letter in 'aeiou':
        count += 1
print (count)
