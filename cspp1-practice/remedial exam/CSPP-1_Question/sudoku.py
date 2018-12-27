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

def validateInput(data):
    if len(data) != 81:
        raise Exception("Invalid input")
    elif '.' not in data:
        raise Exception("Given sudoku is solved")
def validateSudoku(sudoku):
    for x in range(9):
        row_variable=getRowValues(x,sudoku)
        if len(row_variable) != len(set(row_variable)):
            raise Exception("Invalid Sudoku:Duplicate values")
        column_variable=getColumnValues(x,sudoku)
        if len(column_variable) != len(set(column_variable)):
            raise Exception("Invalid Sudoku:Duplicate values")
        

def getRowValues(cell, sudoku):
    row=[]
    for x in sudoku[cell]:
        if x != '.':
            row.append(x)
    # print(row)
    return row
"""
This  method should retunn all the values present in the ith column
"""
def getColumnValues(cell, sudoku):
    column=[]
    for row in sudoku:
        if row[cell] != '.':
            column.append(row[cell])
    return column
            

"""
This  method should retunn all the values present in the i,j th subgrid
"""
def getGridValues(i,j,sudoku):
    grid=[]
    if (i<=0 and i>3) and (j<=0 and j>3):
        for sub_row in range(0,3):
            for sub_col in range(0,3):
                grid.append(sudoku[sub_row][sub_col])
    if (i<=0 and i>3) and (j<=3 and j>6):
        for sub_row in range(0,3):
            for sub_col in range(3,6):
                grid.append(sudoku[sub_row][sub_col])
    if (i<=0 and i>3) and (j<=6 and j>9):
        for sub_row in range(0,3):
            for sub_col in range(6,9):
                grid.append(sudoku[sub_row][sub_col])
    if (i<=3 and i>6) and (j<=0 and j>3):
        for sub_row in range(3,6):
            for sub_col in range(0,3):
                grid.append(sudoku[sub_row][sub_col])
    if (i<=3 and i>6) and (j<=3 and j>6):
        for sub_row in range(3,6):
            for sub_col in range(3,6):
                grid.append(sudoku[sub_row][sub_col])

    if (i<=3 and i>6) and (j<=6 and j>9):
        for sub_row in range(3,6):
            for sub_col in range(6,9):
                grid.append(sudoku[sub_row][sub_col])
    if (i<=0 and i>3) and (j<=0 and j>3):
        for sub_row in range(6,9):
            for sub_col in range(0,3):
                grid.append(sudoku[sub_row][sub_col])
    if (i<=0 and i>3) and (j<=3 and j>6):
        for sub_row in range(6,9):
            for sub_col in range(3,6):
                grid.append(sudoku[sub_row][sub_col])
    if (i<=0 and i>3) and (j<=6 and j>9):
        for sub_row in range(6,9):
            for sub_col in range(6,9):
                grid.append(sudoku[sub_row][sub_col])
    # print(grid)
    return grid
                
"""
This method should collect all the available values present for a "."
You should get the values present in row,column,grid.
Then you should return the values that doesnot exist in the previous values.
"""
def possibleValues(sudoku):
    for x in range(len(sudoku)):
        for y in range(len(sudoku[0])):
            if sudoku[x][y]=='.':
                row_variable=getRowValues(x,sudoku)
                column_variable=getColumnValues(y,sudoku)
                result=row_variable+column_variable
                elements=''
                for i in range(1,10):
                    if str(i) not in result:
                        elements=elements+str(i)
                print(elements)
                
"""
Read the input and store the values in an appropriate data sturcture.
Then travese through each value, if you get a "." then collect the possible values
"""
def main():
    input_data= input()
    data=list(input_data)
    i=0
    sudoku=[]
    try:
        validateInput(input_data)
        while (i < 81):
            row=[]
            for j in range(9):
                row.append(data[i])
                i=i+1
            sudoku.append(row)
        validateSudoku(sudoku)
        possibleValues(sudoku)
        getGridValues(i,j,sudoku)
    except Exception as e:
        print(e)
    # print(sudoku)
    
if __name__ == '__main__':
    main()


