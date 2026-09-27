# PrepMate — Question Bank

This is your starter content for the Aptitude Tests and Technical MCQs features.
Later, we'll load these into the SQLite database using Python.

---

## APTITUDE QUESTIONS

**1.** A train 120m long is running at 60 km/hr. How long does it take to cross a pole?
A) 6.2 sec  B) 7.2 sec  C) 8.2 sec  D) 9.2 sec
**Answer: B**

**2.** If the cost price of 20 articles is equal to the selling price of 16 articles, what is the profit percentage?
A) 20%  B) 25%  C) 30%  D) 35%
**Answer: B**

**3.** What is the next number in the series: 2, 6, 12, 20, 30, ?
A) 40  B) 42  C) 44  D) 46
**Answer: B**

**4.** A can complete a work in 10 days, B in 15 days. Working together, how many days will they take?
A) 5 days  B) 6 days  C) 7 days  D) 8 days
**Answer: B**

**5.** Find the odd one out: 3, 5, 7, 9, 11, 13, 15
A) 9  B) 15  C) 7  D) None
**Answer: A** *(all others are prime, 9 is not)*

**6.** If A's speed is 20 km/hr and B's speed is 30 km/hr, and they start from the same point in opposite directions, how far apart are they after 2 hours?
A) 80 km  B) 90 km  C) 100 km  D) 110 km
**Answer: C**

**7.** A sum of money doubles itself in 8 years at simple interest. What is the rate of interest?
A) 10%  B) 12.5%  C) 15%  D) 20%
**Answer: B**

**8.** Complete the analogy: Book is to Reading as Fork is to ?
A) Drawing  B) Writing  C) Eating  D) Cutting
**Answer: C**

**9.** If 5 workers can build a wall in 20 days, how many days will 10 workers take?
A) 5 days  B) 10 days  C) 15 days  D) 20 days
**Answer: B**

**10.** What comes next: AZ, BY, CX, DW, ?
A) EV  B) EU  C) FV  D) FU
**Answer: A**

---

## TECHNICAL MCQs

### DBMS
**11.** Which of these is NOT a type of SQL command?
A) DDL  B) DML  C) DCL  D) DLL
**Answer: D**

**12.** A primary key can contain:
A) NULL values  B) Duplicate values  C) Only unique, non-null values  D) Any value
**Answer: C**

**13.** Which normal form removes partial dependency?
A) 1NF  B) 2NF  C) 3NF  D) BCNF
**Answer: B**

### Operating Systems
**14.** Which scheduling algorithm can cause starvation?
A) Round Robin  B) FCFS  C) Priority Scheduling  D) SJF (non-preemptive causes it too, but priority is classic answer)
**Answer: C**

**15.** What is a deadlock?
A) A process running forever  B) Two or more processes waiting on each other indefinitely  C) A crashed OS  D) A memory leak
**Answer: B**

### Computer Networks
**16.** Which layer of the OSI model handles routing?
A) Data Link  B) Network  C) Transport  D) Session
**Answer: B**

**17.** What does HTTP stand for?
A) HyperText Transfer Protocol  B) HighText Transfer Protocol  C) HyperText Transmission Process  D) None
**Answer: A**

### Programming Basics
**18.** What is the time complexity of binary search?
A) O(n)  B) O(log n)  C) O(n²)  D) O(1)
**Answer: B**

**19.** In programming, what is a "variable"?
A) A fixed value  B) A container that stores data that can change  C) A type of loop  D) A function
**Answer: B**

**20.** Which data structure uses LIFO (Last In, First Out)?
A) Queue  B) Stack  C) Array  D) Linked List
**Answer: B**

---

## HR / BEHAVIORAL INTERVIEW QUESTIONS
*(For your AI Interview Practice feature)*

1. Tell me about yourself.
2. Why should we hire you?
3. What are your strengths and weaknesses?
4. Describe a challenge you faced and how you solved it.
5. Where do you see yourself in 5 years?
6. Why do you want to work for this company?
7. Describe a time you worked in a team.
8. How do you handle pressure or tight deadlines?
9. What is your biggest achievement so far?
10. Do you have any questions for us?

---

## CODING PRACTICE PROBLEMS
*(For your Coding Practice feature — beginner level)*

1. **Reverse a String** — Write a program to reverse a given string.
2. **FizzBuzz** — Print numbers 1 to 100, but print "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for both.
3. **Find the Largest Number** — Given an array, find the largest element.
4. **Check Palindrome** — Check if a given string reads the same forwards and backwards.
5. **Count Vowels** — Count the number of vowels in a given string.

---

### Next steps for this content:
- Right now, this is just a reference document
- Once we build the database (Step 7), we'll write a small Python script that loads all these questions into your `questions` table automatically — you won't have to type them in one by one
