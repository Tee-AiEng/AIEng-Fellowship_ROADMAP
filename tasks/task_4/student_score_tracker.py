
# task_5
name = [] # empty list
score = [] # empty list
nam = input("Enter name: ") # collects input
nam_1 = input("Enter name: ") # collects input
nam_2 = input("Enter name: ") # collects input
scr = input("Enter score: ") # collects input
scr_1 = input("Enter score: ")# collects input
scr_2 = input("Enter score: ") # collects input

name.append(nam) # add to the list
name.append(nam_1) # add to the list
name.append(nam_2)  # add to the list

score.append(scr) # add to the list
score.append(scr_1) # add to the list
score.append(scr_2) # add to the list
print("Name\t| Score")
print("="*20)
print(f"{name[0]} \t | {score[0]}")
print(f"{name[1]} \t | {score[1]}")
print(f"{name[2]} \t | {score[2]}")