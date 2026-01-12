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

    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))