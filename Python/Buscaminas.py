import random

# Función para crear el tablero
def create_board(num_rows, num_cols, num_bombs):
    board = [[0 for j in range(num_cols)] for i in range(num_rows)]
    bombs_placed = 0
    while bombs_placed < num_bombs:
        row = random.randint(0, num_rows - 1)
        col = random.randint(0, num_cols - 1)
        if board[row][col] != -1:
            board[row][col] = -1
            bombs_placed += 1
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i < num_rows and 0 <= j < num_cols and board[i][j] != -1:
                        board[i][j] += 1
    return board

# Función para imprimir el tablero
def print_board(board):
    for row in board:
        print(' '.join(str(x) for x in row))

# Función para jugar el juego
def play_game(board):
    num_rows = len(board)
    num_cols = len(board[0])
    revealed = [[False for j in range(num_cols)] for i in range(num_rows)]
    while True:
        print_board(revealed)
        row = int(input('Ingrese la fila: '))
        col = int(input('Ingrese la columna: '))
        if board[row][col] == -1:
            print('Perdiste')
            break
        else:
            revealed[row][col] = True
        if all(all(x) for x in revealed):
            print('Ganaste')
            break

# Ejecutar el juego
board = create_board(5, 5, 5)
play_game(board)