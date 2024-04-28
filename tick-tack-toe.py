import time


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def display(board):
    print('\n')
    for i, row in enumerate(board):
        print(' '*20, end='')
        print(' | '.join(row))
        if (i < 2):
            print(" "*19, end='')
            print("-"*11)
    print('\n')


def board_complete(board):
    return all(not cell.isdigit() for row in board for cell in row)

# main


print(' '*20, end='')
for u in "Start Game Of Tick-Tack-Toe\n":
    print(u, end='')
    time.sleep(0.1)
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
print(' '*20, end='')
for u in "Board Structure":
    print(u, end='')
    time.sleep(0.1)
display(board)
x = input("\n\tEnter name of Player 1: ").lower().capitalize()
o = input("\tEnter name of Player 2: ").lower().capitalize()
d = {'X': x, 'O': o}
current_player = 'X'
non_player = 'O'
box = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [
    1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
while True:
    print('\tPlayer', d[current_player]+"'s", 'chance')
    b = int(input('Enter box number: '))
    if (board[box[b][0]][box[b][1]].isalpha()):
        print("\tCELL TAKEN ALREADY TRY AGAIN",
              d[current_player].upper(), 'YOU FOOL')
        continue
    board[box[b][0]][box[b][1]] = current_player
    if check_winner(board, current_player):
        if (d[non_player] == 'Mahir'):
            time.sleep(0.5)
            print('\n\t', d[current_player].upper(), 'IS A CHEATER!!!!!!!')
            print('\t', 'ENTER AGAIN')
            time.sleep(2)
            board[box[b][0]][box[b][1]] = str(b)
            display(board)
        else:
            display(board)
            print('\t', d[current_player], 'wins and',
                  d[non_player], 'lost. Lol!!!!')
            break
    elif board_complete(board):
        display(board)
        print("\tIT'S A DRAW. LMAO!!!!")
        break
    else:
        display(board)
    current_player = 'O' if current_player == 'X' else 'X'
    non_player = 'X' if non_player == 'O' else 'O'
