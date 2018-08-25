'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    '''
    print the keys and frequency with space
    '''
    counts = dictionary
    for key in sorted(counts):
        print(key, '-', counts[key])
	
def main():
    '''
    input
    '''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
