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

def add_number(sls: list, r: int, c: int, val: int):
    if (1<=val<=9):
        sls[r][c]=val
            

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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)