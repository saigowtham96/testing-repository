
def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if row_check(sudoku, list1) and column_check(sudoku, list1):
        return True
    return False







def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = [] 
    # read a line and append row to list
    row = list(map(int, input()))
    sudoku.append(row)
    # call solution function and print result to console
    print(sudoku)

if __name__ == '__main__':
    main()
