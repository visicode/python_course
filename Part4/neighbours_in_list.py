# Write your solution here
def longest_series_of_neighbours(ls: list) -> int:
    result = 0
    was = False
    tmp = 0
    for i in range(len(ls)-1):
        if (ls[i]+1==ls[i+1]) or (ls[i]-1==ls[i+1]):
            tmp+=1
        else:
            tmp=0
        if tmp>result:
            result=tmp
                
    return result+1

if __name__ == '__main__':
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))