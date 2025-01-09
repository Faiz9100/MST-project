import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Guessing Game")
        self.geometry("400x300")
        self.configure(bg="#ffcc99")

        self.secret_number = random.randint(1, 100)  # Random number between 1 and 100
        self.attempts = 0

        # UI Elements
        self.create_ui()

    def create_ui(self):
        # Title label
        self.title_label = tk.Label(self, text="Guess the Number!", font=("Arial", 16), bg="#ffcc99")
        self.title_label.pack(pady=20)

        # Instruction label
        self.instruction_label = tk.Label(self, text="Enter a number between 1 and 100", font=("Arial", 12), bg="#ffcc99")
        self.instruction_label.pack(pady=10)

        # Entry for user's guess
        self.guess_entry = tk.Entry(self, font=("Arial", 14))
        self.guess_entry.pack(pady=10)

        # Submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess, font=("Arial", 12), bg="yellow", fg="black")
        self.submit_button.pack(pady=10)

        # Attempts label
        self.attempts_label = tk.Label(self, text="Attempts: 0", font=("Arial", 12), bg="#ffcc99")
        self.attempts_label.pack(pady=10)

        # Reset button
        self.reset_button = tk.Button(self, text="Reset Game", command=self.reset_game, font=("Arial", 12), bg="yellow", fg="black")
        self.reset_button.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number!")
            return

        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")

        if guess < self.secret_number:
            messagebox.showinfo("Too Low", "Your guess is too low. Try again!")
        elif guess > self.secret_number:
            messagebox.showinfo("Too High", "Your guess is too high. Try again!")
        else:
            messagebox.showinfo("Congratulations!", f"Correct! You guessed the number in {self.attempts} attempts.")
            self.reset_game()

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.attempts_label.config(text="Attempts: 0")
        self.guess_entry.delete(0, tk.END)


# Start the game
if __name__ == "__main__":
    game = NumberGuessingGame()
    game.mainloop()
