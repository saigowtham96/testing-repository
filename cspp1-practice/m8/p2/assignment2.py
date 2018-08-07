# Exercise: Assignment-2
"""sum"""
def sumofdigits(num_num):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if num_num <= 0:
        return 0
    num_sum = num_num % 10
    return num_sum + sumofdigits(num_num//10)
def main():
    """
    main
    """
    num_a = input()
    print(sumofdigits(int(num_a)))
if __name__ == "__main__":
    main()
