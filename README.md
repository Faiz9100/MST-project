# Tic-Tac-Toe Game

This is a simple Tic-Tac-Toe game implemented using Python and Tkinter.

## How to Run

1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone this repository or download the source code.

3. Navigate to the project directory.

4. Run the following command to start the game:

    ```sh
    python tick.py
    ```

## Game Rules

- The game is played on a 3x3 grid.
- Player X always goes first.
- Players take turns placing their marks (X or O) in empty squares.
- The first player to get 3 of their marks in a row (horizontally, vertically, or diagonally) wins.
- If all 9 squares are filled and neither player has 3 marks in a row, the game is a draw.

## Workflow

1. **Initialize the Game**: The game starts with an empty 3x3 grid and Player X's turn.
2. **Player Move**: Players take turns to click on an empty cell to place their mark (X or O).
3. **Check for Winner**: After each move, the game checks if there is a winner.
4. **Check for Draw**: If all cells are filled and there is no winner, the game ends in a draw.
5. **End Game**: The game displays a message indicating the winner or if it's a draw, and disables further moves.
6. **Restart Game**: Players can click the "Restart Game" button to reset the board and start a new game.

## Files

- `tick.py`: The main script that contains the game logic and UI implementation.

## Dependencies

- `tkinter`: This module is part of the standard Python library, so you don't need to install anything extra.

## License

This project is licensed under the MIT License.
