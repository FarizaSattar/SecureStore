# 🔐 SecureStore

<p align="left">
  <img src="https://img.shields.io/badge/stack-Python%20%7C%20Tkinter%20%7C%20JSON-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/system-Local%20Credential%20Manager-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/security-Educational%20Project-orange?style=for-the-badge" />
</p>

---

## 🧠 Secure Credential Management System

**SecureStore** is a lightweight desktop password manager built with Python and Tkinter.  
It allows users to **generate, store, and retrieve credentials locally** through a simple GUI.

The project demonstrates core software engineering principles such as modular design, event-driven programming, and structured data persistence using JSON.

---

## 🚀 Why This Project Stands Out

✔ Clean modular Python architecture  
✔ Full GUI-based desktop application (Tkinter)  
✔ Secure password generation system  
✔ Fast credential lookup by website  
✔ Clipboard integration for usability  
✔ Lightweight offline-first design  
✔ Beginner-friendly but production-inspired structure  

---

## ⚠️ Security Model (Important)

SecureStore uses **local JSON-based storage** for simplicity.

⚠️ Credentials are stored in **plaintext (not encrypted)**.

This project is intended for **learning purposes only**, not production use.

### Planned Security Enhancements
- AES / RSA encryption for stored credentials  
- Master password authentication system  
- PBKDF2 / bcrypt password hashing  
- Secure key derivation (KDF)  
- Encrypted local database layer  

---

## 🏗️ System Architecture

```mermaid
flowchart LR
A[User Input (Tkinter UI)] --> B[Password Generator]
B --> C[Credential Manager]
C --> D[JSON Storage Layer]
C --> E[Clipboard Integration]
D --> F[Search & Retrieval Engine]
F --> A
```

---

## 🔄 Data Flow

User Input (Website + Email)  
→ Password Generation  
→ Credential Structuring  
→ JSON Storage  
→ Retrieval by Website  
→ Clipboard Copy (optional)

---

## ⚙️ Core Features

### 🔑 Password Generation
- Strong randomized password generator  
- Mixed character entropy (letters, digits, symbols)  
- Customizable length support  

### 💾 Credential Storage
- Stores website, email, password  
- Structured JSON-based persistence  
- Local file-based database system  

### 🔍 Credential Retrieval
- Fast lookup by website name  
- Simple search logic  
- Instant result display  

### 📋 Clipboard Support
- One-click copy using `pyperclip`  
- Seamless password usage  

### 🖥️ GUI Interface
- Built with Tkinter  
- Clean and minimal desktop UI  
- Beginner-friendly layout  

---

## 🧠 Key Engineering Concepts

- Event-driven GUI programming  
- Modular software architecture  
- File-based persistence systems  
- JSON data modeling  
- Secure random generation  
- Input validation & error handling  
- Separation of concerns  

---

## 🛠️ Tech Stack

- Python 3  
- Tkinter (GUI framework)  
- JSON (local storage)  
- pyperclip (clipboard automation)  
- random / string libraries  

---

## 📁 Project Structure

```
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
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/SecureStore.git
cd SecureStore
```

### 2. Install Dependencies
```bash
pip install pyperclip
```

### 3. Run Application
```bash
python main.py
```

---

## 📊 Example Credential Entry

```json
{
  "website": "github.com",
  "email": "user@example.com",
  "password": "a8#Kp2!xZ9"
}
```

---

## 🧩 System Modules

### 🧠 Password Generator
- Generates secure random passwords  
- Ensures entropy using mixed character sets  

### 💾 Storage Engine
- Reads/writes JSON file  
- Handles updates and overwrites safely  

### 🔍 Retrieval System
- Searches by website key  
- Returns stored credentials instantly  

### 🖥️ GUI Layer
- Tkinter-based interface  
- Handles user interaction & events  

---

## 📌 Use Cases

- Learning Python GUI development  
- Understanding password management systems  
- Practicing modular architecture design  
- Building foundation for secure applications  

---

## 🔐 Security Notes

- ❌ No encryption (currently plaintext storage)  
- ❌ No authentication system  
- ❌ Not suitable for real-world password storage  

---

## 🌱 Future Improvements

- AES encrypted local storage  
- Master password login system  
- Secure vault architecture  
- Auto-lock timeout system  
- Cloud sync option (optional)  
- UI redesign (modern Tkinter / customtkinter)  

---

## 📜 License

MIT License
```
