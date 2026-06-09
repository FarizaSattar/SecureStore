# 🔐 SecureStore - Password Manager 

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
from pathlib import Path

# ---------------------------- CONSTANTS ------------------------------- #

DATA_FILE = Path("data.json")

LETTERS = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
NUMBERS = list("0123456789")
SYMBOLS = list("!#$%&()*+")

DEFAULT_EMAIL = "user@example.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """Generate a strong random password and copy it to clipboard."""

    password_chars = (
        [choice(LETTERS) for _ in range(randint(8, 12))] +
        [choice(SYMBOLS) for _ in range(randint(2, 4))] +
        [choice(NUMBERS) for _ in range(randint(2, 4))]
    )

    shuffle(password_chars)
    password = "".join(password_chars)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)

    messagebox.showinfo(title="Password Generated", message="Password copied to clipboard!")

# ---------------------------- DATA HANDLING ------------------------------- #

def load_data():
    """Load existing JSON data safely."""
    if not DATA_FILE.exists():
        return {}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}

def save_data(data):
    """Write data safely to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    """Save website credentials to local JSON file."""

    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not password:
        messagebox.showwarning(
            title="Missing Fields",
            message="Website and Password fields cannot be empty."
        )
        return

    new_entry = {
        website: {
            "email": email,
            "password": password
        }
    }

    data = load_data()
    data.update(new_entry)
    save_data(data)

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()

    messagebox.showinfo(title="Success", message=f"Credentials saved for {website}")

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    """Retrieve stored credentials for a website."""

    website = website_entry.get().strip()

    if not website:
        messagebox.showwarning(title="Input Required", message="Please enter a website name.")
        return

    data = load_data()

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]

        pyperclip.copy(password)

        messagebox.showinfo(
            title=website,
            message=f"Email: {email}\nPassword: {password}\n\n(Password copied to clipboard)"
        )
    else:
        messagebox.showerror(title="Not Found", message=f"No details found for {website}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("SecureStore Password Manager")
window.config(padx=50, pady=50)

# Canvas / Logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")  # keep logo in same folder
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
Label(text="Website:").grid(row=1, column=0)
Label(text="Email/Username:").grid(row=2, column=0)
Label(text="Password:").grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, DEFAULT_EMAIL)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
Button(text="Search", width=13, command=find_password).grid(row=1, column=2)
Button(text="Generate Password", command=generate_password).grid(row=3, column=2)
Button(text="Add", width=36, command=save_password).grid(row=4, column=1, columnspan=2)

window.mainloop()
