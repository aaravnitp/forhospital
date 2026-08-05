
# Hospital Website

A Django-based hospital website that lets visitors browse events, find doctors, explore careers, and make payments.

Built by **Aarav Raj**.

---

## Features

- **Events** — browse hospital events (homepage with a slider, upcoming events, and workshops)
- **Doctors** — view doctor profiles (hardcoded list)
- **Careers** — browse job openings, benefits, and employee testimonials, plus an application form
- **Payments** — consultancy fee payment form
- **Admin panel** — full Django admin for content management

> **Note:** All page content is currently hardcoded in the HTML templates. No models are defined yet, so the admin panel is empty and the Careers/Payments forms only show a confirmation alert on submit — they don't persist data.

---

## Tech Stack

- Python 3.x
- Django 5.2.16
- SQLite (default database)

---

## Project Structure

```
forhospital/
├── hospital_website/          # Django project root (open this folder in your editor)
│   ├── manage.py
│   ├── hospital_website/      # Project settings & URL config
│   ├── events/                # Events app
│   ├── doctors/               # Doctors app
│   ├── careers/               # Careers app
│   ├── payments/              # Payments app
│   ├── db.sqlite3
│   └── venv/                  # Python virtual environment (gitignored)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone <repo-url>
cd hospital\ project/forhospital/hospital_website
```

### 2. Create and activate a virtual environment

```bash
# Windows (Git Bash)
python -m venv venv
source venv/Scripts/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r ../requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. (Optional) Create an admin user

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Then open **http://127.0.0.1:8000** in your browser. The admin panel is at **http://127.0.0.1:8000/admin/**.

---

## Opening in VS Code

Open the **`forhospital/hospital_website/`** folder as your VS Code workspace (not the outer `forhospital/` or `hospital project/` folder). This ensures the language server picks up the project root and the virtual environment — otherwise `django` imports will appear underlined in the editor.

To confirm the correct interpreter is selected, click the Python version in the bottom-left status bar and pick the one at `venv/Scripts/python.exe` inside `hospital_website/`.

---

## License

This project is private and unlicensed.
