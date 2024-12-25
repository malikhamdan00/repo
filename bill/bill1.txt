# Inventory Management System

## Description
This Inventory Management System is a Python-based desktop application designed to simplify and streamline inventory management tasks. Built using Tkinter for the graphical user interface and SQLite for database management, it provides features to manage employees, suppliers, and other inventory-related data efficiently.

## Features

- **Employee Management**: Add, update, delete, and search employee details.
- **Supplier Management**: Comprehensive management of supplier details, including adding, updating, deleting, and searching records.
- **User-Friendly Interface**: Clean and intuitive design for easy navigation and use.
- **Database Integration**: Uses SQLite for persistent data storage.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/malikhamdan00/repo.git
   cd repo
   ```

2. **Set Up the Virtual Environment** (Optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

   If a `requirements.txt` file is not available, manually install the necessary libraries:

   ```bash
   pip install tkinter pillow
   ```

4. **Set Up the Database**:

   Run the `create_db.py` script to initialize the SQLite database:

   ```bash
   python create_db.py
   ```

## Usage

1. **Run the Application**:

   ```bash
   python dashboard.py
   ```

2. **Features Navigation**:

   - Access the employee and supplier management modules via the dashboard.
   - Perform CRUD (Create, Read, Update, Delete) operations on records.

## Project Structure

- `dashboard.py`: The main application entry point.
- `employee.py`: Module handling employee management.
- `supplier.py`: Module for supplier management functionalities.
- `create_db.py`: Script to initialize the SQLite database schema.
- `ims.db`: SQLite database file.
- `images/`: Directory containing image assets for the application.

## Dependencies

- Python 3.x
- Tkinter (Standard Library)
- Pillow (Image Processing Library)
- SQLite3 (Built-in Database)

## Contributing

Contributions are welcome! Please fork the repository, make changes, and submit a pull request for review.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Contact

For inquiries or support, please contact:

**Hamdan Malik**
- Email: [fakehacker458@gmail.com](mailto:fakehacker458@gmail.com)

