# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and returns the factorial of given number.

# This function takes in one number and returns one number.


def factorial(N_l):
    """defining pylint"""
    if N_l <= 1:
        return 1
    return N_l*factorial(N_l-1)
    


def main():
    a = input()
    print(factorial(int(a)))    

if __name__== "__main__":
    main()
