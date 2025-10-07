# 🥗 Daily Calorie Tracker (Python CLI Project)

**Author:** Vaishnavi Jha  
**Date:** 7 October 2025  
**Project Type:** Command Line Interface (CLI)  
**Language:** Python  

---

## 📖 Project Overview

The **Daily Calorie Tracker** is a simple Python-based command line tool that helps you log your meals, calculate your total and average calorie intake, and compare it against your daily calorie limit.  
It’s a great beginner-friendly project to practice **loops, lists, conditionals, file handling**, and **basic input/output operations** in Python.

---

## 🎯 Features

✅ User-friendly CLI interface  
✅ Log multiple meals with calorie values  
✅ Calculates **total** and **average** calorie intake  
✅ Compares against a **daily calorie limit**  
✅ Displays formatted meal summary table  
✅ (Bonus) Option to **save session logs** in a text file (`calorie_log.txt`)  
✅ Motivational and funny responses 😄  

---

## ⚙️ How It Works

1. Run the script using Python.
2. Enter the number of meals you want to log.
3. For each meal, input:
   - Meal name
   - Calories
4. Enter your **daily calorie limit**.
5. View your results:
   - Total calories consumed  
   - Average calories per meal  
   - Whether you stayed within your limit or exceeded it  
6. Choose whether to **save the session log** to a text file.

---

## 🧠 Example Output

Welcome to the Daily Calorie Tracker!
This tool helps you calculate total calorie intake,
compare it with your daily limit, and save yourself from obesity🤭

How many meals do you want to enter today? 3
Enter meal #1 name: Breakfast
Enter calories for Breakfast: 250
Enter meal #2 name: Lunch
Enter calories for Lunch: 600
Enter meal #3 name: Dinner
Enter calories for Dinner: 500

All meals recorded successfully!

Enter your daily calorie limit: 1400

Calculating results...

Meal Name Calories
----------------incoming------------------
Breakfast 250.0
Lunch 600.0
Dinner 500.0

Total: 1350.0
Average: 450.00
✅ Great job! You’re within your daily calorie limit, you can eat fast foods now...hehehe.

Do you want to save this session? (yes/no): yes
Session saved successfully to calorie_log.txt ✅


---

## 🗂️ Log File Example

If you choose to save your session, the program creates or appends to `calorie_log.txt`:



=== Daily Calorie Tracker Log ===
Date: 2025-10-07 22:35:18

Breakfast: 250.0 calories
Lunch: 600.0 calories
Dinner: 500.0 calories

Total: 1350.0
Average: 450.00
Status: ✅ Great job! You’re within your daily calorie limit, you can eat fast foods now...hehehe.

---

## 💻 Installation & Usage

### 1️⃣ Requirements
- Python 3.x installed on your system

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/jvaishnavi0406-beep/Python-project
cd Python-project

3️⃣ Run the Script
python tracker.py

🧩 Concepts Used

Input/Output operations (input(), print())

Lists and loops (for, append)

Conditional statements (if/else)

Mathematical calculations (sum(), average)

File handling (open, write, append)

Using Python’s datetime module

🌟 Future Improvements

🚀 Add calorie recommendations based on gender, age, and goals
📊 Visualize calorie trends using charts (matplotlib)
💾 Store data in CSV or JSON format
🧠 Add user authentication and history tracking

📜 License

This project is open-source and free to use for learning and personal development.

💬 Made with love and laughter by Vaishnavi Jha 💚


