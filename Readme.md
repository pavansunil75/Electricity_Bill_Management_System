**⚡ Electricity Bill Management System**



A Python and MySQL-based console application to manage electricity billing, customer profiles, and meter readings.





**📋 Billing Logic**

The total amount for the monthly bill is calculated using the following formula:



Bill Amount = (Current Reading - Previous Reading)\*7.00





**📁 Project Structure**

The repository consists of the following key files:



* main.py: The main executable Python script containing the application logic and interactive terminal menu.
* config.py: The configuration file containing database connection parameters.
* Database.sql: The SQL script to initialize the database tables and populate sample records.
* README.md: This instruction manual.





**🛠️ Step-by-Step Setup Guide**

Step 1: Install MySQL



If you do not have MySQL installed, download and install MySQL Server from the official website:

👉 https://dev.mysql.com/downloads/



Step 2: Create the Database

1. Open your MySQL Command Line Client or any MySQL tool (like MySQL Workbench).
2. Run the following command to log in:
mysql -u root -p
3. Copy the entire contents of the Database.sql file and run it inside your MySQL client. This will create the database electricity\_bill\_db, generate the tables, and insert pre-configured test users.



Step 3: Install Python Dependencies

Open your Command Prompt (Windows) or Terminal (Mac/Linux) and run this command to install the official MySQL connector library:



pip install mysql-connector-python



Step 4: Configure Your Password

1. Open the config.py file in a text editor.
2. Replace 'Password' with your actual MySQL local root password:
DATABASE\_CONFIG = {
    'host': 'localhost',
    'database': 'electricity\_bill\_db',
    'user': 'root',
    'password': 'YOUR\_ACTUAL\_MYSQL\_PASSWORD',  # Change this line
    'port': 3306
}
3. Save the file.



Step 5: Run the Application

Start the system by running the main Python file in your terminal:



python main.py





🎮 Menu Features



Once launched, the system presents an interactive menu with these choices:



1. Add New Customer: Register connection types (Residential, Commercial, Industrial).
2. Add Meter Reading: Track monthly readings for each customer ID.
3. Generate Bill: Automatically compute units consumed and total amount.
4. Display Bill: Generate a beautifully formatted receipt text with customer and reading breakdowns.
5. View All Customers: Print a summary list of all registered clients.
6. View All Bills: Review historical billing records and pay rates.
7. Update Payment Status: Mark bills as Paid, Pending, or Overdue.
8. Generate Bill for Random Customer: Run billing simulations on random profiles.
9. Delete Customer: Safely delete profiles and cascade-remove all their database logs.
10. Exit: Terminate the program and safely close the database link.

