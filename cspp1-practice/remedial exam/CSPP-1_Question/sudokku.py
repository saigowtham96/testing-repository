def solveSudoku(grid, i=0, j=0):
            i,j = findNextCellToFill(grid, i, j)
            if i == -1:
                    return True
            for e in range(1,10):
                    if isValid(grid,i,j,e):
                            grid[i][j] = e
                            if solveSudoku(grid, i, j):
                                    return True
                            # Undo the current cell for backtracking
                            grid[i][j] = 0
            return False
