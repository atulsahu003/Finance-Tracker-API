# 💰 Finance Tracker API

A backend REST API for managing personal finances, built with **FastAPI**, **SQLAlchemy**, **SQLite**, and **JWT Authentication**.

The API allows users to register and log in securely, manage their expenses, and organize financial records through protected REST endpoints.

---

## 🚀 Features

- 🔐 User Registration & Login
- 🔑 JWT-based Authentication
- 👤 Secure User Management
- 💸 Create and Manage Expenses
- 📋 Retrieve Expense Records
- ✏️ Update Expense Details
- 🗑️ Delete Expenses
- 🗄️ SQLite Database
- 🧩 Modular FastAPI Router Structure
- 📑 Pydantic Schemas for Request/Response Validation
- 🔒 Password Hashing & Authentication Security
- 📖 Automatic Swagger API Documentation

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| FastAPI | Backend REST API Framework |
| SQLAlchemy | ORM / Database Interaction |
| SQLite | Database |
| Pydantic | Data Validation |
| JWT | Authentication |
| Passlib | Password Hashing |
| Uvicorn | ASGI Server |

---

## 📁 Project Structure

```text
Finance-Tracker-API/
│
├── router/
│   ├── auth.py
│   └── expense.py
│
├── database.py
├── main.py
├── models.py
├── schemas.py
├── security.py
├── project.md
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/atulsahu003/Finance-Tracker-API.git
```

### 2. Navigate to the Project
```bash
cd Finance-Tracker-API
```

### 3. Create a Virtual Environment
```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 5. Install Dependencies
```bash
pip install fastapi uvicorn sqlalchemy pydantic python-jose passlib bcrypt
```

---

## ▶️ Run the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically provides interactive API documentation.

**Swagger UI**
```
http://127.0.0.1:8000/docs
```

**ReDoc**
```
http://127.0.0.1:8000/redoc
```

You can use Swagger UI to test the API endpoints directly from your browser.

---

## 🔐 Authentication Flow

The application uses JWT-based authentication.

**Authentication Process**
```
User Registration
       ↓
Password Hashing
       ↓
User Login
       ↓
JWT Token Generated
       ↓
Token Used for Protected Routes
       ↓
Authenticated API Access
```

Protected endpoints require a valid JWT access token.

---

## 🔗 Main API Modules

### Authentication
The authentication module handles:
- User registration
- User login
- Password verification
- JWT token generation

### Expense Management
The expense module handles:
- Creating expenses
- Retrieving expenses
- Updating expenses
- Deleting expenses

---

## 🗄️ Database

The project uses SQLite with SQLAlchemy ORM.

Database-related functionality is handled through:
- `database.py`
- `models.py`

The local SQLite database is intentionally excluded from Git using `.gitignore`.

---

## 🔒 Security

The project implements:
- Password hashing
- JWT authentication
- Protected API routes
- Authentication dependencies
- Request validation using Pydantic

> ⚠️ Never commit real API keys, passwords, secret keys, or `.env` files to GitHub.

---

## 🧪 Testing the API

After starting the server, open:

```
http://127.0.0.1:8000/docs
```

Use the Swagger interface to:
1. Register a user
2. Login
3. Obtain an access token
4. Authorize the API
5. Create an expense
6. Retrieve expenses
7. Update an expense
8. Delete an expense

---

## 🎯 Learning Objectives

This project demonstrates practical implementation of:
- REST API development
- FastAPI
- Authentication & Authorization
- JWT Tokens
- SQLAlchemy ORM
- Database Management
- Pydantic Data Validation
- Secure Password Handling
- Modular Backend Architecture

---

## 🔮 Future Improvements

Potential improvements include:
- 📊 Monthly and yearly expense analytics
- 📈 Expense visualization dashboard
- 🏷️ Expense categories
- 🔍 Advanced filtering and search
- 💰 Income tracking
- 📅 Date-based financial reports
- 📤 Export expenses to CSV/PDF
- ☁️ PostgreSQL integration
- 🐳 Docker support
- 🚀 Cloud deployment

---

## 👨‍💻 Author

**Atul Sahu**

GitHub: [https://github.com/atulsahu003](https://github.com/atulsahu003)
