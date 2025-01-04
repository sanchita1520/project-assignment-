def print_board(board):
    print("\n" + "\n---------\n".join(" | ".join(row) for row in board))

def check_winner(board, player):
    return any(all(cell == player for cell in row) for row in board) or \
           any(all(board[row][col] == player for row in range(3)) for col in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2-i] == player for i in range(3))

def play_game():
    board = [[" "] * 3 for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic Tac Toe! Player X and Player O take turns.")
    while True:
        print_board(board)
        try:
            row, col = map(int, input(f"Player {players[current_player]}'s turn. Enter row and column (0, 1, 2): ").split())
            if board[row][col] != " ":
                print("Cell already taken.")
                continue
            board[row][col] = players[current_player]
            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                break
            if all(cell != " " for row in board for cell in row):
                print_board(board)
                print("It's a draw!")
                break
            current_player = 1 - current_player
        except (ValueError, IndexError):
            print("Invalid input. Please enter numeric values between 0 and 2 for both row and column.")

if __name__ == "__main__":
    play_game()
