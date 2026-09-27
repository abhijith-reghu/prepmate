"""
PrepMate - Flask Backend
-------------------------
This file is the "brain" of PrepMate. It:
  1. Serves your HTML/CSS/JS files (the frontend)
  2. Connects to MySQL to store/read students, admins, questions, and scores
  3. Handles login, registration, quiz submission, and dashboard data via API routes

BEFORE RUNNING THIS FILE:
  1. Start MySQL in XAMPP Control Panel (click Start next to MySQL)
  2. Make sure you've created the "prepmate_db" database in phpMyAdmin
     (this file will auto-create the tables inside it on first run)
  3. Install requirements:  pip install flask mysql-connector-python werkzeug

TO RUN:
  IMPORTANT: Open your terminal INSIDE the backend/ folder first (cd backend),
  because this file finds the frontend using a relative path ('../frontend').
  Running it from anywhere else will break the file paths.

  python app.py
  Then open http://127.0.0.1:5000 in your browser
"""

from flask import Flask, request, jsonify, session, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')
app.secret_key = 'prepmate-secret-key-change-this-later'  # needed for login sessions

# ---------- DATABASE CONNECTION SETTINGS ----------
# Default XAMPP MySQL settings: user 'root', no password.
# If you set a password in XAMPP, put it in DB_CONFIG below.
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'prepmate_db'
}


def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)


