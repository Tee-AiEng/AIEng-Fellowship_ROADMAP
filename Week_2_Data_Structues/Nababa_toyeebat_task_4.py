# task_1
quote = input("Enter your favorite quote: ") # coolects an input from user
print(f"\"{quote.title()}\"") # prints input in title format with quoted marks

# task_2
items = [] # empty list
itm_1 = input("Enter item: ") # collects input
itm_2 = input("Enter item: ") # collects input
itm_3 = input("Enter item: ") # collects input
items.append(itm_1) # add to the empty list
items.append(itm_2) # add to the empty list
items.append(itm_3) # add to the empty list
res = (",".join(items)) # joins the list 
print(str(res)) # convert to string

# task_3
sen = input("Enter a sentence: ") # collects input
words = sen.split() # split the input to words
print(len(words)) # prints the number of words

# task_4
names = input("Enter 5 names(separated by spaces): ")
split_names = names.lower().split(" ")
split_names.sort()
print(split_names)
all_names = [print(f"{name}") for name in split_names]

# task_5
name = []
score = []
nam = input("Enter name: ")
nam_1 = input("Enter name: ")
nam_2 = input("Enter name: ")
scr = input("Enter score: ")
scr_1 = input("Enter score: ")
scr_2 = input("Enter score: ")

name.append(nam)
name.append(nam_1)
name.append(nam_2)

score.append(scr)
score.append(scr_1)
score.append(scr_2)
print("Name\t| Score")
print("="*20)
print(f"{name[0]} \t | {score[0]}")
print(f"{name[1]} \t | {score[1]}")
print(f"{name[2]} \t | {score[2]}")

# task_6
word = input("Enter a word: ")
is_upper = word.isupper()
print(f"the word is in upper case: {is_upper}")
lower_case = word.islower()
print(f"the word is in lower case: {lower_case}")
proper = word.istitle()
print(f"the word is in lower case: {proper}")

print(word[::-1])


# task_7
cities = ["Ibadan","Lagos","Abuja","LA","Miami"]
city = input("Enter a city: ")
cities[2] = city
cities.pop(-1)
cities.insert(0,"London")
print(cities)

