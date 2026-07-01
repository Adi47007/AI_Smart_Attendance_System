# AI_Smart_Attendance_System

# 🎓 AI Smart Attendance System

An AI-powered Smart Attendance System built with **Django**, **DeepFace**, **TensorFlow**, and **MySQL** that automatically marks attendance using facial recognition.

---

<img width="953" height="415" alt="image" src="https://github.com/user-attachments/assets/c720fb7b-90e1-402e-89ec-ffd2338d527c" />




## 🚀 Features

- 👤 Student Registration with Photo Upload
- 🤖 AI Face Recognition using DeepFace
- ✅ Automatic Attendance Marking
- 📅 Daily Attendance Records
- 📥 Attendance CSV Export
- 🔐 Django Admin Panel
- 🗄️ MySQL Database
- 📱 Responsive User Interface

---

## 🛠️ Tech Stack

### Backend
- Django
- Python
- MySQL

### AI & Computer Vision
- DeepFace
- TensorFlow
- RetinaFace
- OpenCV

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript

---

## 📂 Project Structure

```
attendance_system/
│
├── attendance/
├── attendance_system/
├── templates/
├── static/
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/attendance_system.git
```

Go into the project

```bash
cd attendance_system
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure your MySQL database in:

```
attendance_system/settings.py
```

Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Create an admin account

```bash
python manage.py createsuperuser
```

Run the server

```bash
python manage.py runserver
```

---

## 📸 How It Works

1. Register students with their photographs.
2. Upload a live face image.
3. DeepFace compares the uploaded image with stored student photos.
4. If a match is found, attendance is automatically recorded.
5. Attendance records can be viewed in the admin panel or exported as CSV.

---

## Future Improvements

- Live webcam attendance
- Face anti-spoofing
- Multi-face detection
- Email notifications
- Attendance analytics dashboard
- Mobile application integration

---

## Author

**Aditya Saini**

GitHub: https://github.com/adi47007

---

## License

This project is licensed under the MIT License.
