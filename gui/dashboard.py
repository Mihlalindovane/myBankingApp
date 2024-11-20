import tkinter as tk
from tkinter import messagebox

# Dummy users data (for testing)
users_db = {
    "user1": {"password": "password123", "balance": 1000},
    "user2": {"password": "password456", "balance": 2000},
}

def show_dashboard_screen(root, username):
    def deposit():
        amount = float(entry_deposit.get())
        if amount > 0:
            users_db[username]["balance"] += amount
            messagebox.showinfo("Deposit Successful", f"Deposited ${amount}. New balance: ${users_db[username]['balance']}")
        else:
            messagebox.showerror("Invalid Amount", "Amount should be greater than 0")

    def withdraw():
        amount = float(entry_withdraw.get())
        if amount <= users_db[username]["balance"]:
            users_db[username]["balance"] -= amount
            messagebox.showinfo("Withdrawal Successful", f"Withdrew ${amount}. New balance: ${users_db[username]['balance']}")
        else:
            messagebox.showerror("Insufficient Funds", "Not enough balance to withdraw")

    # Create the dashboard window
    dashboard_window = tk.Toplevel(root)
    dashboard_window.title("Dashboard")
    dashboard_window.geometry("400x300")

    # Title and balance info
    tk.Label(dashboard_window, text=f"Welcome {username}", font=("Arial", 16)).pack(pady=10)

    tk.Label(dashboard_window, text="Balance:").pack(pady=5)
    balance_label = tk.Label(dashboard_window, text=f"${users_db[username]['balance']}", font=("Arial", 14))
    balance_label.pack(pady=5)

    # Deposit and Withdraw sections
    tk.Label(dashboard_window, text="Deposit Amount:").pack(pady=5)
    entry_deposit = tk.Entry(dashboard_window)
    entry_deposit.pack(pady=5)

    deposit_button = tk.Button(dashboard_window, text="Deposit", width=20, command=deposit)
    deposit_button.pack(pady=10)

    tk.Label(dashboard_window, text="Withdraw Amount:").pack(pady=5)
    entry_withdraw = tk.Entry(dashboard_window)
    entry_withdraw.pack(pady=5)

    withdraw_button = tk.Button(dashboard_window, text="Withdraw", width=20, command=withdraw)
    withdraw_button.pack(pady=10)

    # Back button to return to the Dashboard
    def back_to_dashboard():
        dashboard_window.destroy()  # Close current window
        show_dashboard_screen(root, username)  # Open a new dashboard window

    back_button = tk.Button(dashboard_window, text="Back to Dashboard", width=20, command=back_to_dashboard)
    back_button.pack(pady=10)

    logout_button = tk.Button(dashboard_window, text="Logout", width=20, command=dashboard_window.destroy)
    logout_button.pack(pady=10)
