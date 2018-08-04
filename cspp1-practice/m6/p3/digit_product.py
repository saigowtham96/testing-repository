'''
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
'''
NUM = int(input("enter the number"))
I = 1
while I<NUM:
   A = NUM%10
   I = A*I
   NUM = NUM//10
   
print(I)    

