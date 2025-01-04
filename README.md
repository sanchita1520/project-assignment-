#Tic Tac Toe Game in Python

This is a simple implementation of the classic Tic Tac Toe game in Python, where two players (Player X and Player O) take turns to place their marks on a 3x3 grid. The game checks for a winner or a draw after each move.

#Features

2-player Mode: Players take turns to make their moves.
Winner Check: The game automatically detects if a player has won.
Draw Check: The game recognizes when the board is full, leading to a draw.
Input Validation: Ensures valid moves (no out-of-bounds or already filled cells).

#How to Play
1. Run the Python script sk.py.
2. The game will display an empty Tic Tac Toe board.
3. Players take turns to enter the row and column number where they want to place their mark (X or O).
4. Row and column numbers are from 0 to 2.
5. The game will announce the winner as soon as there’s one, or if the game ends in a draw.
6. The board is displayed at the start of every turn.
7. Players enter their move as two numbers, separated by a space (e.g., 1 2 for row 1, column 2).
8. If a player wins (all their marks are in a row, column, or diagonal), the game ends, and the winner is announced.
9. If all cells are filled and no winner, the game ends in a draw.

#Example Input
vbnet
Player X's turn. Enter row and column (0, 1, 2): 0 0
Example Output
vbnet
1. Player X's turn. Enter row and column (0, 1, 2): 1 1
2. Player O's turn. Enter row and column (0, 1, 2): 0 2
3. Player X's turn. Enter row and column (0, 1, 2): 2 2
4. Player X wins!

#. Requirements
1. Python 3.x

#. How to Run
1. Download the sk.py file.
2. Open a terminal or command prompt.
3. Run the script using Python:
      python sk.py

#Contributing
Feel free to fork this repository, submit pull requests, or raise issues if you find bugs or want to suggest improvements.
