'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def read_input(user_input):
   lines = ""
   for i in range(user_input):
      lines+=input()+"\n"
   print(lines)

def main():
   user_input = int(input())
   read_input(user_input)
if __name__ == '__main__':
    main()
