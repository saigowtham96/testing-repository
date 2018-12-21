import re
def main():
	inp = input()
	inp = list(inp)
	list1 = []
	i = 0
	temp = []
	for i in range(len(inp)):
		if i%9==0 and i!=0:
			list1.append(temp)		
			temp = []
		temp.append(inp[i])
	list1.append(temp)
	for i in range(len(list1)):
		for j in range(len(list1[0])):
			if list1[i][j] == '.':
				print(sudoku(list1,i,j))
def sudoku(list1,i,j):
	# for i in range(len(lis)):
	# 	print(list1[i])
	# 	print()
	temp1 = []
	for k in range(len(list1)):
		tem.append(list1[k][j])
	for m in range(len(list1[0])):
		tem.append(list1[i][m])
	if (i >= 0 and i <= 2) and (j >= 0 and j <= 2):
		for x in range(0,3):
			for y in range(0,3):
				temp1.append(list1[x][y])
	elif (i >= 0 and i <= 2) and (j >= 3 and j <= 5):
		for x in range(0,3):
			for y in range(3,6):
				temp1.append(list1[x][y])
	elif (i >= 0 and i <= 2) and (j >= 6 and j <= 8):
		for x in range(0,3):
			for y in range(6,9):
				temp1.append(list1[x][y])
	elif (i >= 3 and i <= 5) and (j >= 0 and j <= 2):
		for x in range(3,6):
			for y in range(0,3):
				temp1.append(list1[x][y])
	elif (i >= 3 and i <= 5) and (j >= 3 and j <= 5):
		for x in range(3,6):
			for y in range(3,6):
				temp1.append(list1[x][y])
	elif (i >= 3 and i <= 5) and (j >= 6 and j <= 8):
		for x in range(3,6):
			for y in range(6,9):
				temp1.append(list1[x][y])
	elif (i >= 6 and i <= 8) and (j >= 0 and j <= 2):
		for x in range(6,9):
			for y in range(0,3):
				temp1.append(list1[x][y])
	elif (i >= 6 and i <= 8) and (j >= 3 and j <= 5):
		for x in range(6,9):
			for y in range(3,6):
				temp1.append(list1[x][y])
	elif (i >= 6 and i <= 8) and (j >= 6 and j <= 8):
		for x in range(6,9):
			for y in range(6,9):
				temp1.append(list1[x][y])
	string1 = ''.join(tem)
	string1 = string.replace(".", "")
	string = list(string)
	inte = list(map(int,string1))
	whole = [1,2,3,4,5,6,7,8,9]
	numbers = []
	for z in range(len(whole)):
		if whole[z] not in inte:
			numbers.append(whole[z])
	string2 = list(map(str,numbers))
	string2 = ''.join(string2)
	return string2
main()
