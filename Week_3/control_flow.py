# `if Statement
age = 20
if age >= 18:
    print("You are eligible to vote")
# `if-else` Statement
wallet = 400
price = 500
if wallet >= price:
    print("Purchase succesful")
else: 
    print("Insufficient balance")

# `if-elif-else` Statement

score = 85
if score >= 70:
    print("Grade A")
elif score >=50:
    print("Grade B")
else:
    print("Grade C")
#  Nested if
age = 19
citizen = True
if age >= 18:
    if citizen:
        print("you can vote")
    else:
        print("You have to be a citizen to vote")
else:
    print("Too young to vote")
# for loop
fruits = ["apple","banana","orange"]
for fruit in fruits:
    print(f"I like {fruit}")
cordinates = (0.3456,-0.45667,0.0989)
for point in cordinates:
    print(f"Point: {point}")
student = {"name": "Tunde", "Age": 16, "grade": "A"}
for key,value in student.items():
    print(f"{key}:{value}")

word = "PYTHON"
for char in word:
    print(char)

# while loop
count = 1
while count <= 5:
    print("Number:", count)
    count +=1

num = 1
while num <= 10:
    print(num, end = " ")
    num += 1
timer = 10
while timer > 0:
    print("Countdown:",timer)
    timer -= 1
password = ""
while password != "python123":
    password = input("Enter the password: ")
print("Access Granted")

# while true
while True:
    name = input("Enter your name(type 'exit' to quit): ")
    if name.lower() == "exit":
        print("Goodbye!")
        break
    print(f"Hello, {name}")
for num in range(1,10):
    if num == 5:
        break
    print(num)
for num in range(1,6):
    if num == 3:
        continue
    print(num)
for num in range(1,6):
    if num == 3:
        pass
    else:
        print(num)

while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")

    choice = input("Choice an option")

    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Goodbye")
    elif choice == "3":
         print("Exiting program...")
         break
    else:
         print("Invalid choice. Try again.")

while True:
    age = input("Enter your age: ")
    if age.isdigit():
        print(f"Your age is {age}")
        break
    else:
        print("Invalid input. Please enter a number.")
