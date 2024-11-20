import tkinter as tk
from tkinter import messagebox
import random

# Dummy database for storing created users (for now)
users_db = {}


def show_account_creation_screen(root):
    def create_account():
        name = entry_name.get()
        surname = entry_surname.get()
        phone = entry_phone.get()
        id_number = entry_id_number.get()

        if name and surname and phone and id_number:
            # Generate the username as name@surname
            username = f"{name.lower()}@{surname.lower()}"

            # Generate a random account number (for simplicity)
            account_number = random.randint(100000, 999999)
            password = entry_password.get()

            # Save the new user to the "database"
            users_db[username] = {
                "name": name,
                "surname": surname,
                "phone": phone,
                "id_number": id_number,
                "account_number": account_number,
                "password": password,
                "balance": 0.0,
            }

            messagebox.showinfo("Account Created",
                                f"Account created successfully!\nYour username: {username}\nAccount Number: {account_number}")
            root.withdraw()
            show_login_screen(root)  # Navigate back to login after account creation
        else:
            messagebox.showerror("Input Error", "Please fill in all fields")

    # Create the account creation window
    create_window = tk.Toplevel(root)
    create_window.title("Create Account")
    create_window.geometry("300x350")

    tk.Label(create_window, text="Name").pack(pady=10)
    entry_name = tk.Entry(create_window)
    entry_name.pack(pady=5)

    tk.Label(create_window, text="Surname").pack(pady=10)
    entry_surname = tk.Entry(create_window)
    entry_surname.pack(pady=5)

    tk.Label(create_window, text="Phone").pack(pady=10)
    entry_phone = tk.Entry(create_window)
    entry_phone.pack(pady=5)

    tk.Label(create_window, text="ID Number").pack(pady=10)
    entry_id_number = tk.Entry(create_window)
    entry_id_number.pack(pady=5)

    tk.Label(create_window, text="Password").pack(pady=10)
    entry_password = tk.Entry(create_window, show="*")
    entry_password.pack(pady=5)

    create_button = tk.Button(create_window, text="Create Account", width=20, command=create_account)
    create_button.pack(pady=20)

    cancel_button = tk.Button(create_window, text="Cancel", width=20, command=create_window.destroy)
    cancel_button.pack(pady=10)

    # Back button to return to the Dashboard
    def back_to_dashboard():
        create_window.destroy()  # Close current window
        show_dashboard_screen(root, "")  # Open a new dashboard window (with no user logged in)

    back_button = tk.Button(create_window, text="Back to Dashboard", width=20, command=back_to_dashboard)
    back_button.pack(pady=10)
