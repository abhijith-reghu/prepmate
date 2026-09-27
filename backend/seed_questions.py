"""
PrepMate - Question Seeder
----------------------------
Run this ONCE after app.py has created the database tables, to load
the starter question bank into MySQL automatically.

TO RUN:
  python seed_questions.py
"""

import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'prepmate_db'
}

# Format: (category, question, option_a, option_b, option_c, option_d, correct_answer)
QUESTIONS = [
    # ---------- APTITUDE ----------
    ('aptitude', 'A train 120m long is running at 60 km/hr. How long does it take to cross a pole?',
     '6.2 sec', '7.2 sec', '8.2 sec', '9.2 sec', 'B'),
    ('aptitude', 'If the cost price of 20 articles equals the selling price of 16 articles, what is the profit %?',
     '20%', '25%', '30%', '35%', 'B'),
    ('aptitude', 'What is the next number in the series: 2, 6, 12, 20, 30, ?',
     '40', '42', '44', '46', 'B'),
    ('aptitude', 'A can complete a work in 10 days, B in 15 days. Working together, how many days will they take?',
     '5 days', '6 days', '7 days', '8 days', 'B'),
    ('aptitude', 'Find the odd one out: 3, 5, 7, 9, 11',
     '9', '5', '7', 'None', 'A'),
    ('aptitude', "A's speed is 20 km/hr, B's speed is 30 km/hr, opposite directions. Distance apart after 2 hours?",
     '80 km', '90 km', '100 km', '110 km', 'C'),
    ('aptitude', 'A sum of money doubles itself in 8 years at simple interest. What is the rate of interest?',
     '10%', '12.5%', '15%', '20%', 'B'),
    ('aptitude', 'Book is to Reading as Fork is to?',
     'Drawing', 'Writing', 'Eating', 'Cutting', 'C'),
    ('aptitude', 'If 5 workers build a wall in 20 days, how many days will 10 workers take?',
     '5 days', '10 days', '15 days', '20 days', 'B'),
    ('aptitude', 'What comes next: AZ, BY, CX, DW, ?',
     'EV', 'EU', 'FV', 'FU', 'A'),

    # ---------- TECHNICAL ----------
    ('technical', 'Which of these is NOT a type of SQL command?',
     'DDL', 'DML', 'DCL', 'DLL', 'D'),
    ('technical', 'A primary key can contain:',
     'NULL values', 'Duplicate values', 'Only unique, non-null values', 'Any value', 'C'),
    ('technical', 'Which normal form removes partial dependency?',
     '1NF', '2NF', '3NF', 'BCNF', 'B'),
    ('technical', 'Which scheduling algorithm can cause starvation?',
     'Round Robin', 'FCFS', 'Priority Scheduling', 'SJF', 'C'),
    ('technical', 'What is a deadlock?',
     'A process running forever', 'Two or more processes waiting on each other indefinitely',
     'A crashed OS', 'A memory leak', 'B'),
    ('technical', 'Which layer of the OSI model handles routing?',
     'Data Link', 'Network', 'Transport', 'Session', 'B'),
    ('technical', 'What does HTTP stand for?',
     'HyperText Transfer Protocol', 'HighText Transfer Protocol',
     'HyperText Transmission Process', 'None', 'A'),
    ('technical', 'What is the time complexity of binary search?',
     'O(n)', 'O(log n)', 'O(n^2)', 'O(1)', 'B'),
    ('technical', 'In programming, what is a "variable"?',
     'A fixed value', 'A container that stores data that can change', 'A type of loop', 'A function', 'B'),
    ('technical', 'Which data structure uses LIFO (Last In, First Out)?',
     'Queue', 'Stack', 'Array', 'Linked List', 'B'),
]


def seed():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM questions")
    existing_count = cursor.fetchone()[0]

    if existing_count > 0:
        print(f"Questions table already has {existing_count} questions. Skipping to avoid duplicates.")
        print("If you want to reload, first run: DELETE FROM questions; in phpMyAdmin.")
        cursor.close()
        conn.close()
        return

    for q in QUESTIONS:
        cursor.execute(
            """INSERT INTO questions (category, question_text, option_a, option_b, option_c, option_d, correct_answer)
               VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            q
        )

    conn.commit()
    print(f"Successfully added {len(QUESTIONS)} questions to the database!")
    cursor.close()
    conn.close()


if __name__ == '__main__':
    seed()
