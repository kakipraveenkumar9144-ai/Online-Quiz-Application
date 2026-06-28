# Online-Quiz-Application
Online Quiz Application developed using HTML, CSS, JavaScript, Django, and a database. It features user registration, login, quiz management, score calculation, and result tracking. The application provides a responsive, user-friendly interface and demonstrates full-stack web development with secure database integration.

---------------------------------------------------------------------------------------------------------------------------------

## 📌 Project Overview

The Online Quiz Application is a web-based project developed using **Python, Django, HTML, CSS, JavaScript, and SQLite**. It allows users to register, log in, attend quizzes, and view their scores after submitting the quiz. The admin can manage quiz questions through the Django Admin Panel.

---

## 🚀 Features

- User Registration
- User Login & Logout
- Attend Online Quiz
- Multiple Choice Questions
- Automatic Score Calculation
- Result Display
- Admin Panel to Add, Edit, and Delete Questions
- Simple and User-Friendly Interface

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Django

### Database
- SQLite (can be changed to MySQL)

---

## 📁 Project Structure

```
OnlineQuiz/
│
├── manage.py
├── db.sqlite3
├── onlinequiz/
├── quizapp/
│   ├── templates/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
```

---

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/online-quiz-application.git
```

2. Open the project folder

```bash
cd online-quiz-application
```

3. Create a virtual environment

```bash
python -m venv env
```

4. Activate the virtual environment

**Windows**

```bash
env\Scripts\activate
```

5. Install dependencies

```bash
pip install django
```

6. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

7. Create admin account

```bash
python manage.py createsuperuser
```

8. Run the server

```bash
python manage.py runserver
```

9. Open your browser

```
http://127.0.0.1:8000/
```

---

## 👤 User Module

- Register
- Login
- Attempt Quiz
- Submit Quiz
- View Score
- Logout

---

## 👨‍💼 Admin Module

- Admin Login
- Add Questions
- Update Questions
- Delete Questions
- View Quiz Results

---

## 📸 Output

- Home Page
- Registration Page
- Login Page
- Quiz Page
- Result Page
- Admin Dashboard

---

## 🎯 Future Improvements

- Quiz Timer
- Leaderboard
- Question Categories
- Password Reset
- Email Notifications
- Certificate Generation

---

## 👨‍💻 Developed By

**K. Praveen Kumar**

Python Full Stack Developer
