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
def validInput(info):
    if len(info) != 81:
        raise Exception("Invalid input")
    elif '.' not in info:
        raise Exception("Given sudoku is solved")
def validateSudoku(sudoku):
    for x in range(0,9):
        var_A = getRowValues(x, sudoku)
        if(len(set(var_A))) != len(var_A):
            raise Exception("duplicates are present")
        columnvar = getColumnValues(x, sudoku)
        if(len(set(columnvar))) != len(columnvar):
            raise Exception("duplicates are present")
    
"""
This  method should retunn all the values present in the ith row
"""
def getRowValues(cell, sudoku):
    row = []
    for x in range(cell):
        if x != '.':
            row.append(x)
    return row 
"""
This  method should retunn all the values present in the ith column
"""
def getColumnValues(cell, sudoku):
    col = []
    for y in range(cell):
        if row[cell] != '.':
            col.append(row[cell])
    return col

"""
This  method should retunn all the values present in the i,j th subgrid
"""
def getGridValues():
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
    info1 = input()
    info = list(info1)
    j = 0
    try:
        validInput(info)
        while(j<81):
            row = []
            for k in range(0,9):
                row.append(info)
                j += 1
            sudoku.append(row)
        validateSudoku(sudoku)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    main()
