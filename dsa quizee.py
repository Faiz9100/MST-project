import tkinter as tk
from tkinter import messagebox, filedialog
import random
import time
import json

# Sample question set
questions = [
    {"question": "What is the time complexity of accessing an element in an array?", "choices": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "answer": "O(1)"},
    {"question": "Which data structure uses LIFO (Last In First Out) order?", "choices": ["Queue", "Stack", "Array", "Linked List"], "answer": "Stack"},
    {"question": "What is the best-case time complexity of QuickSort?", "choices": ["O(n log n)", "O(n^2)", "O(log n)", "O(1)"], "answer": "O(n log n)"},
]

class DSAQuizGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DSA Quiz Game")
        self.geometry("600x500")
        self.configure(bg="#ff7f7f")

        self.current_question = 0
        self.score = 0
        self.total_questions = len(questions)
        self.difficulty = "Easy"
        self.incorrect_answers = []

        # UI Elements
        self.create_ui()

    def create_ui(self):
        # Difficulty selection
        self.difficulty_var = tk.StringVar(value=self.difficulty)
        difficulty_frame = tk.Frame(self, bg="#ff7f7f")
        tk.Label(difficulty_frame, text="Select Difficulty:", bg="#ff7f7f", font=("Arial", 12)).pack(side="left", padx=10)
        for level in ["Easy", "Medium", "Hard"]:
            tk.Radiobutton(difficulty_frame, text=level, variable=self.difficulty_var, value=level, bg="#ff7f7f", font=("Arial", 12), command=self.set_difficulty).pack(side="left")
        difficulty_frame.pack(pady=10)

        # Question label
        self.question_label = tk.Label(self, text="Question will appear here", font=("Arial", 14), wraplength=500, bg="#ff7f7f", fg="white")
        self.question_label.pack(pady=20)

        self.choice_var = tk.StringVar()

        # Choice buttons
        self.choice_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self, text="", variable=self.choice_var, value="", font=("Arial", 12), bg="#ff7f7f", fg="white", selectcolor="black")
            btn.pack(anchor="w")
            self.choice_buttons.append(btn)

        # Submit button
        self.submit_button = tk.Button(self, text="Next", command=self.check_answer, font=("Arial", 12), bg='yellow', fg='black')
        self.submit_button.pack(pady=10)

        # Previous button
        self.previous_button = tk.Button(self, text="Previous", command=self.previous_question, font=("Arial", 12), bg='yellow', fg='black')
        self.previous_button.pack(pady=10)

        # Score label
        self.score_label = tk.Label(self, text="Score: 0", font=("Arial", 12), bg="#ff7f7f", fg="white")
        self.score_label.pack(pady=10)

        # Reset button
        self.reset_button = tk.Button(self, text="Restart", command=self.reset_game, font=("Arial", 12), bg='yellow', fg='black')
        self.reset_button.pack(pady=10)

        # Leaderboard button
        self.leaderboard_button = tk.Button(self, text="Leaderboard", command=self.show_leaderboard, font=("Arial", 12), bg='yellow', fg='black')
        self.leaderboard_button.pack(pady=10)

        # Upload questions
        self.upload_button = tk.Button(self, text="Upload Questions", command=self.upload_questions, font=("Arial", 12), bg='yellow', fg='black')
        self.upload_button.pack(pady=10)

        self.display_question()

    def display_question(self):
        question_data = questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        self.choice_var.set("")

        for i, choice in enumerate(question_data["choices"]):
            self.choice_buttons[i].config(text=choice, value=choice)

    def check_answer(self):
        selected_answer = self.choice_var.get()
        correct_answer = questions[self.current_question]["answer"]

        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Well Done! That's the right answer.")
        else:
            self.incorrect_answers.append((questions[self.current_question]["question"], correct_answer))
            messagebox.showerror("Incorrect", f"Sorry, the correct answer was: {correct_answer}")

        self.current_question += 1

        if self.current_question >= self.total_questions:
            self.end_game()
        else:
            self.display_question()

        self.score_label.config(text=f"Score: {self.score}")

    def previous_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.display_question()

    def end_game(self):
        result_message = f"Your final score is {self.score} out of {self.total_questions}"
        if self.incorrect_answers:
            result_message += "\n\nReview Incorrect Answers:\n"
            for question, answer in self.incorrect_answers:
                result_message += f"\n{question}\nCorrect Answer: {answer}\n"
        messagebox.showinfo("Quiz Over", result_message)
        self.submit_button.config(state=tk.DISABLED)

    def reset_game(self):
        self.score = 0
        self.current_question = 0
        self.incorrect_answers = []
        self.submit_button.config(state=tk.NORMAL)
        self.score_label.config(text=f"Score: {self.score}")
        self.display_question()

    def set_difficulty(self):
        self.difficulty = self.difficulty_var.get()

    def show_leaderboard(self):
        # Placeholder for leaderboard functionality
        messagebox.showinfo("Leaderboard", "Leaderboard feature coming soon!")

    def upload_questions(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    global questions
                    questions = json.load(file)
                    self.total_questions = len(questions)
                    self.reset_game()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load questions: {e}")

# Start the game
if __name__ == "__main__":
    game = DSAQuizGame()
    game.mainloop()
