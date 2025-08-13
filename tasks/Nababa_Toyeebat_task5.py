# Task_1
dishes = [] #empty list
fav_food = input("Enter Favorite food: ") # coolects input
fav_food_1 = input("Enter Favorite food: ") # coolects input
fav_food_2 = input("Enter Favorite food: ") # coolects input
dishes.append(fav_food) # adds to thr empty list
dishes.append(fav_food_1) # adds to thr empty list
dishes.append(fav_food_2) # adds to thr empty list
t = tuple(dishes) # converts to tuple
print(t) # prints the variable t
food1, food2, food3 = t # unpacks tuple
print(f"{food1}\n{food2}\n{food3}") # prints the value in differnt 

# task 2
bfs = [] # empty list
best_frind = input("Enter 5 best friends name: ") # coolects input
best_frind1 = input("Enter 5 best friends name: ")# coolects input
best_frind2 = input("Enter 5 best friends name: ")# coolects input
best_frind3 = input("Enter 5 best friends name: ")# coolects input
best_frind4 = input("Enter 5 best friends name: ")# coolects input
bfs.append(best_frind) # adds to thr empty list
bfs.append(best_frind1) # adds to thr empty list
bfs.append(best_frind2) # adds to thr empty list
bfs.append(best_frind3) # adds to thr empty list
bfs.append(best_frind4) # adds to thr empty list
friends = tuple(bfs)# converts to tuple
print(friends[::-1]) # reverse the tuple

# task 3
states = [] # empty list
state1 = input("Enter state: ")# coolects input
state2 = input("Enter state: ")# coolects input
state3 = input("Enter state: ")# coolects input
state4 = input("Enter state: ")# coolects input
state5 = input("Enter state: ")# coolects input
states.append(state1)# adds to thr empty list
states.append(state2)# adds to thr empty list
states.append(state3)# adds to thr empty list
states.append(state4)# adds to thr empty list
states.append(state5)# adds to thr empty list
states_tuple = tuple(states)# converts to tuple
print(states_tuple[0])# prints the first value in the tuple
print(states_tuple[-1])# prints the last value in the tuple
print("lagos" in states_tuple) # checks if lagos is in the tuple
print("lagos" not in states_tuple)# checks if lagos is not in the tuple
print(len(states_tuple)) # prints the length of the tuple

# task 4
name_1 = input("Enter name: ")# coolects input
age_1 = int(input("Enter age: "))# coolects input
fav_color_1 = input("Enter fav color: ")# coolects input
home_town_1 = input("Enter hometown: ")# coolects input
profile = (name_1,age_1,fav_color_1,home_town_1)# stores the inputs in a tuple
name,age,fav_color,home_town = profile #unpacks the tuple
print(f"First name: {name}\nAge: {age}\nFavorite color: {fav_color}\nHome town: {home_town}") #prints 

# task 5
item1 = input("Enter item: ")# coolects input
item2 = input("Enter item: ")# coolects input
item3 = input("Enter item: ")# coolects input
shoping_list = (item1,item2,item3)# stores the inputs in a tuple
shoping_list_lst = list(shoping_list)# converts to list
item4 = input("Enter item: ")# coolects input
item5 = input("Enter item: ")# coolects input
shoping_list_lst.append(item4)# adds to a list
shoping_list_lst.append(item5)# adds to a list
update_list = tuple(shoping_list_lst)# converts a list to tuple
print("|".join(update_list)) #joins the tuple with a |

days = ("sunday","monday","tuesday","wednesday","thursday","friday","saturday") # a tuple containing a list of days
print(days)
months = ("January","Febuary","March","April","May","June","July","August","September","October","November","December") # a tuple containing a list of months
print(months)

name = input("Enter name: ") # collects input
gender = input("Enter gender: ") # collects input
course = input("course track: ") # collects input
month = int(input("Enter month(1-12): ")) # collects input
day= int(input("Enter day(1-7): ")) # collects input
att_day=days[day-1] # subtracts 1 from the index of the enterted number for day
att_month=months[month-1] # subtracts 1 from the index of the enterted number for month

print(f"Name\t|Gender\t|Course\t|Month\t|Day\n{name}\t|{gender}\t|{course}\t|{att_month}\t|{att_day}")#prints an attedance list

