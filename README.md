# Contact Lenses App 👁️‍🗨️

A full-stack Django web application for managing a contact lens business, including products, customers, orders, and user-generated reviews.
The app features authentication, role management, and is deployed on the cloud.

---

## 🌐 Live Demo
👉 https://contactlensesapp-e9gyhyh4d7cvf4dk.francecentral-01.azurewebsites.net

---

## 🛠️ Tech Stack

- 🐍 Python 3.11+
- 🌐 Django 6.0.2+
- 🗄️ PostgreSQL
- 🎨 Bootstrap 5
- ☁️ Microsoft Azure (App Service)
- 🔧 Git & GitHub

---

## 🚀 Features

### 🛒 Core Functionality

- CRUD operations for Products, Customers, and Orders
- Many-to-many relationship between Orders and Products
- Clean and reusable templates

### 👤Authentication & Authorization

- Custom User model
- Login / Logout functionality
- User Groups (role-based access)
- Protected views

### ⭐ Reviews System

- Users can leave reviews for products
- Rating system (1–5 stars)
- Average rating calculation per product

### 📊 Dashboard

- Overview of key metrics
- Quick navigation to main sections

### 🎨 UI/UX

- Responsive design using Bootstrap 5
- Reusable layout (navbar, footer, base template)
- Custom 404 and 500 error pages

---

## ☁️ Deployment

The application is deployed on Microsoft Azure App Service using:

- Gunicorn (WSGI server)
- Environment variables for configuration
- PostgreSQL database
- 
---

## ⚙️ Installation (Local Setup)


### 1️⃣ Clone the repository
```
git clone https://github.com/ivanpch12/ContactLensesApp
cd ContactLensesApp
```

### 2️⃣ Create and activate a virtual environment

```
# Linux / macOS
python -m venv venv
source venv/bin/activate
```
```
# Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables
Create a .env file based on .env.example: 
```
SECRET_KEY=<your-secret-key>
DEBUG=False
DB_NAME=contact_lenses_app
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=127.0.0.1
DB_PORT=5432
```

---

## 🗄️ Database Setup
Apply migrations
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## ▶️ Running the App
```
python manage.py runserver
```

Open <http://127.0.0.1:8000> in your browser.

---

## 📦 Static Files

Before deployment:

python manage.py collectstatic

---

## 📁 Project Structure

- 📂 core – Home page, base template, custom 404 page, navigation, and footer

- 📂 products – Product model, forms, views, templates

- 📂 customers – Customer model, forms, views, templates

- 📂 orders – Order model (many-to-many with products), forms, views, templates

---

## 🔐 Roles & Permissions

- Admin – full access via Django admin
- Authenticated Users – can add reviews and interact with the system
- Guests – read-only access

---

## 🧪 Testing

Basic manual testing via:
- Django Admin
- UI forms and validations

(Future: automated tests)

---

## 🚧 Future Improvements

#### ℹ️ This is an early-stage project with more planned improvements:

- 🔍 Product search and filtering

- 🛍️ Shopping cart functionality

- 📊 Advanced analytics dashboard

- 📦 Order tracking system

- 🌐 Multi-language support

- 🧪 Unit & integration tests

---

## 📌 Notes

- Environment variables are required for production
- Static files are handled via collectstatic
- Azure deployment uses Gunicorn
