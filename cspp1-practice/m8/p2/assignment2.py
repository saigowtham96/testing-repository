# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.


def sum_of_digits(n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if n == 0:
       return 0
    else:   
       return int(n % 10 + sum_of_digits(n / /10))



def main():
    a = input()
    print(sum_of_digits(int(a)))  

if __name__== "__main__":
    main()

