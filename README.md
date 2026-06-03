# 🔐 SecureStore  
### Secure Credential Management System (Python + Tkinter)

---

## 📌 Overview

SecureStore is a lightweight desktop credential management system built in Python. It enables users to generate, store, and retrieve login credentials through a simple graphical interface.

The project demonstrates core software engineering principles including modular design, structured data persistence, and basic security-aware credential handling workflows.

---

## ⚠️ Security Model

This application uses a **local JSON-based storage system** to persist credentials.

> ⚠️ Important: This project is intended for educational purposes and does not implement production-grade security. Credentials are stored in plaintext.

### Future security improvements:
- AES/RSA encryption for stored credentials
- Master password authentication system
- Secure key derivation functions (KDF)
- Password hashing using PBKDF2 or bcrypt

---

## ⚙️ Core Features

### 🔑 Password Generation
- Generates strong randomized passwords
- Uses mixed character sets to increase entropy

### 💾 Credential Storage
- Stores website, email, and password mappings
- Uses structured JSON-based local persistence

### 🔍 Credential Retrieval
- Fast lookup by website name
- Simple search and retrieval logic

### 📋 Clipboard Support
- One-click password copy using system clipboard (`pyperclip`)

### 🖥️ Graphical User Interface
- Built using Tkinter
- Simple and intuitive desktop UI

---

## 🏗️ System Architecture

### Components

- **Tkinter Frontend** → User Interface Layer  
- **Password Generator Module** → Password creation logic  
- **Storage Layer (JSON)** → Local persistence system  
- **Retrieval Engine** → Credential search logic  
- **Clipboard Interface** → System clipboard integration  

---

## 🔄 Data Flow

1. User enters website and email  
2. System generates a secure password  
3. Credential is stored in JSON database  
4. User searches credentials by website  
5. Password is copied to clipboard if needed  

---

## 🧠 Key Engineering Concepts

- File-based data persistence  
- Structured JSON data modeling  
- Event-driven GUI programming (Tkinter)  
- Random password generation  
- Input validation and error handling  
- Modular software design  

---

## 🛠️ Tech Stack

- Python 3  
- Tkinter (GUI framework)  
- JSON (data storage)  
- pyperclip (clipboard automation)  

---

## 📁 Recommended Code Structure

```bash
SecureStore/
│
├── main.py
├── gui.py
├── password_generator.py
├── storage.py
├── utils.py
│
└── data/
    └── passwords.json
