## Stitch Shop Backend ##

A Django REST API backend for the Stitch Shop e-commerce platform specializing in clothing and fashion items.

## Tech Stack ##

Framework: Django 4.2+ with Django REST Framework
Database: MongoDB with Djongo
Payment Processing: Stripe & PayPal
Authentication: Token-based Authentication
File Storage: Local storage (configurable for cloud)
Environment: Python 3.11+

## Project Structure ##
stitch_shop_backend/
├── stitch_shop/           # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/              # Product management app
├── orders/                # Order management app  
├── payments/              # Payment processing app
├── users/                 # User management app
├── cart/                  # Shopping cart app
├── media/                 # Uploaded images
├── static/                # Static files
├── requirements.txt       # Python dependencies
├── manage.py             # Django management script
└── README.md             # This file

##  Quick Start ##

## Prerequisites ##

-Python 3.11 or higher
-MongoDB Community Server
-Git
-Code editor (VS Code recommended)

## Installation ##

## Clone the repository ##
bashgit clone https://github.com/YOUR_USERNAME/stitch-shop-backend.git
cd stitch-shop-backend

## Create virtual environment ##
bash# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

## Install dependencies ##
bashpip install -r requirements.txt

## Environment Setup ##
Create a .env file in the root directory:
envSECRET_KEY=your-django-secret-key-here
DEBUG=True
STRIPE_PUBLISHABLE_KEY=pk_test_your_stripe_publishable_key
STRIPE_SECRET_KEY=sk_test_your_stripe_secret_key
PAYPAL_CLIENT_ID=your_paypal_client_id
PAYPAL_CLIENT_SECRET=your_paypal_client_secret

## Database Setup ##
bash# Start MongoDB service (Windows)
net start MongoDB

# Run Django migrations
python manage.py makemigrations
python manage.py migrate

## Create Superuser ##
bashpython manage.py createsuperuser

## Start Development Server ##
bashpython manage.py runserver

## Authentication ##
The API uses Token-based authentication. Include the token in request headers:
bashAuthorization: Token your_token_here
Get Authentication Token
bashPOST /api/users/login/
{
    "username": "your_username",
    "password": "your_password"
}

## Database Models ##
Core Models Overview

Product: Name, description, price, category, image, stock
Category: Name, description, active status
Order: User, items, total, status, shipping address
OrderItem: Product, quantity, price
Cart: User session cart management
CartItem: Product, quantity, temporary storage

## Testing ##
Run Tests
bash# Run all tests
python manage.py test

# Run specific app tests
python manage.py test products
python manage.py test orders
API Testing

Admin Panel: http://localhost:8000/admin/
API Browser: http://localhost:8000/api/
Postman Collection: [Coming Soon]
 
  ## Development ##
Adding New Dependencies
bashpip install package_name
pip freeze > requirements.txt
Database Migrations
bash# After model changes
python manage.py makemigrations
python manage.py migrate
Collect Static Files
bashpython manage.py collectstatic

  ## Code Style ##

-Follow PEP 8 Python style guide
-Use meaningful variable and function names
-Add docstrings to functions and classes
-Comment complex logic

  ## Deployment ##
  
## Environment Variables for Production ##

SECRET_KEY=production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=mongodb://production-db-url
STRIPE_SECRET_KEY=sk_live_your_live_key

## Production Checklist ##

 Set DEBUG=False
 Configure ALLOWED_HOSTS
 Set up production database
 Configure static file serving
 Set up SSL certificate
 Configure payment webhooks

