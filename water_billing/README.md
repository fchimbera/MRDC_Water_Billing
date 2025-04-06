# superuser login credentials
Username: waterbilling
Email: waterbilling@mrdc.co.zw
Password: mrdc2025

# Water Billing System

## Description

This project is a Django-based web application for managing water billing. It allows administrators to manage users and water rates, meter readers to input meter readings, and residents to view their bills. It also provides a RESTful API for core functionalities.

## Features

* User registration and authentication with roles (resident, meter_reader, admin)
* Custom Django admin interface for managing users, water rates, meter readings, and bills
* Meter reading submission
* Automatic bill calculation based on consumption and water rates
* API endpoints for users, authentication, meter readings, and bills
* Web interface for basic user interactions (implementation may vary based on current views)

## Technologies Used

* Python
* Django
* Django REST Framework (DRF)
* MySQL

## Prerequisites

* Python 3.x
* Pip (Python package installer)
* MySQL Server installed and running
* Virtualenv (Recommended)

## Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/fchimbera/MRDC_Water_Billing.git
    cd water_billing 
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    * *(Note: A `requirements.txt` file was not found. You should create one by running `pip freeze > requirements.txt` after installing necessary packages.)*
    * Install necessary packages manually (or via `requirements.txt` once created):
        ```bash
        pip install Django djangorestframework mysqlclient 
        # Add any other dependencies your project uses
        ```
       *(The `mysqlclient` package is needed for Django to connect to MySQL)*

4.  **Configure Environment Variables:**
    * **IMPORTANT:** Do not commit sensitive information like `SECRET_KEY` or database credentials directly into your code. Use environment variables.
    * Create a `.env` file in the project root (where `manage.py` is).
    * Add the following variables to your `.env` file, replacing placeholder values:
        ```dotenv
        SECRET_KEY='your_strong_random_secret_key_here'
        DEBUG=True # Set to False for production!

        DB_NAME='water_billing'
        DB_USER='your_db_user'
        DB_PASSWORD='your_db_password'
        DB_HOST='localhost' # Or your DB host
        DB_PORT='3306' # Or your DB port
        ```
    * You will need to modify `settings.py` to load these variables (e.g., using `python-dotenv` package and `os.getenv`). 
        *Example modification in `settings.py`:*
        ```python
        import os
        from dotenv import load_dotenv

        load_dotenv() # Loads variables from .env file

        SECRET_KEY = os.getenv('SECRET_KEY')
        DEBUG = os.getenv('DEBUG', 'False') == 'True' # Default to False if not set

        # ... inside DATABASES setting ...
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        # ...
        ```
        *(Remember to `pip install python-dotenv`)*

5.  **Database Setup:**
    * Ensure your MySQL server is running.
    * Connect to MySQL and create the database specified in your `.env` file (e.g., `water_billing`):
        ```sql
        CREATE DATABASE water_billing; 
        ```

6.  **Run Database Migrations:**
    ```bash
    python manage.py migrate
    ```

7.  **Create Superuser:**
    * This user will have access to the Django admin interface.
    ```bash
    python manage.py createsuperuser
    ```
    * Follow the prompts to create a username, email, and password. **Do not use the insecure credentials previously stored in this README.**

## Running the Application

1.  **Activate Virtual Environment:** (If not already active)
    ```bash
    # On Windows: venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate
    ```
2.  **Start the Development Server:**
    ```bash
    python manage.py runserver
    ```
3.  The application will be running at `http://127.0.0.1:8000/`.

## API Endpoints Overview

(Assuming base URL `http://127.0.0.1:8000/api/`)

* `POST /register/`: User registration
* `POST /login/`: User login, returns auth token
* `GET, PUT /profile/`: View/Update user profile (Authentication Required)
* `POST /meter_readings/`: Add a new meter reading (Authentication Required, likely MeterReader role)
* `GET /bills/`: List bills for the logged-in user (Authentication Required)
* `GET /bill_details/<int:pk>/`: Get details for a specific bill (Authentication Required)

*(Refer to Postman or API documentation for request/response details)*

## Admin Interface

* Access the Django admin panel at `http://127.0.0.1:8000/admin/`.
* Log in using the superuser credentials created during setup.
* Here you can manage Users, Water Rates, Meter Readings, and Bills.

## Important Notes

* **Security:** Ensure `DEBUG` is set to `False` and you use a strong, environment-managed `SECRET_KEY` in production environments. Never expose database credentials or secret keys in your code repository.
* **Dependencies:** Keep your `requirements.txt` file updated.
* **Testing:** This project currently lacks automated tests. It is highly recommended to add unit and integration tests.