'''
Given a  number int_input, find the product of all the digits

'''
int_input= int(input())
I = 1
while I<int_input:
   A = int_input%10
   I = A*I
   int_input = int_input//10
   
print(I)    

