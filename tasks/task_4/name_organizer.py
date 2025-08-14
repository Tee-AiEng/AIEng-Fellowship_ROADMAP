# task_4
names = input("Enter 5 names(separated by spaces): ") # coolects an input from user
split_names = names.lower().split(" ") # convert to lwer case, then splits
split_names.sort() # sorts the name
print(split_names)
all_names = [print(f"{name}") for name in split_names] # prints the name in new line