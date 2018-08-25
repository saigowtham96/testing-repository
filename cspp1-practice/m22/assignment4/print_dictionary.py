'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''
from collections import Counter
def print_dictionary(dictionary):
    pass
    '''
    print the keys and frequency with space

    '''
    counts = dictionary
    for key in counts:
        print(key,'-' ,counts[key])
	

            
    

def main():
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
