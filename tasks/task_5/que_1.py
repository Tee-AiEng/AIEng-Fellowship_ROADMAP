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
