# Contact Lenses App 👁️‍🗨️

A Django web application to manage **products, customers, and orders** for a contact lens business.  
The app provides full CRUD functionality, a **dashboard**, and a responsive interface using **Bootstrap 5**.

---

## 🛠️ Tech Stack

- 🐍 Python 3.11+
- 🌐 Django 6.0.2+
- 🗄️ PostgreSQL
- 🎨 Bootstrap 5
- 🔧 Git & GitHub

---

## 🚀 Installation

### 1️⃣ Clone the repository
```
git clone <https://github.com/ivanpch12/ContactLensesApp>
cd contact-lenses-app
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
```

---

## ▶️ Running the App
```
python manage.py runserver
```

Open <http://127.0.0.1:8000> in your browser.

---

## ✨ Features

- 🛒 CRUD operations for Products, Customers, and Orders

- 📊 Dashboard with total counts and quick links to each section

- 📱 Responsive design using Bootstrap 5

- ❌ Custom 404 error page

- 🔁 Reusable templates with navigation, header, and footer partials

- 📝 Forms with validations, help texts, placeholders, and read-only delete confirmation

---

## 📁 Project Structure

- 📂 core – Home page, base template, custom 404 page, navigation, and footer

- 📂 products – Product model, forms, views, templates

- 📂 customers – Customer model, forms, views, templates

- 📂 orders – Order model (many-to-many with products), forms, views, templates


---

## 📝 Notes

- ❗ Authentication is not implemented; login/logout functionality is excluded

- ❗ All pages are accessible via navigation links

---

## 🚧 Future Features / Roadmap

#### ℹ️ This is an early-stage project with more planned improvements:

 - 🔑 Authentication and user management using Django's built-in User model

- 👓 Support for lens specifications such as diopters, colors, and types

- 📦 Advanced product filtering and search

- 🧾 Order history, invoices, and reports

- 🛠️ Admin enhancements with dashboards and analytics

- 🌐 Optional multi-language support