# ---------- AUTO-CREATE TABLES ON STARTUP ----------
def setup_database():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            college VARCHAR(150),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admins (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            category VARCHAR(50) NOT NULL,
            question_text TEXT NOT NULL,
            option_a VARCHAR(255) NOT NULL,
            option_b VARCHAR(255) NOT NULL,
            option_c VARCHAR(255) NOT NULL,
            option_d VARCHAR(255) NOT NULL,
            correct_answer CHAR(1) NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT NOT NULL,
            test_type VARCHAR(50) NOT NULL,
            score INT NOT NULL,
            date_taken TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS answer_log (
            id INT AUTO_INCREMENT PRIMARY KEY,
            score_id INT NOT NULL,
            question_id INT NOT NULL,
            selected_answer CHAR(1),
            is_correct BOOLEAN,
            confidence INT,
            FOREIGN KEY (score_id) REFERENCES scores(id),
            FOREIGN KEY (question_id) REFERENCES questions(id)
        )
    """)

    # Seed a default admin account if none exists yet
    cursor.execute("SELECT COUNT(*) FROM admins WHERE email = %s", ('admin@prepmate.com',))
    if cursor.fetchone()[0] == 0:
        hashed = generate_password_hash('admin123')
        cursor.execute(
            "INSERT INTO admins (name, email, password) VALUES (%s, %s, %s)",
            ('Admin', 'admin@prepmate.com', hashed)
        )

    conn.commit()
    cursor.close()
    conn.close()


# ---------- SERVE FRONTEND PAGES ----------
@app.route('/')
def home():
    return send_from_directory('../frontend', 'index.html')


# Flask's static_folder already serves .html, .css, .js files directly,
# e.g. /login.html, /style.css, /script.js all work automatically.


# ---------- AUTH: REGISTER ----------
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    fullname = data.get('fullname', '').strip()
    email = data.get('email', '').strip().lower()
    college = data.get('college', '').strip()
    password = data.get('password', '').strip()

    if not fullname or not email or not password:
        return jsonify({'success': False, 'message': 'Please fill in all required fields.'})

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM students WHERE email = %s", (email,))
    if cursor.fetchone():
        cursor.close()
        conn.close()
        return jsonify({'success': False, 'message': 'An account with this email already exists.'})

    hashed_password = generate_password_hash(password)
    cursor.execute(
        "INSERT INTO students (name, email, password, college) VALUES (%s, %s, %s, %s)",
        (fullname, email, hashed_password, college)
    )
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()

    # Log them in immediately after registering
    session['user_id'] = new_id
    session['role'] = 'student'
    session['name'] = fullname

    return jsonify({'success': True})


# ---------- AUTH: LOGIN ----------
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email', '').strip().lower()
    password = data.get('password', '').strip()
    role = data.get('role', 'student')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    table = 'admins' if role == 'admin' else 'students'
    cursor.execute(f"SELECT * FROM {table} WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user or not check_password_hash(user['password'], password):
        return jsonify({'success': False, 'message': 'Invalid email or password.'})

    session['user_id'] = user['id']
    session['role'] = role
    session['name'] = user['name']

    return jsonify({'success': True})


# ---------- AUTH: LOGOUT ----------
@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'success': True})


# ---------- CURRENT LOGGED-IN USER INFO ----------
@app.route('/api/me')
def me():
    if 'user_id' not in session:
        return jsonify({'logged_in': False})
    return jsonify({
        'logged_in': True,
        'name': session['name'],
        'role': session['role']
    })


# ---------- GET QUESTIONS FOR A QUIZ ----------
@app.route('/api/questions')
def get_questions():
    category = request.args.get('category', 'aptitude')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM questions WHERE category = %s", (category,))
    questions = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(questions)


# ---------- SUBMIT A COMPLETED TEST (with confidence ratings) ----------
@app.route('/api/submit-test', methods=['POST'])
def submit_test():
    if 'user_id' not in session or session['role'] != 'student':
        return jsonify({'success': False, 'message': 'Please log in as a student first.'})

    data = request.get_json()
    test_type = data.get('test_type')
    score = data.get('score')
    answers = data.get('answers', [])  # list of {question_id, selected, correct, confidence}

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO scores (student_id, test_type, score) VALUES (%s, %s, %s)",
        (session['user_id'], test_type, score)
    )
    score_id = cursor.lastrowid

    for ans in answers:
        is_correct = (ans['selected'] == ans['correct'])
        cursor.execute(
            """INSERT INTO answer_log (score_id, question_id, selected_answer, is_correct, confidence)
               VALUES (%s, %s, %s, %s, %s)""",
            (score_id, ans['question_id'], ans['selected'], is_correct, ans['confidence'])
        )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'success': True})


# ---------- STUDENT'S OWN SCORE HISTORY (for their dashboard) ----------
@app.route('/api/my-scores')
def my_scores():
    if 'user_id' not in session:
        return jsonify({'total_tests': 0, 'average_score': 0, 'average_confidence': 0, 'history': []})

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, test_type, score, date_taken FROM scores WHERE student_id = %s ORDER BY date_taken DESC",
        (session['user_id'],)
    )
    rows = cursor.fetchall()

    history = []
    total_score = 0
    total_confidence = 0
    confidence_count = 0

    for row in rows:
        cursor.execute(
            "SELECT AVG(confidence) as avg_conf FROM answer_log WHERE score_id = %s",
            (row['id'],)
        )
        conf_result = cursor.fetchone()
        avg_conf = round(conf_result['avg_conf'], 1) if conf_result['avg_conf'] else 0

        history.append({
            'test_type': row['test_type'],
            'score': row['score'],
            'avg_confidence': avg_conf,
            'date': row['date_taken'].strftime('%d %b %Y')
        })
        total_score += row['score']
        if avg_conf:
            total_confidence += avg_conf
            confidence_count += 1

    cursor.close()
    conn.close()

    return jsonify({
        'total_tests': len(rows),
        'average_score': round(total_score / len(rows)) if rows else 0,
        'average_confidence': round(total_confidence / confidence_count, 1) if confidence_count else 0,
        'history': history
    })


# ---------- ADMIN: LIST ALL STUDENTS WITH THEIR STATS ----------
@app.route('/api/admin/students')
def admin_students():
    if 'user_id' not in session or session['role'] != 'admin':
        return jsonify({'error': 'Not authorized'}), 403

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, name, email, college FROM students")
    students = cursor.fetchall()

    result = []
    total_tests_all = 0
    total_score_all = 0

    for s in students:
        cursor.execute(
            "SELECT COUNT(*) as cnt, AVG(score) as avg_score FROM scores WHERE student_id = %s",
            (s['id'],)
        )
        stat = cursor.fetchone()
        tests_taken = stat['cnt'] or 0
        avg_score = round(stat['avg_score']) if stat['avg_score'] else 0

        total_tests_all += tests_taken
        total_score_all += (stat['avg_score'] or 0)

        result.append({
            'name': s['name'],
            'email': s['email'],
            'college': s['college'],
            'tests_taken': tests_taken,
            'avg_score': avg_score
        })

    cursor.close()
    conn.close()

    return jsonify({
        'total_students': len(students),
        'total_tests': total_tests_all,
        'platform_average': round(total_score_all / len(students)) if students else 0,
        'students': result
    })


if __name__ == '__main__':
    print("Setting up database tables (if they don't already exist)...")
    setup_database()
    print("Done. Starting Flask server at http://127.0.0.1:5000")
    app.run(debug=True)
