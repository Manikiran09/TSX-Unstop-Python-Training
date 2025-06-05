# 📁 Flask Portfolio Website

A personal portfolio website built with Flask, Bootstrap, SQLite, and Flask-Mail. It includes a contact form that stores messages in a database and sends an email notification.

---

## 🚀 Features

- Home, About, Projects, and Contact pages
- Contact form with form validation
- Messages stored in SQLite (`messages.db`)
- Email notifications using Flask-Mail
- Bootstrap for responsive design

---

## 📦 Requirements

- Python 3.8+
- pip

---

## 📚 Setup Instructions

### 1. Clone the Repository
git clone https://github.com/Manikiran09/TSX-Unstop-Python-Training
### 2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
### 3. Install Dependencies
pip install -r requirements.txt
### 4. Run the Application
python app.py

✅ Notes
Access stored messages at /messages

Use debug=False in production

Messages will be printed to terminal if email fails
