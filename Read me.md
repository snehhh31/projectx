# ProjectX - Shop Inventory Management System by SNEH KESHARI

![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg?style=flat&logo=python)
![Database](https://img.shields.io/badge/MySQL-Connector-orange.svg?style=flat&logo=mysql)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat)

A Command-Line Interface (CLI) application built with Python and MySQL to streamline retail store inventory, track goods, manage suppliers, and handle stock updates in real time.

---

## Key Features

- Inventory Tracking: Insert, view, search, and delete product records.
- Selective & Bulk Search:
  - Full-inventory overview with tabulated output.
  - Search items by product name, place of origin, or company name.
  - Quick-view summary (Item Name, Code, Quantity, Size, Price).
- Field-Level Updates: Update specific product attributes independently (Price, Quantity, Brand, Size, Contact, and Origin).
- Automated Database Setup: Connects to MySQL and initializes the database (Projectrec_1) and table (goodsinfo) automatically if they do not exist.
- SQL Injection Safe: Uses parameterized queries to prevent SQL syntax errors and security vulnerabilities.

---

## Tech Stack

- Language: Python 3.x
- Database: MySQL
- Driver: mysql-connector-python

---

## Project Structure

ProjectX/
├── ProjectX.py          # Main application script
├── requirements.txt     # Python package dependencies
├── schema.sql           # Database schema & table definitions
├── .gitignore           # Ignored temporary and environment files
└── README.md            # Project documentation
---

## Prerequisites

Before running the application, make sure you have:
- [Python 3.8+](https://www.python.org/downloads/) installed
- [MySQL Server](https://dev.mysql.com/downloads/mysql/) installed and running locally

---

## Installation & Setup

1. Clone the repository:
  
   git clone [https://github.com/snehhh31/ProjectX.git](https://github.com/snehhh31/ProjectX.git)
   cd ProjectX
   
2. Install required dependencies:
  
   pip install -r requirements.txt
   
3. Run the application:
  
   python ProjectX.py
   
4. Connect to your Database:
   - When prompted, provide your MySQL host (localhost by default), username (root by default), and your MySQL root password.
   - The required database (Projectrec_1) and table (goodsinfo) will be created automatically.

---

## Database Schema

If you prefer setting up the database manually via MySQL Workbench or the MySQL CLI:

CREATE DATABASE IF NOT EXISTS Projectrec_1;
USE Projectrec_1;

CREATE TABLE IF NOT EXISTS goodsinfo (
    Code INT PRIMARY KEY,
    Item_name VARCHAR(100),
    Size VARCHAR(20),
    Item_quantity VARCHAR(50),
    Item_price INT,
    Company_name VARCHAR(100),
    Mobileno VARCHAR(20),
    Place_of_origin VARCHAR(100)
);
---

## Author

- Sneh Kumar - [@snehhh31](https://github.com/snehhh31)[span_0](start_span)[span_0](end_span)
- Email: kesharisneh25@gmail.com

---

## License

This project is open-source and available under the [MIT License](LICENSE).