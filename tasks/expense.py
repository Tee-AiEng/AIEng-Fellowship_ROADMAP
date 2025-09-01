import csv
from datetime import datetime

def add_expense(date, category, amount, description):
    with open("expenses.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
    
        writer.writerow([date, category, amount, description])
        
def view_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expense records found.")
def del_expenses():
    data = view_expenses()
    for idx,data in enumerate(data):


while True:
    print("Welcome to expense tracker")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Delete Expense")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        date = datetime.today().strftime("%Y-%m-%d")
        category = input("Enter expense category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        add_expense(date, category, amount, description)
        print("Expense added successfully!")
    elif choice == "2":
        print("Here are your recorded expenses:")
        view_expenses()
    elif choice == "3":
        print("are you sure? yes or no")
        ans = input("Enter answer: ").lower()
        if ans == "yes":
            break




