# task 4
name_1 = input("Enter name: ")# coolects input
age_1 = int(input("Enter age: "))# coolects input
fav_color_1 = input("Enter fav color: ")# coolects input
home_town_1 = input("Enter hometown: ")# coolects input
profile = (name_1,age_1,fav_color_1,home_town_1)# stores the inputs in a tuple
name,age,fav_color,home_town = profile #unpacks the tuple
print(f"First name: {name}\nAge: {age}\nFavorite color: {fav_color}\nHome town: {home_town}") #prints