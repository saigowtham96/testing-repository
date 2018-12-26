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
def validinput(data1):
        if len(data1) != 81:
                raise Exception("Invalid input")
        elif '.' not in data1:
                raise Exception("Given sudoku is solved")
def validSudoku(sudoku):
        pass
        
	
"""
This  method should retunn all the values present in the xth row
"""
def getRowValues(cell, sudoku):
        row = []
        for x in sudoku[cell]:
                if a != '.':
                        row.append(a)
        return row
         	
"""
This  method should retunn all the values present in the ith column
"""
def getColumnValues(cell, sudoku):
        pass

"""
This  method should retunn all the values present in the x,j th subgrid
"""
def getGridValues(grid):
        pass

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
        data = input()
        data1 = list(data)
        j = 0
        sudoku = []
        try:
                while(j < 81):
                        row = []
                        for k in range(0,9):
                                row.append(data1[j])
                                j = j+1
                        sudoku.append(row)
                validinput(data)
                validateSudoku(sudoku)
        except Exception as e:
                print(e)
if __name__ == '__main__':
    main()
        
        

        
                                
                                
        


