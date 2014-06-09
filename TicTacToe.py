__author__ = 'QJ_H'

"""
井字过三关游戏
"""

import random
 
 
def draw_board(board):
    print('  '+board[7]+' |  '+board[8]+' | '+board[9])
    print('-----------------')
    print('  '+board[4]+' |  '+board[5]+' | '+board[6])
    print('-----------------')
    print('  '+board[1]+' |  '+board[2]+' | '+board[3])


def player_input():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O ?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def player_again():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def make_move(board, letter, move):
    board[move] = letter


def is_winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[2] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))


def clone_board(board):
    dupe_board = []

    for i in board:
        dupe_board.append(i)

    return dupe_board


def is_space_free(board, nextMove):
    return board[nextMove] == ' '


def get_player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('What is your next move? (1~9)')
        move = input()

    return int(move)


def choose_random_move(board, move):
    possible_moves = []
    for i in move:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) > 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #AI
    #first, check if we can win in the next move
    for i in range(1, 10):
        copy = clone_board(board)
        if is_space_free(copy, i):
            make_move(copy, computerLetter, i)
            if is_winner(copy, computerLetter):
                return i

    #second, check if the player could win on his next move, and block them
    for i in range(1, 10):
        copy = clone_board(board)
        if is_space_free(copy, i):
            make_move(copy, playerLetter, i)
            if is_winner(copy, playerLetter):
                return i

    #third, try to take one of the corners, if they are free
    move = choose_random_move(board, [1, 3, 7, 9])
    if move is not None:
        return move

    #forth, try to take the center, if it is free
    if is_space_free(board, 5):
        return 5

    #finally, move on one of the sides
    return choose_random_move(board, [2, 4, 6, 8])


def is_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False

    return True

#function ens
#begin to play


def play():
    print("Welcome to Tic Tac Toe!")

    while True:
        theBoard = [' '] * 10
        playerLetter, computerLetter = player_input()
        turn = who_goes_first()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                #player's turn
                draw_board(theBoard)
                move = get_player_move(theBoard)
                make_move(theBoard, playerLetter, move)


                if is_winner(theBoard, playerLetter):
                    draw_board(theBoard)
                    print('Hooray! You have won the game!')
                    gameIsPlaying = False
                else:
                    if is_board_full(theBoard):
                        draw_board(theBoard)
                        print("The Game is Tie!")
                        break
                    else:
                        turn = 'computer'
            else:
                #computer's turn
                move = get_computer_move(theBoard, computerLetter)
                make_move(theBoard, computerLetter, move)
                if is_winner(theBoard, computerLetter):
                    draw_board(theBoard)
                    print('The computer has beaten you! you lose.')
                    gameIsPlaying = False
                else:
                    if is_board_full(theBoard):
                        draw_board(theBoard)
                        print('The Game is tie!')
                        break
                    else:
                        turn = 'player'

        if not player_again():
            break

play()