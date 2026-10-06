# 💰 Expense Management System

A full-stack expense tracking application that helps users log daily expenses, analyze spending patterns by category, and visualize monthly trends through an interactive dashboard.

## 🚀 Features

- **Add / Update Expenses** — Log daily expenses with amount, category, and notes
- **Category Analytics** — Visualize spending breakdown by category with percentages
- **Monthly Summary** — Track and compare monthly expense trends with charts
- **REST API Backend** — Clean FastAPI endpoints for all operations
- **MySQL Persistence** — Reliable data storage with connection pooling
- **Logging** — Structured logging for debugging and audit trails

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Database | MySQL |
| Data Handling | Pandas |
| Testing | Pytest |
| Logging | Python `logging` |

## 📁 Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AnuraagSaxena02/Expense-Management-System.git
   cd Expense-Management-System
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```
