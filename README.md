# 🔑 SecureStore
### A friendly little tool for managing passwords — and learning how password managers work under the hood

## 👋 What is this?

Be honest: how many of your passwords are the same one, just with a number swapped at the end? Most of us know password reuse is risky, but creating (and remembering) a unique strong password for every single account is genuinely annoying.

SecureStore is a lightweight desktop app, built with Python and Tkinter, that generates, stores, and retrieves your login credentials through a simple, clean interface. I built it partly to make my own password habits better, and partly because building a password manager from scratch is a great way to really understand how these tools work — data storage, secure password generation, and clean interface design, all in one project.

## ❓ Why I built this

I wanted something simple that centralizes my passwords without needing a full commercial product — and building it myself meant I got to learn the actual mechanics behind credential management: how to structure the data, how to generate genuinely random passwords, and how to keep the whole thing organized and easy to extend later.

## 🚀 What it actually does

With SecureStore, you can:

- Enter a website or app name, plus your email or username.
- Generate a strong, random password (or type your own).
- Save it all to a local database.
- Search your saved credentials by website.
- Copy a password straight to your clipboard when you need it.

Behind the scenes, the password generator, storage engine, and interface are all separate, modular pieces — which makes the code easier to follow and simple to build on later.

## 📈 A quick example

Say you're signing up for a new account.

**Without SecureStore:** you'd probably make up a password on the spot (likely reused from somewhere else), maybe jot it down somewhere unsafe, and hope you remember it later.

**With SecureStore:** you type in the website and your email, click generate for a strong random password, and save it. Next time you need it, just search by website name and copy it straight to your clipboard. Simple as that.

## 👥 Who this is for

- Python developers or CS students wanting a beginner-friendly project to learn from
- Anyone curious how password managers actually work internally
- Folks learning Tkinter and GUI development for the first time
- Cybersecurity students interested in credential management fundamentals

## 🛠️ What you'll need to run it

**Software:** Python 3.10+, pip, Git (optional)

**One package to install:**
```
pip install pyperclip
```

**Helpful background:** basic Python, working with JSON, and some Tkinter familiarity — though it's designed to be approachable even as a first GUI project.

## 💡 How it flows, visually

```
User Opens Application
        │
        ▼
Enter Website & Email
        │
        ▼
Generate or Enter Password
        │
        ▼
Save Credentials
        │
        ▼
JSON Storage
        │
        ▼
Search by Website
        │
        ▼
Retrieve Credentials
        │
        ▼
Copy Password to Clipboard
```

## ⚠️ An important honest note

Right now, SecureStore stores credentials in a plain JSON file — **not encrypted**. This project is meant to show how a password manager's architecture works, not to be a secure vault. **Please don't use it to store your real passwords just yet!**

Encryption, master password authentication, and secure key derivation are all on the roadmap — once those are in place, it'll be a very different story. For now, think of this as the well-organized skeleton that real security features will eventually attach to.

## 🧰 Built with

Python · Tkinter
