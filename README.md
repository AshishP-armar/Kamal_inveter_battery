# Battery Sales Management System

This is a Flask-based web application for managing battery sales records. The app allows users to add, search, and store battery sales data in a MySQL database. This project is designed to be easily deployable on AWS or any other platform of your choice.


## Features

-   Add battery sales data with customer details.
-   Search battery records by serial number.
-   MySQL integration for storing sales data.

## Technologies Used

-   **Backend**: Flask
-   **Database**: MySQL
-   **Frontend**: HTML, CSS

## Database Schema

| Column Name     | Data Type      | Description                          |
|------------------|---------------|--------------------------------------|
| `id`            | INT           | Auto-increment primary key           |
| `customer_name` | VARCHAR(255)  | Customer's name                      |
| `mobile_number` | VARCHAR(15)   | Customer's mobile number             |
| `sale_date`     | DATE          | Date of sale                         |
| `battery_id`    | VARCHAR(255)  | Unique serial number of the battery  |
| `battery_name`  | VARCHAR(255)  | Battery name                         |
| `ampires`       | INT           | Battery capacity in amperes          |
| `price`         | DECIMAL(10,2) | Battery price                        |
| `warranty`      | VARCHAR(50)   | Warranty period                      |

## Virtual Environment For Your Flask project
### 1. **Install `virtualenv` (if not installed)**
```bash
pip install virtualenv
```
First, you need to make sure you have `virtualenv` installed. If you don't have it yet, you can install it using `pip`.
### 2. **Create a Virtual Environment**
```bash
python3 -m  venv .venv
```
### 3. **Activate the Virtual Environment**
macOS/Linux:
```bash
. .venv/bin/activate
```
### 3. **Deactivate the Virtual Environment**
```bash
deactivate
```
## Getting Started

Follow these steps to deploy and set up the project:

### 1. Clone the Repository
```bash
https://github.com/AshishP-armar/Kamal_inveter_battery.git
cd Kamal_inveter_battery
   ```


### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up the Database
1. Create a MySQL database: 
```bash
CREATE DATABASE battery_sales_db;
```
2. Create the `battery_sales` table:
```bash
CREATE DATABASE battery_sales_db;
CREATE TABLE battery_sales ( id INT AUTO_INCREMENT PRIMARY KEY, customer_name VARCHAR(255) NOT NULL, mobile_number VARCHAR(15) NOT NULL, sale_date DATE NOT NULL, battery_id VARCHAR(255) NOT NULL UNIQUE, battery_name VARCHAR(255) NOT NULL, ampires INT NOT NULL, price DECIMAL(10, 2) NOT NULL, warranty VARCHAR(50) NOT NULL );
```
3. Configure Environment Variables:-
Create a `.env` file in the project directory with your database credentials:
```bash
DB_HOST=your-mysql-host
DB_USER=your-mysql-username
DB_PASSWORD=your-mysql-password
DB_NAME=battery_sales_db
DB_PORT=3306
```
4. Run the Application :-
Start the Flask app locally:
```bash
python app.py
```
Access the app at `http://127.0.0.1:5000`.

### **Usage**

1.  **Add Sales Records**:
    -   Navigate to `/add` to add a new battery sales record.
2.  **Search Records**:
    -   Navigate to `/search` to search for a battery by its serial number.

### **Project Structure**
```bash
├── app.py           
├── templates/        # HTML templates
│   ├── main.html     # Landing page
│   ├── index.html    # Add sales form
│   └── search.html   # Search form and results
├── static/           # Static files (CSS, JS)
├── requirements.txt  # Python dependencies
├── Procfile          # For deployment
└── README.md         # Project instructions` 
```
----------
