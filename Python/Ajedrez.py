# Crear el tablero del ajedrez
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

# Función para imprimir el tablero
def print_board(board):
    for row in board:
        print('|'.join(row))

# Función para mover las piezas
def move_piece(board, start, end):
    x1, y1 = start
    x2, y2 = end
    piece = board[x1][y1]
    board[x1][y1] = ' '
    board[x2][y2] = piece
    return board

# Prueba de la función de movimiento de piezas
board = move_piece(board, (1, 0), (2, 0))
print_board(board)