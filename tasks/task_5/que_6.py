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

