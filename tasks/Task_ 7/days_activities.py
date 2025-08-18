print("\nDays and Activities Pairing")
days = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday") # tuple containg list of days
days_dict = dict(enumerate(days , start = 1)) # numbers the days in the tuple so input can enter the numbers
print(days_dict)
index_chosen_days = input("Enter the number of of the days you want to record\nEnsure they are separated by comma(you can check the number above): ").split(",") # coolects the user's number of the days the want to record
int_index_days = [int(i) for i in index_chosen_days] # converts the entered numbers to interger since .splits() converts to strings instead of an interger as in the dic
chosen_days =tuple([days_dict[key] for key in int_index_days]) # records the value to the key(number of the day) in a tuple
print(chosen_days)
activities =tuple([input(f"Enter an activity for {day}: ") for day in chosen_days])# collects user activities for the days they inputed and converts it to a tuple
print(activities)# prints a tuple for the activities inputed

day_activities_dict = {day:activity for day, activity in zip(chosen_days,activities)} # maps activities to the days entered in a dict

print(day_activities_dict) # prints the dict




   