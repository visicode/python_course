# Write your solution here
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

if __name__ == '__main__':
    sudoku = [
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

    print(block_correct(sudoku, 0, 0)) #False
    print(block_correct(sudoku, 1, 2)) #True