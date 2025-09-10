name = "Ada Balogun"
print(name.upper())

sentence = "python is amazing"
print(sentence.title())

text = "   Abuja   "
print(text.strip()) 

message = "I love Java"
print(message.replace("Java", "Python"))

text = "Hello ABEOKUTA"
print(text.swapcase())

text = "   Nigeria"
print(text.lstrip())  

text = "Nigeria   "
print(text.rstrip())

fruits = "mango orange banana"
print(fruits.split()) 

text = "one,two,three,four,five"
print(text.rsplit(",",1))

lines = "Line 1\nLine 2\nLine 3"
print(lines.splitlines())

words = ["I","love","Python"]
print(" ".join(words))
text = "Python"
print(text.center(20, "-"))
text_1 = "Python"
print(text.ljust(10,"*"))

text_1 = "Python"
print(text.rjust(10,"*"))

num = "42"
print(num.zfill(5))

print("Lagos".isalpha())
print("Lagos234".isalpha())
print("123456".isdigit())
print("1256asd".isdigit())

print("Python6".isalnum())
print("Python 6".isalnum())
