# E-Commerce Website using Django

This E-commerce platform offers users the ability to browse a variety of products, add them to their cart, proceed to checkout, and securely complete the purchase using PayPal integration.

## Table of Contents

1. [About](#about)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Demo Images](#demo-images)
    - [Register User](#register-user)
    - [Login User](#login-user)
    - [Empty Cart](#empty-cart)
    - [Index/Shop Page](#indexshop-page)
    - [Product Page](#product-page)
    - [Cart Page](#cart-page)
    - [Paypal Payment](#paypal-payment)
    - [Payment Success](#payment-success)
    - [Admin Panel- Order Details](#admin-panel-order-details)
    - [Admin Panel- Cart Detail](#admin-panel-cart-detail)
    - [Admin Panel- User List](#admin-panel-user-list)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Technologies Used](#technologies-used)

## About <a name="about"></a>

This repository contains a robust and user-friendly E-commerce website developed using Django, a high-level Python web framework. The platform provides an intuitive interface for users to explore a wide range of products, add them to their cart, and seamlessly complete purchases using PayPal integration. Featuring authentication functionalities, the project enables users to register, sign in, and manage their shopping experiences effortlessly. The project structure is well-organized, adhering to Django's best practices, and is a great starting point for building your own online store.

## Features <a name="features"></a>

- User authentication and registration
- Product catalog display
- Product details view
- Shopping cart functionality
- Checkout process using PayPal
- Order management

## Project Structure <a name="project-structure"></a>

The project directory structure is organized as follows:

```plaintext
e-commerce-django/
├── core/                    # Django app with core functionalities such as handling product display, cart operations, etc.
├── authentication/          # Django app for user authentication
├── ecommerce/               # Django project folder
├── static/                  # Static files (CSS, JS, images)
├── media/                   # Media files (uploaded product images)
├── templates/               # Base templates for the project
├── manage.py                # Django's command-line utility
├── env_variables.py         # Django's secret SETTINGS.PY variable file
└── requirements.txt         # Required Python packages
```

## Demo Images <a name="demo-images"></a>

### Register User <a name="register-user"></a>
![9](https://github.com/mustafa854/ecommerce-django/assets/84233282/fabe4e17-5583-48a0-8922-b6de02b24f94)

### Login User <a name="login-user"></a>
![8](https://github.com/mustafa854/ecommerce-django/assets/84233282/a739b834-3046-4bff-a67a-42e15cad47d7)

### Empty Cart <a name="empty-cart"></a>
![7](https://github.com/mustafa854/ecommerce-django/assets/84233282/a75730ab-a0d6-4464-b571-014ed061bd0c)

### Index/Shop Page <a name="indexshop-page"></a>
![1](https://github.com/mustafa854/ecommerce-django/assets/84233282/63d96de8-60bb-490f-bf31-d1a55bbdb659)
![2](https://github.com/mustafa854/ecommerce-django/assets/84233282/fc952d2a-9756-4078-a530-5df74e820590)

### Product Page <a name="product-page"></a>
![3](https://github.com/mustafa854/ecommerce-django/assets/84233282/177c708d-c9e7-41c0-a7cc-b6c9e910c726)

### Cart Page <a name="cart-page"></a>
![4](https://github.com/mustafa854/ecommerce-django/assets/84233282/dd075498-0183-4d36-b7c2-498fb71630c9)

### Paypal Payment <a name="paypal-payment"></a>
![5](https://github.com/mustafa854/ecommerce-django/assets/84233282/a54e2c67-33ed-406a-b3e8-16c09da10840)

### Payment Success <a name="payment-success"></a>
![6](https://github.com/mustafa854/ecommerce-django/assets/84233282/5958f003-687c-44bb-b8f4-21eb443a73ef)

### Admin Panel- Order Details <a name="admin-panel-order-details"></a>
![10](https://github.com/mustafa854/ecommerce-django/assets/84233282/36c89914-f779-4c9c-bd91-7c8114348612)

### Admin Panel- Cart Detail <a name="admin-panel-cart-detail"></a>
![11](https://github.com/mustafa854/ecommerce-django/assets/84233282/5791e620-87dd-4cb7-9711-549a53dd0e3a)

### Admin Panel- User List <a name="admin-panel-user-list"></a>
![12](https://github.com/mustafa854/ecommerce-django/assets/84233282/04f6b0b7-554e-4100-b2ab-557259bac16e)

## Installation <a name="installation"></a>

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

## Usage <a name="usage"></a>

- Visit the homepage to view available products and click on a product to see details.
- Add products to the cart and proceed to checkout.
- Use PayPal sandbox credentials for test payments.

## Technologies Used <a name="technologies-used"></a>

- Django
- Bootstrap 5
- PayPal REST SDK
