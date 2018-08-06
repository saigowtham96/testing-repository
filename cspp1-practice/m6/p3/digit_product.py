'''
Given a  number int_input, find the product of all the digits

'''
NUM = int(input())
# NUM = -12345
temp = NUM
I = 1
if NUM < 0:
	NUM = NUM * -1
while NUM >= 1:      
    A = NUM%10
    I = A*I
    NUM = NUM//10

if temp < 0:
    I = I * -1

if temp == 0:
	print(temp) 
else:
	print(I)    

