'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
n = int(input())
# n = 16
i=1
for i in range(1,n+1,1):
    if(i%3==0 and i%5==0):
        print("fizz")
        print("buzz")
       # break
    elif(i%3==0):
        print("fizz")
        # break
    elif(i%5==0):
        print("Buzz")
        # break
    else:
        print(i)
    i=i+1          
     
