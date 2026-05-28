CREATE DATABASE IF NOT EXISTS electricity_bill_db;
USE electricity_bill_db;

DROP TABLE IF EXISTS bills;
DROP TABLE IF EXISTS meter_readings;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100),
    connection_type VARCHAR(50) DEFAULT 'Residential',
    registration_date DATE NOT NULL
);

CREATE TABLE meter_readings (
    reading_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    reading_month VARCHAR(20) NOT NULL,
    reading_date DATE NOT NULL,
    meter_reading INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE bills (
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
);

INSERT INTO customers (name, address, phone, email, connection_type, registration_date) VALUES
('Rajesh Kumar', '123 MG Road, Chennai', '9876543210', 'rajesh@email.com', 'Residential', '2025-01-15'),
('Priya Sharma', '456 Anna Salai, Chennai', '9876543211', 'priya@email.com', 'Commercial', '2025-01-20'),
('Amit Patel', '789 Park Street, Coimbatore', '9876543212', 'amit@email.com', 'Residential', '2025-02-01'),
('Sunita Reddy', '321 Nehru Nagar, Chennai', '9876543213', 'sunita@email.com', 'Industrial', '2025-01-10'),
('Vikram Singh', '654 Lake View Road, Coimbatore', '9876543214', 'vikram@email.com', 'Residential', '2025-01-25');

INSERT INTO meter_readings (customer_id, reading_month, reading_date, meter_reading) VALUES
(1, 'January 2026', '2026-01-31', 1500),
(2, 'January 2026', '2026-01-31', 3200),
(3, 'January 2026', '2026-01-31', 1800),
(4, 'January 2026', '2026-01-31', 5600),
(5, 'January 2026', '2026-01-31', 1350);

INSERT INTO meter_readings (customer_id, reading_month, reading_date, meter_reading) VALUES
(1, 'December 2025', '2025-12-31', 1200),
(2, 'December 2025', '2025-12-31', 2800),
(3, 'December 2025', '2025-12-31', 1500),
(4, 'December 2025', '2025-12-31', 4900),
(5, 'December 2025', '2025-12-31', 1100);
COMMIT;