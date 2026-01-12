# Write your solution here
def row_correct (g :list, r: int) -> bool:
    row = g[r] #working with the row

    #Counting which element present how many times
    count=[0,0,0,0,0,0,0,0,0]
    for num in row:
        if num!=0:
            count[num-1]+=1

    #Evaluating the result
    for num in count:
        if num>1:
            return False
    return True

def column_correct (g :list, r: int) -> bool:
    col=[]
    #creating a list from the row elements
    for row in g:
        col.append(row[r])
    

    #Counting which element present how many times
    count=[0,0,0,0,0,0,0,0,0]
    for num in col:
        if num!=0:
            count[num-1]+=1

    #Evaluating the result
    for num in count:
        if num>1:
            return False
    return True

def block_correct (g :list, r: int, c:int) -> bool:
    block=[]
    #creating a list from the list
    if (0<=r<=6) and (0<=c<=6): #check for stupid indexes
        block.append(g[r][c])
        block.append(g[r][c+1])
        block.append(g[r][c+2])

        block.append(g[r+1][c])
        block.append(g[r+1][c+1])
        block.append(g[r+1][c+2])

        block.append(g[r+2][c])
        block.append(g[r+2][c+1])
        block.append(g[r+2][c+2])
    else:
        return False #stupid index should not continue

    #Counting which element present how many times
    count=[0,0,0,0,0,0,0,0,0]
    for num in block:
        if num!=0:
            count[num-1]+=1

    #Evaluating the result
    for num in count:
        if num>1:
            return False
    return True

def sudoku_grid_correct(g: list) -> bool:
    
    #Check rows
    for n in range(9):
        if row_correct(g,n)==False:
            return False

    #Check cols
    for n in range(9):
        if column_correct(g,n)==False:
            return False

    #Check blocks
    to_check=[0,3,6]
    for i in to_check:
        for j in to_check:
            if block_correct(g,i,j)==False:
                return False
    
    return True

if __name__ == '__main__':
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))