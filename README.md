# PrepMate — AI Placement Preparation Platform

A full-stack web platform that helps college students prepare for campus placements — aptitude and technical MCQ tests, a unique **confidence-rating** feature, and live performance dashboards for both students and admins.

Built as a BCA final-year project using **Flask, MySQL, HTML, CSS, and JavaScript.**

## ✨ Key Features

- 🔐 **Student & Admin Authentication** — separate login flows, hashed passwords
- 📋 **Aptitude & Technical MCQ Tests** — categorized question bank
- ⭐ **Confidence Rating (flagship feature)** — students rate their confidence after each answer, revealing overconfidence vs. genuine knowledge gaps — a feature not found in existing placement-prep platforms
- 📊 **Student Dashboard** — real-time score history and average confidence, pulled live from the database
- 🧑‍💼 **Admin Dashboard** — view all registered students and their performance stats

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python (Flask) |
| Database | MySQL |
| Local Server | XAMPP |

## 🚧 Project Status

This is an active academic project. Core auth, testing, and dashboard features are fully functional with a real database. Coding Practice, AI Interview Practice, and Resume Analyzer are planned as future scope.

---

# Setup Instructions

## Files in this project

**Frontend:**
- index.html, login.html, register.html, student-dashboard.html, admin-dashboard.html, aptitude.html
- style.css, script.js

**Backend:**
- app.py — Flask server (run this to start everything)
- schema.sql — Database structure (reference only — app.py creates tables automatically)
- seed_questions.py — Loads the 20 starter questions into the database
- requirements.txt — Python packages needed

## Folder Structure

```
PrepMate-Project/
├── frontend/
│   ├── index.html, login.html, register.html
│   ├── student-dashboard.html, admin-dashboard.html, aptitude.html
│   ├── style.css, script.js
├── backend/
│   ├── app.py
│   ├── schema.sql
│   ├── seed_questions.py
│   └── requirements.txt
├── question-bank.md
├── README.md
└── .gitignore
```

## First-Time Setup (do this once)

**1. Install Python packages**
Open a terminal **inside the `backend/` folder** and run:
```
pip install -r requirements.txt
```

**2. Start MySQL**
- Open XAMPP Control Panel
- Click **Start** next to MySQL (you do NOT need to start Apache)

**3. Create the database**
- Open your browser, go to `http://localhost/phpmyadmin`
- Click **New** (left sidebar)
- Name it exactly: `prepmate_db`
- Click **Create**

**4. Start the Flask server**
Make sure your terminal is still inside the `backend/` folder, then run:
```
python app.py
```
You should see:
```
Setting up database tables (if they don't already exist)...
Done. Starting Flask server at http://127.0.0.1:5000
```
This step automatically creates all your tables (students, admins, questions, scores, answer_log) and a default admin account.

**5. Load the starter questions (only once)**
Open a NEW terminal, navigate into the `backend/` folder again (keep app.py running in the first terminal), and run:
```
python seed_questions.py
```

**6. Open the site**
Go to: **http://127.0.0.1:5000**

## Login Details

**Default Admin Account:**
- Email: `admin@prepmate.com`
- Password: `********`

**Student Account:**
- Use the Sign Up page to create your own — it saves to the real database now.

## How to Run It Again Next Time (after closing everything)

1. Start MySQL in XAMPP
2. Open terminal in this folder → `python app.py`
3. Go to `http://127.0.0.1:5000`

(You do NOT need to run seed_questions.py again — questions are already saved.)

## Troubleshooting

**"Can't connect to MySQL"**
→ Make sure MySQL is started in XAMPP Control Panel (green "Running" status)

**"Unknown database 'prepmate_db'"**
→ You skipped Step 3 — create the database in phpMyAdmin first

**Page loads but login/signup doesn't work, shows "Could not reach the server"**
→ Make sure you're opening the site via `http://127.0.0.1:5000` (Flask), NOT via Live Server / opening index.html directly. Live Server can't run Python — only Flask can.

**"ModuleNotFoundError: No module named 'flask'" or similar**
→ Run `pip install -r requirements.txt` again

## What's Real vs What's Still Demo-Level

**Fully working with real database:**
- Registration & Login (Student + Admin, separate)
- Aptitude & Technical MCQ tests with the Confidence Rating feature
- Score history saved and shown on Student Dashboard
- Admin Dashboard showing real registered students and their stats

**Still placeholder / future scope (mention in your report):**
- Coding Practice — page not built yet
- AI Interview Practice — would need real AI integration
- Resume Analyzer — would need real AI integration
