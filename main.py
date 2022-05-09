import math

import numpy as np

class Move:
    def __init__(self):
        self.location = None
        self.children = None

def play_game():
    player_turn()
    play_on = check_player_win()
    if play_on == True:
        if num_empty_squares(board_rep) == 0:
            print('Game is a tie!')
            play_on = False
            return play_on
        else:
            computer_turn()
            play_on = check_computer_win()
            return play_on
    else:
        return play_on


def player_turn():
    global board, board_rep
    choice = input('Player, Choose a spot on the board to mark with an X in the format: 0,0')
    choice = choice.split(",")
    spot_one = (int(choice[0]))
    spot_two = (int(choice[1]))

    spots = check_if_valid(spot_one, spot_two)
    spot_one = spots[0]
    spot_two = spots[1]

    spots = check_if_taken(spot_one, spot_two)
    spot_one = spots[0]
    spot_two = spots[1]

    if spot_one == 0:
        if spot_two == 0:
            num = 0
        elif spot_two == 1:
            num = 1
        else:
            num = 2
    elif spot_one == 1:
        if spot_two == 0:
            num = 3
        elif spot_two == 1:
            num = 4
        else:
            num = 5
    else:
        if spot_two == 0:
            num = 6
        elif spot_two == 1:
            num = 7
        else:
            num = 8

    board_rep[num] = 'X'

    board_spots[spot_one, spot_two] = 'X'
    board = (f"{board_spots[0, 0]}  |  {board_spots[0, 1]}  |  {board_spots[0, 2]}\n"
            "______________\n"
            f"{board_spots[1, 0]}  |  {board_spots[1, 1]}  |  {board_spots[1, 2]}\n"
            "______________\n"
            f"{board_spots[2, 0]}  |  {board_spots[2, 1]}  |  {board_spots[2, 2]}\n")
    print(board)


def computer_turn():
    global board, board_rep

    computer_player = True

    computer_move = minimax(computer_player)['position']

    board_rep[computer_move] = 'O'

    if computer_move == 0:
        spot_one = 0
        spot_two = 0
    elif computer_move == 1:
        spot_one = 0
        spot_two = 1
    elif computer_move == 2:
        spot_one = 0
        spot_two = 2
    elif computer_move == 3:
        spot_one = 1
        spot_two = 0
    elif computer_move == 4:
        spot_one = 1
        spot_two = 1
    elif computer_move == 5:
        spot_one = 1
        spot_two = 2
    elif computer_move == 6:
        spot_one = 2
        spot_two = 0
    elif computer_move == 7:
        spot_one = 2
        spot_two = 1
    else:
        spot_one = 2
        spot_two = 2

    board_spots[spot_one, spot_two] = 'O'

    board = (f"{board_spots[0, 0]}  |  {board_spots[0, 1]}  |  {board_spots[0, 2]}\n"
            "______________\n"
            f"{board_spots[1, 0]}  |  {board_spots[1, 1]}  |  {board_spots[1, 2]}\n"
            "______________\n"
            f"{board_spots[2, 0]}  |  {board_spots[2, 1]}  |  {board_spots[2, 2]}\n")
    print(board)

    return True

def minimax(computer_player):
    global board_rep

    if eval_computer_win(board_rep):
        return {'position': None, 'score': 1 * (num_empty_squares(board_rep) + 1)}
    if eval_player_win(board_rep):
        return {'position': None, 'score': -1 * (num_empty_squares(board_rep) + 1)}


    if num_empty_squares(board_rep) == 0:
        return {'position': None, 'score': 0}

    # computer player is always the maximizing player
    if computer_player:
        best_score = {'position': None, 'score': -math.inf}
    else:
        best_score = {'position': None, 'score': math.inf}

    for move in available_moves(board_rep):
        if computer_player:
            board_rep[move] = 'O'
            try_score = minimax(False)
        else:
            board_rep[move] = 'X'
            try_score = minimax(True)


        board_rep[move] = ' '
        try_score['position'] = move

        if computer_player:
            if try_score['score'] > best_score['score']:
                best_score = try_score

        else:
            if try_score['score'] < best_score['score']:
                best_score = try_score

    return best_score

