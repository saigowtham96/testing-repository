# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and returns the factorial of given number.

# This function takes in one number and returns one number.


def factorial(N_1):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if N_1 <= 1:
        return 1
    return N_1*factorial(N_1-1)
    


def main():
    a = input()
    print(factorial(int(a)))    

if __name__== "__main__":
    main()
