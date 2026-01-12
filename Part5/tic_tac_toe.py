# Write your solution here
def play_turn (ls :list, x: int, y: int,val: str) -> bool:
    if (val in ["X","O"]) and (0<=x<=2) and (0<=y<=2):
        if ls[y][x]=="":
            ls[y][x]=val
            return True
    return False


if __name__ == '__main__':
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)