-- PrepMate Database Schema
-- Run this in phpMyAdmin (SQL tab) after creating the "prepmate_db" database,
-- OR just run app.py once — it auto-creates these tables if they don't exist.

CREATE DATABASE IF NOT EXISTS prepmate_db;
USE prepmate_db;

-- Students table
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    college VARCHAR(150),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Admins table
CREATE TABLE IF NOT EXISTS admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Questions table
CREATE TABLE IF NOT EXISTS questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50) NOT NULL,      -- 'aptitude' or 'technical'
    question_text TEXT NOT NULL,
    option_a VARCHAR(255) NOT NULL,
    option_b VARCHAR(255) NOT NULL,
    option_c VARCHAR(255) NOT NULL,
    option_d VARCHAR(255) NOT NULL,
    correct_answer CHAR(1) NOT NULL     -- 'A', 'B', 'C', or 'D'
);

-- Scores table — one row per completed test
CREATE TABLE IF NOT EXISTS scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    test_type VARCHAR(50) NOT NULL,
    score INT NOT NULL,                  -- percentage, e.g. 80
    date_taken TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- Answer log table — one row per question answered, stores the Confidence Rating (flagship feature)
CREATE TABLE IF NOT EXISTS answer_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    score_id INT NOT NULL,
    question_id INT NOT NULL,
    selected_answer CHAR(1),
    is_correct BOOLEAN,
    confidence INT,                      -- 1 to 5 stars
    FOREIGN KEY (score_id) REFERENCES scores(id),
    FOREIGN KEY (question_id) REFERENCES questions(id)
);

-- Note: the default admin account (admin@prepmate.com / admin123) is created
-- automatically by app.py on first run, with a properly hashed password.
-- We don't insert it here in plain SQL because passwords must be hashed by Python, not stored as plain text.
