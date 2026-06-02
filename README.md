# ⚡ Electricity Bill Management System

### Python & MySQL Database Project

This project is a console-based Electricity Bill Management System developed using Python and MySQL. It automates customer management, meter reading recording, bill generation, payment tracking, and billing reports.


## 📌 Project Overview

The Electricity Bill Management System helps electricity providers efficiently manage customer records, track meter readings, generate bills, and monitor payment status.

The system stores all information in a MySQL database and provides a menu-driven interface for easy operation.


## 🎯 Project Objectives

- Manage customer information.
- Record monthly meter readings.
- Automatically generate electricity bills.
- Calculate electricity consumption and billing amounts.
- Track payment status.
- Display billing history.
- Maintain customer and billing records using MySQL.


## 🛠 Technologies Used

- Python
- MySQL
- MySQL Connector Python
- SQL
- Object-Oriented Programming (OOP)


## 📊 System Features

### 👤 Customer Management

- Add new customers
- View all customers
- Delete customer records

### ⚡ Meter Reading Management

- Record monthly meter readings
- Store reading history

### 🧾 Bill Generation

- Automatic bill calculation
- Unit consumption calculation
- Due date generation
- Bill display and printing

### 💳 Payment Management

- Update payment status
- Mark bills as Paid, Pending, or Overdue
- Store payment dates

### 📋 Reports

- View all customers
- View all generated bills
- Display detailed bill information


## 🗄 Database Structure

The system uses three tables:

### Customers Table

| Field | Description |
|---------|-------------|
| customer_id | Unique customer ID |
| name | Customer name |
| address | Customer address |
| phone | Phone number |
| email | Email address |
| connection_type | Residential / Commercial / Industrial |
| registration_date | Registration date |

### Meter Readings Table

| Field | Description |
|---------|-------------|
| reading_id | Reading ID |
| customer_id | Customer reference |
| reading_month | Billing month |
| reading_date | Reading date |
| meter_reading | Meter value |

### Bills Table

| Field | Description |
|---------|-------------|
| bill_id | Bill ID |
| customer_id | Customer reference |
| bill_month | Billing month |
| previous_reading | Previous reading |
| current_reading | Current reading |
| units_consumed | Units used |
| rate_per_unit | Electricity rate |
| total_amount | Total bill amount |
| bill_date | Bill generation date |
| due_date | Due date |
| payment_status | Paid / Pending / Overdue |
| payment_date | Payment date |


## ⚙️ Installation

### Install Required Packages

```bash
pip install mysql-connector-python
```


## 🗄 Database Setup

1. Install MySQL Server.
2. Create a database:

```sql
CREATE DATABASE electricity_bill_db;
```

3. Execute the SQL script:

```sql
SOURCE Database.sql;
```

4. Update database credentials in `config.py`:

```python
DATABASE_CONFIG = {
    'host': 'localhost',
    'database': 'electricity_bill_db',
    'user': 'root',
    'password': 'your_password',
    'port': 3306
}
```


## ▶️ How to Run

```bash
python main.py
```


## 📋 Main Menu

```text
1. Add New Customer
2. Add Meter Reading
3. Generate Bill
4. Display Bill
5. View All Customers
6. View All Bills
7. Update Payment Status
8. Generate Bill for Random Customer
9. Delete Customer
10. Exit
```


## 📁 Project Structure

```text
Electricity_Bill_Management_System/
│
├── main.py
├── config.py
├── Database.sql
└── README.md
```


## 🔑 Bill Calculation Logic

```text
Units Consumed = Current Reading - Previous Reading

Total Bill Amount = Units Consumed × Rate Per Unit

Rate Per Unit = ₹7.00
```


## ✨ Sample Workflow

1. Add Customer
2. Add Meter Reading
3. Generate Bill
4. Display Bill
5. Update Payment Status
6. View Reports


## 🚀 Future Enhancements

- GUI using Tkinter
- Web Application using Flask/Django
- Online Payment Integration
- PDF Bill Generation
- Email Notifications
- Customer Login Portal
- Admin Dashboard


## 👨‍💻 Author

**Sunil Pavan Raja**

Bachelor of Technology (Artificial Intelligence and Data Science)

Prathyusha Engineering College

GitHub: https://github.com/pavansunil75


## 📄 License

This project is intended for educational and academic purposes.

---

⭐ If you found this project useful, consider giving it a star.
