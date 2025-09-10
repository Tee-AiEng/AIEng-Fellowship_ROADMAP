# 1. Using curly braces
fruits = {"apple", "banana", "mango"}
print(fruits)

# 2. Using the set() constructor
numbers = set([1, 2, 3, 4])
print(numbers)

# 3. Creating an empty set (must use set(), not {})
empty_set = set()
print(empty_set)

letters = set("mississippi")
print(letters)

# set operation
colors = {"red", "blue"}
colors.add("green")
print(colors)

colors.remove("blue")   # Removes an element, raises error if not found
colors.discard("yellow") # Removes if found, no error if missing
print(colors)