# E-Commerce Website using Django

This E-commerce platform offers users the ability to browse a variety of products, add them to their cart, proceed to checkout, and securely complete the purchase using PayPal integration.

## About

This repository contains a robust and user-friendly E-commerce website developed using Django, a high-level Python web framework. The platform provides an intuitive interface for users to explore a wide range of products, add them to their cart, and seamlessly complete purchases using PayPal integration. Featuring authentication functionalities, the project enables users to register, sign in, and manage their shopping experiences effortlessly. The project structure is well-organized, adhering to Django's best practices, and is a great starting point for building your own online store.

## Features

- User authentication and registration
- Product catalog display
- Product details view
- Shopping cart functionality
- Checkout process using PayPal
- Order management

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/mustafa854/ecommerce-django.git
    ```

2. **Create and activate a virtual environment:**

    ```bash
    # Create a virtual environment
    python -m venv myenv
    
    # Activate the virtual environment
    source myenv/bin/activate  # For Linux or macOS
    .\myenv\Scripts\activate   # For Windows
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create `env_variables.py` file in the project root:**

    - In the project root directory, create a file named `env_variables.py`.
    - Add the following variables in the file:
        - `SECRET_KEY` (Django project Secret Key)
        - `PAYPAL_CLIENT_ID`
        - `PAYPAL_SECRET`
          
4. **Configure Django settings:**

    - Open `settings.py` and set up your database configurations.


5. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Start the Django server:**

    ```bash
    python manage.py runserver
    ```


## Usage

- Visit the homepage to view available products and click on a product to see details.
- Add products to the cart and proceed to checkout.
- Use PayPal sandbox credentials for test payments.

## Technologies Used

- Django
- Bootstrap 5
- PayPal REST SDK
