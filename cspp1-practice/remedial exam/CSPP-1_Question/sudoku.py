"""
In this method :
 * Check there are only 81 values
 * iterate through each row in the sudoku and if you find any duplicate values
 	raise an exception
 * iterate through each column in the sudoku and if you find any duplicate values
	raise an exception
 * iterate through each subgrid(3x3) in the sudoku and if you find any duplicate values
	raise an exception
"""
def validateSudoku(sudoku):
        if len(given_input) > 81 or len(given_input) < 81:
                print("Invalid input")
        
        
        
        
        
	
"""
This  method should retunn all the values present in the xth row
"""
def getRowValues(row):
        list1 = set()
        for i in range(9):
                for j in range(9):
                        if row[i] != '0':
                                list1.append(i)
        return list1
         
	
"""
This  method should retunn all the values present in the ith column
"""
def getColumnValues(col):
        list2 = set()
        for i in range(9):
                for j in range(9):
                        if col[j] != '0':
                                list2.append(j)
        return list2


"""
This  method should retunn all the values present in the x,j th subgrid
"""
def getGridValues(grid):
        for i in range(9):
                print(grid[i])
"""
This method should collect all the available values present for a "."
You should get the values present in row,column,grid.
Then you should return the values that doesnot exist in the previous values.
"""
def possibleValues():
	pass
"""
Read the input and store the values in an appropriate data sturcture.
Then travese through each value, if you get a "." then collect the possible values
"""
def main():
        grid = [[0 for x in range(9)] for y in range(9)]
        given_input = input()
        k = 0
        for i in range(9):
                for j in range(9):
                        if given_input[k] != '.':
                                grid[i][j] = given_input[k]
                        k = k+1
        print(getGridValues(grid))
        print(validateSudoku(given_input))

        
                                
                                
        


