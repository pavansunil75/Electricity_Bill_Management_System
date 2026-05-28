import mysql.connector
from datetime import datetime
import random

class ElectricityBillSystem:
    def __init__(self):
        self.connection = None
        self.cursor = None
        
    def connect_database(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='electricity_bill_db',
                user='root',
                password='Password' #Change to your Actual Password
            )
            
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("Connected to database successfully")
                return True
                
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def create_tables(self):
        try:
            create_customers = """
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                address VARCHAR(255) NOT NULL,
                phone VARCHAR(15) NOT NULL,
                email VARCHAR(100),
                connection_type VARCHAR(50) DEFAULT 'Residential',
                registration_date DATE NOT NULL
            )
            """
            
            create_readings = """
            CREATE TABLE IF NOT EXISTS meter_readings (
                reading_id INT AUTO_INCREMENT PRIMARY KEY,
                customer_id INT NOT NULL,
                reading_month VARCHAR(20) NOT NULL,
                reading_date DATE NOT NULL,
                meter_reading INT NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            )
            """
            
            create_bills = """
            CREATE TABLE IF NOT EXISTS bills (
                bill_id INT AUTO_INCREMENT PRIMARY KEY,
                customer_id INT NOT NULL,
                bill_month VARCHAR(20) NOT NULL,
                previous_reading INT NOT NULL,
                current_reading INT NOT NULL,
                units_consumed INT NOT NULL,
                rate_per_unit DECIMAL(10, 2) DEFAULT 7.00,
                total_amount DECIMAL(10, 2) NOT NULL,
                bill_date DATE NOT NULL,
                due_date DATE NOT NULL,
                payment_status VARCHAR(20) DEFAULT 'Pending',
                payment_date DATE,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            )
            """
            
            self.cursor.execute(create_customers)
            self.cursor.execute(create_readings)
            self.cursor.execute(create_bills)
            self.connection.commit()
            print("Tables created successfully")
            
        except Exception as e:
            print(f"Error: {e}")
    
    def add_customer(self, name, address, phone, email, connection_type):
        try:
            query = """
            INSERT INTO customers (name, address, phone, email, connection_type, registration_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (name, address, phone, email, connection_type, datetime.now().date())
            
            self.cursor.execute(query, values)
            self.connection.commit()
            
            print(f"Customer added: {name} (ID: {self.cursor.lastrowid})")
            return self.cursor.lastrowid
            
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def add_meter_reading(self, customer_id, reading_month, meter_reading):
        try:
            query = """
            INSERT INTO meter_readings (customer_id, reading_month, reading_date, meter_reading)
            VALUES (%s, %s, %s, %s)
            """
            values = (customer_id, reading_month, datetime.now().date(), meter_reading)
            
            self.cursor.execute(query, values)
            self.connection.commit()
            
            print(f"Meter reading added: {meter_reading} units")
            return True
            
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def generate_bill(self, customer_id, current_month):
        try:
            current_query = """
            SELECT meter_reading FROM meter_readings
            WHERE customer_id = %s AND reading_month = %s
            ORDER BY reading_date DESC LIMIT 1
            """
            self.cursor.execute(current_query, (customer_id, current_month))
            current_result = self.cursor.fetchone()
            
            if not current_result:
                print("No current month reading found")
                return None
            
            current_reading = current_result[0]
            
            previous_query = """
            SELECT meter_reading FROM meter_readings
            WHERE customer_id = %s AND reading_month != %s
            ORDER BY reading_date DESC LIMIT 1
            """
            self.cursor.execute(previous_query, (customer_id, current_month))
            previous_result = self.cursor.fetchone()
            
            if not previous_result:
                print("No previous month reading found")
                return None
            
            previous_reading = previous_result[0]
            
            units_consumed = current_reading - previous_reading
            rate_per_unit = 7.00
            total_amount = units_consumed * rate_per_unit
            
            bill_query = """
            INSERT INTO bills (customer_id, bill_month, previous_reading, current_reading,
                             units_consumed, rate_per_unit, total_amount, bill_date, due_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, DATE_ADD(%s, INTERVAL 15 DAY))
            """
            bill_date = datetime.now().date()
            values = (customer_id, current_month, previous_reading, current_reading,
                     units_consumed, rate_per_unit, total_amount, bill_date, bill_date)
            
            self.cursor.execute(bill_query, values)
            self.connection.commit()
            
            bill_id = self.cursor.lastrowid
            print(f"Bill generated successfully (ID: {bill_id})")
            
            return bill_id
            
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def display_bill(self, bill_id):
        try:
            query = """
            SELECT b.bill_id, c.customer_id, c.name, c.address, c.phone, c.connection_type,
                   b.bill_month, b.previous_reading, b.current_reading, b.units_consumed,
                   b.rate_per_unit, b.total_amount, b.bill_date, b.due_date, 
                   b.payment_status, b.payment_date
            FROM bills b
            JOIN customers c ON b.customer_id = c.customer_id
            WHERE b.bill_id = %s
            """
            
            self.cursor.execute(query, (bill_id,))
            result = self.cursor.fetchone()
            
            if not result:
                print("Bill not found")
                return
            
            (bill_id, customer_id, name, address, phone, connection_type,
             bill_month, prev_reading, curr_reading, units_consumed,
             rate_per_unit, total_amount, bill_date, due_date,
             payment_status, payment_date) = result
            
            print("\n" + "="*70)
            print("ELECTRICITY BILL")
            print("="*70)
            print(f"\nBill ID: {bill_id}")
            print(f"Bill Date: {bill_date}")
            print(f"Due Date: {due_date}")
            print("\n" + "-"*70)
            print("CUSTOMER INFORMATION")
            print("-"*70)
            print(f"Customer ID      : {customer_id}")
            print(f"Name             : {name}")
            print(f"Address          : {address}")
            print(f"Phone            : {phone}")
            print(f"Connection Type  : {connection_type}")
            print("\n" + "-"*70)
            print("METER READING DETAILS")
            print("-"*70)
            print(f"Billing Month    : {bill_month}")
            print(f"Previous Reading : {prev_reading} units")
            print(f"Current Reading  : {curr_reading} units")
            print(f"Units Consumed   : {units_consumed} units")
            print(f"Rate per Unit    : Rs.{rate_per_unit:.2f}")
            print("\n" + "-"*70)
            print("BILLING SUMMARY")
            print("-"*70)
            print(f"Total Amount     : Rs.{total_amount:.2f}")
            print(f"Payment Status   : {payment_status}")
            if payment_date:
                print(f"Payment Date     : {payment_date}")
            print("="*70 + "\n")
            
        except Exception as e:
            print(f"Error: {e}")
    
    def get_random_customer(self):
        try:
            query = "SELECT customer_id, name FROM customers"
            self.cursor.execute(query)
            customers = self.cursor.fetchall()
            
            if customers:
                return random.choice(customers)
            return None
            
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def view_all_customers(self):
        try:
            query = "SELECT customer_id, name, phone, connection_type FROM customers"
            self.cursor.execute(query)
            customers = self.cursor.fetchall()
            
            if not customers:
                print("No customers found")
                return
            
            print("\n" + "="*70)
            print("ALL CUSTOMERS")
            print("="*70)
            print(f"{'ID':<8} {'Name':<25} {'Phone':<15} {'Type':<15}")
            print("-"*70)
            
            for customer in customers:
                print(f"{customer[0]:<8} {customer[1]:<25} {customer[2]:<15} {customer[3]:<15}")
            
            print("="*70 + "\n")
            
        except Exception as e:
            print(f"Error: {e}")
    
    def view_all_bills(self):
        try:
            query = """
            SELECT b.bill_id, c.name, b.bill_month, b.units_consumed, 
                   b.total_amount, b.payment_status
            FROM bills b
            JOIN customers c ON b.customer_id = c.customer_id
            ORDER BY b.bill_date DESC
            """
            self.cursor.execute(query)
            bills = self.cursor.fetchall()
            
            if not bills:
                print("No bills found")
                return
            
            print("\n" + "="*90)
            print("ALL BILLS")
            print("="*90)
            print(f"{'Bill ID':<10} {'Customer':<25} {'Month':<15} {'Units':<10} {'Amount':<12} {'Status':<10}")
            print("-"*90)
            
            for bill in bills:
                print(f"{bill[0]:<10} {bill[1]:<25} {bill[2]:<15} {bill[3]:<10} Rs.{bill[4]:<11.2f} {bill[5]:<10}")
            
            print("="*90 + "\n")
            
        except Exception as e:
            print(f"Error: {e}")
    
    def update_payment_status(self, bill_id, status):
        try:
            query = """
            UPDATE bills 
            SET payment_status = %s, payment_date = %s
            WHERE bill_id = %s
            """
            payment_date = datetime.now().date() if status == 'Paid' else None
            
            self.cursor.execute(query, (status, payment_date, bill_id))
            self.connection.commit()
            
            print(f"Payment status updated to {status}")
            
        except Exception as e:
            print(f"Error: {e}")
    def delete_customer(self, customer_id):
        try:
            delete_readings = "DELETE FROM meter_readings WHERE customer_id = %s"
            self.cursor.execute(delete_readings, (customer_id,))           
            delete_bills = "DELETE FROM bills WHERE customer_id = %s"
            self.cursor.execute(delete_bills, (customer_id,))
            delete_cust = "DELETE FROM customers WHERE customer_id = %s"
            self.cursor.execute(delete_cust, (customer_id,))
            
            self.connection.commit()
            
            if self.cursor.rowcount > 0:
                print(f"Customer ID {customer_id} and all associated data deleted successfully.")
                return True
            else:
                print(f"No customer found with ID {customer_id}.")
                return False
                
        except Exception as e:
            self.connection.rollback()
            print(f"Error: {e}")
            return False
    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Database connection closed")


def main():
    system = ElectricityBillSystem()
    
    if not system.connect_database():
        print("Database connection failed")
        return
    
    system.create_tables()
    
    print("\n" + "="*70)
    print("ELECTRICITY BILL MANAGEMENT SYSTEM")
    print("="*70)
    
    while True:
        print("\nMAIN MENU")
        print("1. Add New Customer")
        print("2. Add Meter Reading")
        print("3. Generate Bill")
        print("4. Display Bill")
        print("5. View All Customers")
        print("6. View All Bills")
        print("7. Update Payment Status")
        print("8. Generate Bill for Random Customer")
        print("9. Delete Customer")
        print("10. Exit")
        
        choice = input("\nEnter choice (1-10): ").strip()
        
        if choice == '1':
            print("\nADD CUSTOMER")
            name = input("Customer name: ").strip()
            address = input("Address: ").strip()
            phone = input("Phone: ").strip()
            email = input("Email: ").strip()
            print("1.Residential  2.Commercial  3.Industrial")
            conn_choice = input("Connection type (1-3): ").strip()
            
            conn_types = {'1': 'Residential', '2': 'Commercial', '3': 'Industrial'}
            connection_type = conn_types.get(conn_choice, 'Residential')
            
            system.add_customer(name, address, phone, email, connection_type)
        
        elif choice == '2':
            print("\nADD METER READING")
            customer_id = input("Customer ID: ").strip()
            reading_month = input("Month (e.g. January 2026): ").strip()
            meter_reading = input("Meter reading: ").strip()
            
            try:
                system.add_meter_reading(int(customer_id), reading_month, int(meter_reading))
            except:
                print("Invalid input")
        
        elif choice == '3':
            print("\nGENERATE BILL")
            customer_id = input("Customer ID: ").strip()
            current_month = input("Current month (e.g. February 2026): ").strip()
            
            try:
                bill_id = system.generate_bill(int(customer_id), current_month)
                if bill_id:
                    system.display_bill(bill_id)
            except:
                print("Invalid input")
        
        elif choice == '4':
            print("\nDISPLAY BILL")
            bill_id = input("Bill ID: ").strip()
            
            try:
                system.display_bill(int(bill_id))
            except:
                print("Invalid bill ID")
        
        elif choice == '5':
            system.view_all_customers()
        
        elif choice == '6':
            system.view_all_bills()
        
        elif choice == '7':
            print("\nUPDATE PAYMENT")
            bill_id = input("Bill ID: ").strip()
            print("1.Paid  2.Pending  3.Overdue")
            status_choice = input("Status (1-3): ").strip()
            
            status_map = {'1': 'Paid', '2': 'Pending', '3': 'Overdue'}
            status = status_map.get(status_choice, 'Pending')
            
            try:
                system.update_payment_status(int(bill_id), status)
            except:
                print("Invalid input")
        
        elif choice == '8':
            print("\nRANDOM CUSTOMER BILL")
            random_customer = system.get_random_customer()
            
            if random_customer:
                customer_id, name = random_customer
                print(f"Customer: {name} (ID: {customer_id})")
                
                current_month = input("Current month (e.g. February 2026): ").strip()
                
                bill_id = system.generate_bill(customer_id, current_month)
                if bill_id:
                    system.display_bill(bill_id)
            else:
                print("No customers found")
        
        elif choice == '9':
            print("\nDELETE CUSTOMER")
            customer_id = input("Enter Customer ID to delete: ").strip()
            
            confirm = input(f"Are you sure you want to delete customer {customer_id}? (yes/no): ").lower()
            if confirm == 'yes':
                try:
                    system.delete_customer(int(customer_id))
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            else:
                print("Deletion cancelled.")

        elif choice == '10':
            print("\nExiting system...")
            break
        else:
            print("Invalid choice")
    
    system.close_connection()


if __name__ == "__main__":
    main()
