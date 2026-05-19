# 🎓 CampusAtDesk

> *Where campus talent meets opportunity — a smart, role-based career portal built for students, recruiters, and administrators.*

---

## What is this?

CampusAtDesk is a full-stack campus placement platform that connects students with recruiters through a clean, structured workflow. Students browse and apply for jobs. Recruiters post openings and review candidates. Admins keep everything running smoothly.

Three roles. One platform. Zero friction.

---

## Who's it for?

| Role | What they do |
|------|-------------|
| 🎒 **Student** | Register, browse jobs by category, apply with resume, track application status |
| 🏢 **Recruiter** | Post jobs, manage listings, review incoming applications |
| 🛡️ **Admin** | Oversee users, manage companies, categories, and recruiters, filter students by branch |

---

## Features

- 🔐 Secure authentication with hashed passwords and session management
- 🎭 Role-based access control — every page knows who belongs there
- 🌿 Branch-wise student filtering 
- 📄 Resume upload support for job applications
- 🏷️ Job categorization for easier discovery
- 🏗️ Company and recruiter management from admin panel
- ⚡ Built with Flask + SQLAlchemy on a live MySQL database

---

## 🛠️ Tech Stack


| Layer | Technology |
| :--- | :--- |
| **Backend** | Flask (Python) |
| **Database** | MySQL _(via SQLAlchemy + PyMySQL)_ |
| **Auth** | Werkzeug password hashing + Flask sessions |
| **Frontend** | Jinja2 templates + custom CSS |


---

## Getting Started

```bash
# Install dependencies
pip install flask flask-sqlalchemy pymysql werkzeug python-dotenv

# Run the app
python app.py
```

Visit `http://127.0.0.1:5001` — log in or register to get started.

---



> *Developed & Designed by **Madan Y***