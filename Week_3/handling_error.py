# for i in range(3):
#     print(i)
# if 5 > 3: 
#     print("Hello")
# print ("Hello")
# x = 10 / 2   
# # print(age)
# result = "10" + 5 
# number = int("abc")
# fruits = ["apple", "banana"]
# print(fruits[3])
# data = {"name": "Ada"}
# print(data["age"])
# f = open("missing.txt") 
# try:
#     x = 10 / 2
#     print("Result:", x) 
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
try:
    f = open("sample.txt", "r")
    content = f.read()

except FileNotFoundError:
    print("File not found.")

finally:
    print("Closing file if it was opened.")
    
balance = 5000  # starting balance

print("Welcome to the ATM")
amount = input("Enter amount to withdraw: ")

try:
    amount = float(amount)  # convert input to number
    
    if amount > balance:
        raise ValueError("Insufficient funds.")
    
    balance -= amount
    print("Withdrawal successful. New balance: ₦", balance)

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Transaction session closed.")
