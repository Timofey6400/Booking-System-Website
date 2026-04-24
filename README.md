# 📅 Booking System Web Site

![Django](https://img.shields.io/badge/framework-django-green.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

### 📝 Description
**Booking System** is a robust web application built with **Django**, designed to manage resource or service reservations. The project features availability logic, user dashboards, and a clean interface for managing appointments or rentals.

### ✨ Key Features
* 🔐 **Authentication System:** Secure user registration, login, and profile management using Django’s auth framework.
* 📅 **Booking Management:** Users can easily create, view, and cancel their reservations.
* 📊 **Availability Logic:** Smart system to prevent double-booking (handles "Available" vs. "Busy" states).
* 👤 **User Dashboard:** A personalized area for users to track their booking history and current status.
* ⚡ **Dynamic UI:** Integrated JavaScript for a smoother and more interactive user experience.

---

### 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Timofey6400/Booking-System-Website.git](https://github.com/Timofey6400/Booking-System-Website.git)
   cd Booking-System-Website
Install dependencies:
It is recommended to use a virtual environment.

Bash
pip install -r requirements.txt
Apply migrations:
Prepare the local database.

Bash
python manage.py migrate
Run the server:

Bash
python manage.py runserver
Open http://127.0.0.1:8000/ in your web browser.

📂 Project Structure
bookings/ — Logic for managing reservations and resource states.

main/ — General app handling the landing page and core site logic.

myproject/ — Django configuration files (settings, URLs).

js/ — Client-side scripts for dynamic front-end behavior.

🛠 Tech Stack
Backend: Python 3.x, Django

Frontend: HTML5, CSS3, JavaScript

Database: SQLite3 (default)
