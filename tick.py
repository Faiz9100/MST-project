import tkinter as tk
from tkinter import messagebox


# Game logic
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.config(bg="lightblue")

        self.turn = "X"  # Player X starts first
        self.board = [[None for _ in range(3)] for _ in range(3)]  # 3x3 board

        # Create a 3x3 grid of buttons
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                               bg="white", command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

        # Restart button
        self.restart_button = tk.Button(self.root, text="Restart Game", font=("Arial", 14), bg="green",
                                        command=self.restart_game)
        self.restart_button.grid(row=3, column=0, columnspan=3, pady=10)

    def on_button_click(self, i, j):
        if self.board[i][j] is None:  # Only allow marking an empty spot
            self.board[i][j] = self.turn
            self.buttons[i][j].config(text=self.turn)
            if self.check_winner():
                self.show_winner(self.turn)
            elif self.check_draw():
                self.show_draw()
            else:
                self.turn = "O" if self.turn == "X" else "X"  # Switch turn

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != None:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != None:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != None:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != None:
            return True

        return False

    def check_draw(self):
        for row in self.board:
            if None in row:
                return False
        return True

    def show_winner(self, winner):
        messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
        self.disable_buttons()

    def show_draw(self):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        self.disable_buttons()

    def disable_buttons(self):
        # Disable all buttons after the game ends
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state="disabled")

    def restart_game(self):
        # Reset the game board and buttons
        self.board = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal")
        self.turn = "X"  # Reset to player X's turn


# Initialize the main window
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
