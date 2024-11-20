import tkinter as tk
from tkinter import messagebox
from gui.login import show_login_screen
from gui.acc_create import show_account_creation_screen
from gui.dashboard import show_dashboard_screen

# Create the main window (root)
root = tk.Tk()
root.title("Banking App")
root.geometry("400x300")

# Add buttons to navigate to different screens
def go_to_login():
    root.withdraw()  # Hide the main window
    show_login_screen(root)

def go_to_account_creation():
    root.withdraw()
    show_account_creation_screen(root)

# Main menu (Login or Account Creation)
label = tk.Label(root, text="Welcome to the Banking App")
label.pack(pady=20)

login_button = tk.Button(root, text="Login", width=20, command=go_to_login)
login_button.pack(pady=10)

account_button = tk.Button(root, text="Create Account", width=20, command=go_to_account_creation)
account_button.pack(pady=10)

# Start the app
root.mainloop()

