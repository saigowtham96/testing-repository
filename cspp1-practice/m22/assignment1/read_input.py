'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def read_input(user_input):
   no_of_lines = 5
   lines = ""
   for i in range(5):
      lines+=input()+"\n"
   print(lines)

def main():
   user_input = input()
   read_input(user_input)
if __name__ == '__main__':
    main()