def check_player_win():
    if (board_spots[0, 0] == 'X' and board_spots[0, 1] == 'X' and board_spots[0, 2] == 'X'):
        print('Player Wins!')
        return False
    elif (board_spots[1, 0] == 'X' and board_spots[1, 1] == 'X' and board_spots[1, 2] == 'X'):
        print('Player Wins!')
        return False
    elif (board_spots[2, 0] == 'X' and board_spots[2, 1] == 'X' and board_spots[2, 2] == 'X'):
        print('Player Wins!')
        return False
    elif (board_spots[0, 0] == 'X' and board_spots[1, 0] == 'X' and board_spots[2, 0] == 'X'):
        print('Player Wins!')
        return False
    elif (board_spots[0, 1] == 'X' and board_spots[1, 1] == 'X' and board_spots[2, 1] == 'X'):
        print('Player Wins!')
        return False
    elif (board_spots[0, 2] == 'X' and board_spots[1, 2] == 'X' and board_spots[2, 2] == 'X'):
        print('Player Wins!')
        return False
    elif (board_spots[0, 0] == 'X' and board_spots[1, 1] == 'X' and board_spots[2, 2] == 'X'):
        print('Player Wins!')
        return False
    elif (board_spots[2, 0] == 'X' and board_spots[1, 1] == 'X' and board_spots[0, 2] == 'X'):
        print('Player Wins!')
        return False
    else:
        return True


def check_computer_win():
    if (board_spots[0, 0] == 'O' and board_spots[0, 1] == 'O' and board_spots[0, 2] == 'O'):
        print('Computer Wins!')
        return False
    elif (board_spots[1, 0] == 'O' and board_spots[1, 1] == 'O' and board_spots[1, 2] == 'O'):
        print('Computer Wins!')
        return False
    elif (board_spots[2, 0] == 'O' and board_spots[2, 1] == 'O' and board_spots[2, 2] == 'O'):
        print('Computer Wins!')
        return False
    elif (board_spots[0, 0] == 'O' and board_spots[1, 0] == 'O' and board_spots[2, 0] == 'O'):
        print('Computer Wins!')
        return False
    elif (board_spots[0, 1] == 'O' and board_spots[1, 1] == 'O' and board_spots[2, 1] == 'O'):
        print('Computer Wins!')
        return False
    elif (board_spots[0, 2] == 'O' and board_spots[1, 2] == 'O' and board_spots[2, 2] == 'O'):
        print('Computer Wins!')
        return False
    elif (board_spots[0, 0] == 'O' and board_spots[1, 1] == 'O' and board_spots[2, 2] == 'O'):
        print('Computer Wins!')
        return False
    elif (board_spots[2, 0] == 'O' and board_spots[1, 1] == 'O' and board_spots[0, 2] == 'O'):
        print('Computer Wins!')
        return False
    else:
        return True


def eval_player_win(board_rep):
    if board_rep[0] == 'X' and board_rep[1] == 'X' and board_rep[2] == 'X':
        return True
    if board_rep[3] == 'X' and board_rep[4] == 'X' and board_rep[5] == 'X':
        return True
    if board_rep[6] == 'X' and board_rep[7] == 'X' and board_rep[8] == 'X':
        return True
    if board_rep[0] == 'X' and board_rep[3] == 'X' and board_rep[6] == 'X':
        return True
    if board_rep[1] == 'X' and board_rep[4] == 'X' and board_rep[7] == 'X':
        return True
    if board_rep[2] == 'X' and board_rep[5] == 'X' and board_rep[8] == 'X':
        return True
    if board_rep[0] == 'X' and board_rep[4] == 'X' and board_rep[8] == 'X':
        return True
    if board_rep[2] == 'X' and board_rep[4] == 'X' and board_rep[6] == 'X':
        return True
    else:
        return False

