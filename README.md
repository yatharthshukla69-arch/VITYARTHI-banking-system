#  Real Banking System (CLI - Python)

 Project Overview

The **Real Banking System** is a Command Line Interface (CLI) based application developed using Python. It simulates real-world banking operations such as account creation, secure login, deposit, withdrawal, balance checking, and money transfer.

The system uses **file handling (TXT file)** for data storage instead of JSON or databases, making it simple and easy to understand.

---

 Problem Statement

Manual banking operations are inefficient and prone to errors. There is a need for a digital system that can automate financial transactions and securely manage user data.

---

 Features

 Create new bank account
   Secure login using PIN
   Deposit money
   Withdraw money
   Check account balance
   Transfer money between accounts
  File-based storage (No JSON, No Database)

---

 Technologies Used

* Python
* File Handling (`open`, `read`, `write`)

---

 How It Works

1. User creates an account with account number and PIN
2. User logs in using credentials
3. After login, user can perform banking operations
4. Data is stored and updated in a text file (`bank_data.txt`)



---
 Sample Output
 REAL BANKING SYSTEM 
1. Create Account
2. Login
3. Exit

Enter choice: 1
Enter your name: Rahul
Enter account number: 101
Set PIN: 1234

 Account created successfully!


---
 Project Structure


banking-system/
│── main.py
│── bank_data.txt
│── README.md
│── report.pdf
---

 Real-World Applications

* Banking system simulation
* Financial transaction systems
* Educational learning tools



 Learning Outcomes

* Understanding file handling in Python
* Implementing authentication systems
* Managing structured data
* Building CLI-based applications



 Limitations

* No database integration
* No encryption/security layer
* CLI-based (no GUI)


 Future Enhancements

* Add database (SQLite/MySQL)
* Implement GUI using Tkinter
* Add transaction history
* Add encryption and security features
* AI-based fraud detection



 Author

Name: Yatharth Shukla
Reg No: 25BAI10751
Department: CSE - AIML
Course: CSA2001 (Fundamentals of AI & ML)
