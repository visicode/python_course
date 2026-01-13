# write your solution here

def matrix_sum()-> int:
    rs = row_sums()
    return sum(rs)

def matrix_max()-> int:
    res=0
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            for st in parts:
                if int(st) > res:
                    res = int(st)
    return res

def row_sums()-> list:
    res=[]
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            sm=0
            for st in parts:
                sm += int(st)
            res.append(sm)
    return res
    
if __name__ == '__main__':
    print(matrix_sum())
    print(matrix_max())