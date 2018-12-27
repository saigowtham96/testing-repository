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
        var = getRowValues(x,sudoku)
        if len(var) != len(set(var)):
            raise Exception("Invalid Sudoku:Duplicate values")
        columnvar=getColumnValues(x,sudoku)
        if len(columnvar) != len((columnvar)):
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
          
"""
This method should collect all the available values present for a "."
You should get the values present in row,column,grid.
Then you should return the values that doesnot exist in the previous values.
"""
def possibleValues(sudoku):
    for x in range(len(sudoku)):
        for y in range(len(sudoku[0])):
            if sudoku[x][y]=='.':
                var=getRowValues(x,sudoku)
                column =getColumnValues(y,sudoku)
                result=var+columnvar
                string=''
                for i in range(1,10):
                    if str(i) not in result:
                        string=string+str(i)
                print(string)
                
"""
Read the input and store the values in an appropriate data sturcture.
Then travese through each value, if you get a "." then collect the possible values
"""
def main():
    data= input()
    data1=list(input_data)
    j=0
    sudoku=[]
    try:
        validateInput(data)
        while (j < 81):
            row=[]
            for k in range(9):
                row.append(data1[i])
                j=j+1
            sudoku.append(row)
        validateSudoku(sudoku)
        possibleValues(sudoku)
        getGridValues(i,j,sudoku)
    except Exception as e:
        print(e)
    # print(sudoku)
    
if __name__ == '__main__':
    main()


