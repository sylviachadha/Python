board = ["  " for i in range(9)]

def display_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def player_move(player_icon):
    
    if player_icon == "X":
        number =1
    elif player_icon == 'O':
        number =2
    
    print("Your turn player {}".format(number))
    choice = int(input("Enter your move(1-9): ").strip())
    if board[choice - 1] == "  ":
        board[choice - 1] = player_icon
    else:
        print()
        print("That space is taken!")


# We use below function to return a boolean and then use that boolean return further in  
# conditional check ---->  if is_victory("X"):
# is_victory("X") return either True or False
def is_victory(player_icon):
    if (board[0] == player_icon and board[1] == player_icon and board[2] == player_icon) or \
       (board[3] == player_icon and board[4] == player_icon and board[5] == player_icon) or \
       (board[6] == player_icon and board[7] == player_icon and board[8] == player_icon) or \
       (board[0] == player_icon and board[3] == player_icon and board[6] == player_icon) or \
       (board[1] == player_icon and board[4] == player_icon and board[7] == player_icon) or \
       (board[2] == player_icon and board[5] == player_icon and board[8] == player_icon) or \
       (board[0] == player_icon and board[4] == player_icon and board[8] == player_icon) or \
       (board[2] == player_icon and board[4] == player_icon and board[6] == player_icon):
        return True
    else:
        return False


def is_draw():
    if "  " not in board:
        return True
    else:
        return False

    
while True:
    display_board()
    player_move("X")
    display_board()
    if is_victory("X"):
        print("X wins! Congratulations!")
        break
    elif is_draw():
        print("Its a draw!")
        break
    player_move("O")
    if is_victory("O"):
        display_board()
        print("O wins! Congratulations!")
        break
    elif is_draw():
        print("Its a draw!")
        break










    
