# IT Inventory Management System

A simple command-line interface (CLI) application to manage an IT equipment inventory. The project provides basic features to register equipment and employees, list and update equipment status, and store data in a PostgreSQL database.

This repository is intended as a small, modular starter project for learning how to use Python with PostgreSQL in a clean, testable way.

Features
- Register new equipment (model, serial number, status, optional responsible person)
- View full inventory
- Update equipment status by serial number
- Register and list responsible employees
- Small, easy-to-read codebase with separate modules for database connection and actions

Requirements
- Python 3.8+
- PostgreSQL
- Python dependencies (see requirements.txt)

Quick start
1. Clone the repository

   git clone https://github.com/Domdevx3/IT-Inventory-Management-System.git
   cd IT-Inventory-Management-System

2. Create a virtual environment and install dependencies

   python -m venv .venv
   source .venv/bin/activate    # Linux / macOS
   .venv\Scripts\activate     # Windows (PowerShell)
   pip install -r requirements.txt

3. Configure the database

The project uses PostgreSQL. By default the database connection settings are in `database.py`:

- host: localhost
- port: 5432
- user: postgres
- password: (empty)
- database: it_inventory

Create the database and the tables used by the app. Example SQL:

```sql
-- Create database (run as a PostgreSQL superuser)
CREATE DATABASE it_inventory;

-- Connect to the database and create tables
CREATE TABLE empleados (
  id_emp VARCHAR(64) PRIMARY KEY,
  emp_name VARCHAR(255) NOT NULL,
  departamento VARCHAR(255) NOT NULL,
  email VARCHAR(255)
);

CREATE TABLE equipos (
  id_equipos SERIAL PRIMARY KEY,
  modelo VARCHAR(255) NOT NULL,
  num_serie VARCHAR(255) UNIQUE NOT NULL,
  estado VARCHAR(64) NOT NULL DEFAULT 'disponible',
  id_responsable VARCHAR(64),
  CONSTRAINT fk_responsable
    FOREIGN KEY(id_responsable)
      REFERENCES empleados(id_emp)
      ON DELETE SET NULL
);
```

Notes:
- If you prefer not to edit `database.py`, you can create the database and user that match the defaults, or adapt the file to load settings from environment variables.

Run the application

    python main.py

Select options from the menu to register equipment and employees, list the inventory, or update equipment status.

Usage examples
- Register a new employee (option 4)
- Register equipment (option 1). When prompted for responsible ID, provide the `id_emp` of an existing employee or press Enter to leave it empty.
- List equipment (option 2)
- Update equipment state by serial number (option 3)

Project structure
- main.py — CLI menu and user interaction
- actions.py — business logic and database queries
- database.py — simple DatabaseConnection wrapper around psycopg2
- requirements.txt — Python dependencies

Testing and improvements (suggestions)
- Replace hard-coded database credentials with environment variables (e.g., using python-dotenv or os.environ)
- Add logging instead of printing directly to stdout
- Add unit tests for actions (use a test database or a mocking library)
- Improve input validation and internationalization (some interactive prompts mix English and Spanish)

