name = input("Enter name of place: ") #que 1:collect string input from user
print(f"{name.upper()}") #que 1: convert user's input to upper case
var = "Python" # que 2: assign a value to a variable
print(var[0]) # que 2: prints the the first charcter of the value assigned to the varaible
print(var[-1]) # que 2: prints the the last charcter of the value assigned to the varaible
name_1 = input("enter name: ")
print(f"Hello {name}!") # que 3:prints Hello user's input
value = "Toyeebat"
print(value.rindex(value[-1])+1) #  que 4: counts the number of character in a string

code = "Hello World"
print(code.replace("World","Python")) #que 5, replaces world with python
#TASK 2
string = "I am learning python"
print("python" in string) # que 6; confirms if the substring  python is in the string
charc = "Ayodele"
print("".join(reversed(charc))) # que 7: reverses the string
str = "    Ayodele    "
print(str.lstrip().rstrip())
# que 9:
text = input("Enter a sentence: ")
text = text.lower()
number_of_vowls = text.count("a") + text.count("e") + text.count("o") + text.count("i") + text.count("a")
print(number_of_vowls)
# Que 10
number = "1233"
print(int(number) * 2)

# QUE 11
fruit = ["apple,banana,orange"]
print()

