import tkinter as tk
from tkinter import messagebox

# Dummy data for login (for now, we use this hardcoded)
users_db = {
    "user1": {"password": "password123", "balance": 1000},
    "user2": {"password": "password456", "balance": 2000},
}

def show_login_screen(root):
    def authenticate_user():
        username = entry_username.get()
        password = entry_password.get()

        # Check if the username exists and the password is correct
        if username in users_db and users_db[username]["password"] == password:
            messagebox.showinfo("Login Successful", f"Welcome {username}!")
            root.withdraw()  # Hide the main window
            show_dashboard_screen(root, username)  # Show the dashboard screen
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    # Create the login window
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry("300x200")

    tk.Label(login_window, text="Username").pack(pady=10)
    entry_username = tk.Entry(login_window)
    entry_username.pack(pady=5)

    tk.Label(login_window, text="Password").pack(pady=10)
    entry_password = tk.Entry(login_window, show="*")
    entry_password.pack(pady=5)

    login_button = tk.Button(login_window, text="Login", width=20, command=authenticate_user)
    login_button.pack(pady=20)

    cancel_button = tk.Button(login_window, text="Cancel", width=20, command=login_window.destroy)
    cancel_button.pack(pady=10)

    # Back button to return to the Dashboard
    def back_to_dashboard():
        login_window.destroy()  # Close current window
        show_dashboard_screen(root, "")  # Open a new dashboard window (with no user logged in)

    back_button = tk.Button(login_window, text="Back to Dashboard", width=20, command=back_to_dashboard)
    back_button.pack(pady=10)
