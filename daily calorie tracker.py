# tracker.py
# Author: [Vaishnavi Jha]
# Date: [7 October 2025]
# Project: Daily Calorie Tracker

# setup & introduction
print("Welcome to the Daily Calorie Tracker!")
print("This tool helps you calculate total calorie intake,")
print("compare it with your daily limit, and save yourself from obesity🤭\n")

#input and data collection
meal_names = []
meal_calories = []

num_meals = int(input("How many meals do you want to enter today? "))

for x in range(num_meals):
    meal = input(f"Enter meal #{x+1} name: ")
    cal = float(input(f"Enter calories for {meal}: "))
    meal_names.append(meal)
    meal_calories.append(cal)

print("\nAll meals recorded successfully!\n")

# Calorie Calculation 
total_calories = sum(meal_calories)
average_calories = total_calories / len(meal_calories)

daily_limit = float(input("Enter your daily calorie limit: "))

print("\nCalculating results...\n")

# Exceed Limit Warning System
if total_calories > daily_limit:
    status = "⚠️ Warning: You have exceeded your daily calorie limit, you may gain unecessary weight!"
else:
    status = "✅ Great job! You’re within your daily calorie limit, you can eat fast foods."

# Neatly Formatted Output
print("Meal Name\tCalories")
print("----------------incoming------------------")
for meal, cal in zip(meal_names, meal_calories):
    print(f"{meal}\t\t{cal}")
print("----------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")
print(status)

# (Bonus): Save Session Log to File
from datetime import datetime

save_choice = input("\nDo you want to save this session? (yes/no): ").strip().lower()

if save_choice == "yes":
    filename = "calorie_log.txt"
    with open(filename, "a") as file:
        file.write("=== Daily Calorie Tracker Log ===\n")
        file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for meal, cal in zip(meal_names, meal_calories):
            file.write(f"{meal}: {cal} calories\n")
        file.write(f"\nTotal: {total_calories}\nAverage: {average_calories:.2f}\n")
        file.write(f"Status: {status}\n")
        file.write("----------------------------------\n\n")
    print(f"\nSession saved successfully to {filename} ✅")
else:
    print("\nSession not saved.")



