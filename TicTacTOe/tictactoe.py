def make_move(board, player):
    while True:
        coordinates = input("Enter the coordinates: ").split()
        if len(coordinates) != 2 or not coordinates[0].isdigit() or not coordinates[1].isdigit():
            print("You should enter numbers!")
            continue

        row, col = map(int, coordinates)
        if not (1 <= row <= 3) or not (1 <= col <= 3):
            print("Coordinates should be from 1 to 3!")
            continue

        row -= 1  # зменшуємо на 1, оскільки індексація починається з 0
        col -= 1

        if board[row][col] == "_":
            board[row][col] = player
            break
        else:
            print("This cell is occupied! Choose another one!")

def print_board(board):
    print("---------")
    for row in board:
        print("|", " ".join(row), "|")
    print("---------")

# ініціалізація порожньої ігрової дошки
board = [["_"] * 3 for _ in range(3)]

# основний ігровий цикл
while True:
    print_board(board)
    make_move(board, "X")
    print_board(board)

    # перевірка на перемогу X
    if any(all(cell == "X" for cell in row) for row in board) or \
            any(all(board[row][col] == "X" for row in range(3)) for col in range(3)) or \
            all(board[i][i] == "X" for i in range(3)) or \
            all(board[i][2 - i] == "X" for i in range(3)):
        print("X wins")
        break

    make_move(board, "O")
    print_board(board)

    # перевірка на перемогу O
    if any(all(cell == "O" for cell in row) for row in board) or \
            any(all(board[row][col] == "O" for row in range(3)) for col in range(3)) or \
            all(board[i][i] == "O" for i in range(3)) or \
            all(board[i][2 - i] == "O" for i in range(3)):
        print("O wins")
        break
