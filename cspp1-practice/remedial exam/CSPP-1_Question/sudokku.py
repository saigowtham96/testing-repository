def print_grid(arr): 
    for i in range(9): 
        print(arr[i]) 
def create_set(h, row, col):
    list1= set()
    for i in range(9):
        if h[row][i] != '0':
            list1.add(h[row][i])
        if h[i][col] != '0':
            list1.add(h[i][col])
    return list1

def possibilities(h):
    for i in range(9):
        for j in range(9):
            result = ""
            s = set()
            if h[i][j] == '0':
                s = create_set(h, i, j)
                # print(s)
            if len(s) != 0:
                for each in "123456789":
                    if each not in s:
                        result += each
                print(result)
        

if __name__=="__main__": 
      
    # creating a 2D array for the grid 
    grid=[['0' for x in range(9)]for y in range(9)] 
    # print_grid(grid)
      
    given_input = input()
    k = 0
    for i in range(9):
        for j in range(9):
            if given_input[k] != '.':
                grid[i][j] = given_input[k]
            k += 1
    # print_grid(grid)
    possibilities(grid)
