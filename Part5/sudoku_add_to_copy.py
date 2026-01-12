# Write your solution here
def print_sudoku (sls: list):
    for i in range(9):
        for j in range(9):
            if sls[i][j]==0:
                print(f"_ ",end="")
            else:
                print(f"{sls[i][j]} ",end="")
            if (j+1)%3==0: #every third column extra space
                print(f" ",end="")
        if (i+1)%3==0:
            print() #every third row extra line
        print()

def copy_and_add(sls: list, r: int, c: int, val: int) -> list:
    nls = []
    for i in sls:
        nls.append(i[:])

    if (1<=val<=9):
        nls[r][c]=val
    return nls
            

if __name__ == '__main__':
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)