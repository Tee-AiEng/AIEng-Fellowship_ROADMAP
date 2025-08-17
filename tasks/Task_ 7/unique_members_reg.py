print("\nUnique Members Registration")
names = input("Enter 3 names separated by a ,: ").title().split(",") # colects 3 names separated by a comma from the user, convets it to proper noun and splits
set_of_names = set(names) # converts the name to a splitted name to a set
dict_of_name = {name:len(name) for name in set_of_names} # creates a dictionary in which the name entered is the key and length of name is the value
print(dict_of_name) # prints the dictionary