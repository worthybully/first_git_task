def draw_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])
def get_player_move(board, player):
    while True:
        move = input(f'Игрок {player}, введите номер клетки от 1 до 9')
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == ' ':
            return int(move) - 1
        else:
            print('Недопустимый ход, попробуйте ещё раз')
import random
def get_computer_move(board):
    while True:
        move = random.randint(0, 9)
        if board[move] == ' ':
            return move
def check_win(board, player):
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player:
            return True
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6]:
        return True
    return False
def main():
    board = [' '] * 9
    players = ['X', '0']
    turn = 0
    print('Добро пожаловать в игру')
    while True:
        draw_board(board)
        player = player[turn % 2]
        if player == 'X':
            move = get_player_move(board, player)
        else:
            print(f'Компьютер {player} делает ход')
            move = get_computer_move(board)
        board[move] = player
        if check_win(board, player):
            draw_board(board)
            print(f'Поздравляем! Игрок {player} победил!')
            break
        elif ' ' not in board:
            draw_board(board)
            print('Ничья')
            break
        turn += 1