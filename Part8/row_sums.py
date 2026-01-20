# Write your solution here
def row_sums(my_matrix: list)->None:
    for i in  my_matrix:
        s=sum(i)
        i.append(s)


if __name__ == '__main__':
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)

#[[1, 2, 3], [3, 4, 7]]
