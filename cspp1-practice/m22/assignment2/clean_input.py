'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    '''
    to remove special characters and retain the alphabets
    '''
    list1 =[]
    for i in range(len(string)):
        if i not in list1:
           list1.append(i)
    new_string = re.sub('[^ a-zA-Z]', '', list1)
    print(new_string)
            
   
        

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
