







# task_6
word = input("Enter a word: ") # collects an input
is_upper = word.isupper() #checks if the input is in upper case
print(f"the word is in upper case: {is_upper}")
lower_case = word.islower() #checks if the input is in lower case
print(f"the word is in lower case: {lower_case}") 
proper = word.istitle() #checks if the input is in lower case
print(f"the word is in lower case: {proper}")

print(word[::-1]) # reverse the word


# task_7
cities = ["Ibadan","Lagos","Abuja","LA","Miami"] # a list of cities
city = input("Enter a city: ") # collects an input(cities)
cities[2] = city # changes the second value in the list with the new input
cities.pop(-1) # removes the last city in list of cities
cities.insert(0,"London") # insert a new city at the begining 
print(cities) #prints the  new list of cities

