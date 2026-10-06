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
expense-management-system/
├── frontend/ # Streamlit UI
│ ├── app.py
│ ├── add_update_ui.py
│ ├── analytics_by_category.py
│ └── analytics_by_months.py
├── backend/ # FastAPI server
│ ├── server.py
│ ├── db_helper.py
│ └── logging_setup.py
├── tests/ # Unit & integration tests
│ └── conftest.py
├── requirements.txt
├── .env.example
└── README.md

text

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/expense-management-system.git
cd expense-management-system
2. Install dependencies
bash
pip install -r requirements.txt
3. Configure environment variables
Create a .env file in the root directory:

text
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=expense_manager
4. Run the FastAPI backend
bash
uvicorn backend.server:app --reload
5. Run the Streamlit frontend
bash
streamlit run frontend/app.py
