import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Expense Tracker")

# Create lists to hold expenses and categories
expenses = []
categories = []


# Function to add an expense
def add_expense():
    try:
        # Get the amount in INR
        amount_inr = float(entry_amount.get())
        category = entry_category.get()

        if amount_inr <= 0:
            messagebox.showerror("Error", "Amount should be greater than zero.")
            return

        # Append to the expenses and categories list
        expenses.append(amount_inr)
        categories.append(category)

        # Insert into listbox showing INR value
        listbox_expenses.insert(tk.END, f"{category}: ₹{amount_inr:.2f}")

        # Clear input fields
        entry_amount.delete(0, tk.END)
        entry_category.delete(0, tk.END)

        # Recalculate and display the total expenses in INR
        calculate_total()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")


# Function to calculate total expenses
def calculate_total():
    total_expenses_inr = sum(expenses)  # Expenses are in INR now
    label_total.config(text=f"Total Expenses: ₹{total_expenses_inr:.2f}")


# Function to clear all expenses
def clear_all():
    expenses.clear()
    categories.clear()
    listbox_expenses.delete(0, tk.END)
    label_total.config(text="Total Expenses: ₹0.00")


# Create and place the widgets
label_amount = tk.Label(root, text="Amount in INR:")
label_amount.grid(row=0, column=0, padx=10, pady=10)

entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1, padx=10, pady=10)

label_category = tk.Label(root, text="Category:")
label_category.grid(row=1, column=0, padx=10, pady=10)

entry_category = tk.Entry(root)
entry_category.grid(row=1, column=1, padx=10, pady=10)

button_add = tk.Button(root, text="Add Expense", command=add_expense)
button_add.grid(row=2, column=0, columnspan=2, pady=10)

label_total = tk.Label(root, text="Total Expenses: ₹0.00")
label_total.grid(row=3, column=0, columnspan=2, pady=10)

button_clear = tk.Button(root, text="Clear All", command=clear_all)
button_clear.grid(row=4, column=0, columnspan=2, pady=10)

listbox_expenses = tk.Listbox(root, width=40, height=10)
listbox_expenses.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
