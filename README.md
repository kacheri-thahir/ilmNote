# 📚 IlmNote

◆ IlmNote is a production-oriented Django web application that implements a role-based content management system with strict access control.
The platform cleanly separates public content delivery from internal business operations, while reserving system-level administration exclusively for superusers.

◆ It enforces permission boundaries at the view, form, and template layers, dynamically restricts sensitive fields, and prevents privilege escalation through backend validation.
The architecture and security model reflect real-world enterprise Django practices.

<img width="1920" height="1080" alt="Screenshot 2025-12-14 120835" src="https://github.com/user-attachments/assets/1d67ac1a-97a3-430a-a2c8-a07bae979661" />

<img width="1920" height="1080" alt="Screenshot 2025-12-14 120900" src="https://github.com/user-attachments/assets/3aee36a3-4732-4ac2-ac6a-5b0a1cae8e88" />

<img width="1920" height="1080" alt="Screenshot 2025-12-14 120915" src="https://github.com/user-attachments/assets/3a23aef3-18d8-4e1b-a204-89018b26276a" />

# ✨ Key Features

📰 Public blog and knowledge publishing platform

🧭 Custom internal dashboard for editors and managers

🔐 Role-based access control (RBAC)

🛡️ Backend-enforced permission validation

🧩 Dynamic form field restriction based on user role

👤 Secure user creation, editing, and deletion

🚫 Superuser protection from non-privileged roles

⚙️ Production-ready static and media handling

👥 User Roles & Access Model
🔹 Public Users

View and read published content

No authentication required

🔹 Editors / Managers

Access custom dashboard

Create and manage content

Manage normal users

❌ Cannot:

View or edit superuser accounts

Assign permissions or groups

Grant superuser privileges

🔹 Superusers

Full system-level access

Exclusive access to secured Django admin panel

Handle configuration, emergency fixes, and system maintenance

# 🛠️ Tech Stack

Backend: Django (Python)

Database: SQLite (development)
Easily extensible to PostgreSQL / MySQL

Frontend: Django Templates, HTML, CSS

Authentication: Django Auth with custom permission logic

Deployment: PythonAnywhere (production-compatible setup)

Version Control: Git & GitHub

# 📁 Project Structure

ilmNote/

│

├── blogs/                 # Public blog functionality

├── dashboard/             # Role-based internal dashboard

├── ilmnote/               # Core project settings and URLs

├── templates/             # HTML templates

├── static/                # CSS and static assets

├── media/                 # Uploaded images and files

├── manage.py

└── requirements.txt

# 🔐 Security Design Highlights

✅ Permissions enforced at:

View level

Form level

Template level

🚫 Managers cannot:

Modify is_superuser

Assign groups or permissions

Edit or delete superuser accounts

🔒 Django admin access restricted to superusers only

🧠 Backend validation prevents privilege escalation

🔗 Admin URL obfuscated for additional protection

# 🌐 Deployment Notes

Environment-aware configuration

Static files handled via collectstatic

Media served securely

Admin access hardened and restricted

Suitable for real-world small to medium production deployments

# 👨‍💻 Author

# Thahir Kacheri
# 🎓 MCA Graduate | 🐍 Python & Django Developer
