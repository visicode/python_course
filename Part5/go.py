# Write your solution here
def who_won(gb: list) -> int:
    p1=0
    p2=0
    for row in gb:
        p1+=row.count(1)
        p2+=row.count(2)
    if p1>p2:
        return 1
    elif p1==p2:
        return 0
    else:
        return 2

if __name__ == '__main__':
    game=[[1,1],[2,0]]
    print (who_won(game))
    