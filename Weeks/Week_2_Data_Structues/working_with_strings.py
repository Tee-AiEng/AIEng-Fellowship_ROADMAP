name = 'Ada' #single qoutes
print(name)
greetings = "Hello" #double qoutes
print(greetings)
# triple quotes (for multi_line strings)
story = """ Once upon a time, there was a coder named Ada"""
print(story)
# strings with number and symbol
password = "p@ssw0rd123" 
print(password)

word = "Python"
print(word[1])  # P
print(word[-1]) # n

word = "Python."
print(word[0:4])   # Pyth
print(word[2:])    # thon
print(word[:3])    # Pyt
print(word[::2])   # Pto
print(word[::-1])

a = "Hello"
b = "World"
print(a + " " + b)
word = "Hi! "
print(word * 3)

text = "Python programming"
print("Python" in text)   
print("Java" not in text)

text = "Hello World"
print(text.find("o"))   
print(text.rfind("o")) 

text = "Hello World"
print(text.index("World")) 

filename = "data.csv"
print(filename.startswith("data"))
print(filename.endswith(".csv"))

