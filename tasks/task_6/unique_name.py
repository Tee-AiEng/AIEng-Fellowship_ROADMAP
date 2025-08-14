# task 2 unique name collector
names = input("Enter all names of Seminar attendees(seperated by (,)): ") # collects all input
lst_names = names.split(",") #splits the input 
set_name = set(lst_names) # covert to a set
print(sorted(set_name))