def eval_computer_win(board_rep):
    if board_rep[0] == 'O' and board_rep[1] == 'O' and board_rep[2] == 'O':
        return True
    if board_rep[3] == 'O' and board_rep[4] == 'O' and board_rep[5] == 'O':
        return True
    if board_rep[6] == 'O' and board_rep[7] == 'O' and board_rep[8] == 'O':
        return True
    if board_rep[0] == 'O' and board_rep[3] == 'O' and board_rep[6] == 'O':
        return True
    if board_rep[1] == 'O' and board_rep[4] == 'O' and board_rep[7] == 'O':
        return True
    if board_rep[2] == 'O' and board_rep[5] == 'O' and board_rep[8] == 'O':
        return True
    if board_rep[0] == 'O' and board_rep[4] == 'O' and board_rep[8] == 'O':
        return True
    if board_rep[2] == 'O' and board_rep[4] == 'O' and board_rep[6] == 'O':
        return True
    else:
        return False

def check_if_taken(spot_one, spot_two):
    valid_choice = True
    while valid_choice:
        if board_spots[spot_one, spot_two] == 'X' or board_spots[spot_one, spot_two] == 'O':
            choice = input('Please choose a spot that hasn\'t already been taken.')
            choice = choice.split(",")
            spot_one = (int(choice[0]))
            spot_two = (int(choice[1]))
            spots = [spot_one, spot_two]
        else:
            spots = [spot_one, spot_two]
            valid_choice = False
    return spots


def check_if_valid(spot_one, spot_two):
    valid_choice = True
    while valid_choice:
        if  (spot_one < 0 or spot_one > 2) or (spot_two < 0 or spot_two > 2):
            choice = input('Please enter a valid position on the board')
            choice = choice.split(",")
            spot_one = (int(choice[0]))
            spot_two = (int(choice[1]))
            spots = [spot_one, spot_two]
        else:
            spots = [spot_one, spot_two]
            valid_choice = False
    return spots

def num_empty_squares(board_rep):
    return board_rep.count(' ')

def available_moves(board_rep):
    return [i for i, x in enumerate(board_rep) if x == ' ']


board_rep = [' ' for spot in range(9)]
board_spots = np.array(board_rep)
board_spots = board_spots.reshape(3, 3)

board = (f"{board_spots[0, 0]}  |  {board_spots[0, 1]}  |  {board_spots[0, 2]}\n"
      "______________\n"
      f"{board_spots[1, 0]}  |  {board_spots[1, 1]}  |  {board_spots[1, 2]}\n"
      "______________\n"
      f"{board_spots[2, 0]}  |  {board_spots[2, 1]}  |  {board_spots[2, 2]}\n")


computer_move = None

print('Player will be marking their spots with an \'X\'')
print('Computer will be marking their spots with an \'O\'')
print('Location 0,0 denotes the position at row 0, column 0.')
print(board)


play_on = True
while play_on:
      play_on = play_game()
      another_game = None
      if play_on == False:
          another_game = input('That was fun! Would you like to play again? Type \'y\' if so, and anything else to stop playing')
      if another_game == 'y':
          play_on = True
          board_rep = [' ' for spot in range(9)]
          board_spots = np.array(board_rep)
          board_spots = board_spots.reshape(3, 3)

          playable_moves_computer = [0 for spot in range(9)]
          playable_moves_computer = np.array(playable_moves_computer)
          playable_moves_computer = playable_moves_computer.reshape(3, 3)

          board = (f"{board_spots[0, 0]}  |  {board_spots[0, 1]}  |  {board_spots[0, 2]}\n"
                   "______________\n"
                   f"{board_spots[1, 0]}  |  {board_spots[1, 1]}  |  {board_spots[1, 2]}\n"
                   "______________\n"
                   f"{board_spots[2, 0]}  |  {board_spots[2, 1]}  |  {board_spots[2, 2]}\n")



