# # # example usses of in-built finctions
# # # range()
# # for i in range(3):
# #     print(i)
# # # zip()
# # names = ["Esther", "Precious", "Kennie"]
# # score = [85,90,75]
# # for n,s in zip(names, score):
# #     print(n, "scored", s)
# # # map()
# # nums = [1,2,3,4]
# # squred = list(map(lambda x: x**2, nums))
# # print(squred)
# # # filter()
# # even_nums = list(filter(lambda x: x%2 == 0, nums))
# # print(even_nums)


# #step 1 : Input studen data
# name1 = input("Enter name for first student: ")
# score1 = int(input(f"Enter score for {name1} : "))

# name2 = input("Enter name for first student: ")
# score2 = int(input(f"Enter score for {name2} : "))

# name3 = input("Enter name for first student: ")
# score3 = int(input(f"Enter score for {name3} : "))

# name4 = input("Enter name for first student: ")
# score4 = int(input(f"Enter score for {name4} : "))

# #Step3: Display data
# names = [name1,name2,name3,name4]
# scocres = [score1,score2,score3,score4]

# #step 3 : dispaly data
# print("\nStudent Data:")
# for index, (n,s) in enumerate(zip(names, scocres)):
#     print(f"{index + 1}. {n} - {s}")

# # step 4: summary using built-ins
# total = sum(scocres)
# average = round(total/ len(scocres),2)
# higest = max(scocres)
# lowest = min(scocres)

# print("\nPerformanc Summary")
# print(f"Total Score: {total}")
# print(f"Average Score: {average}")
# print(f"Highest Score: {higest}")
# print(f"Lowest Score: {lowest}")

# # step 5: ranking using sorted and zip
# ranked = sorted(zip(scocres,names), reverse = True)
# for rank, (score, name) in enumerate(ranked,1):
#     print(f"{rank}. {name} - {score}")

# # step 6: check data types
# print("\nData Type Checks:")
# print("Type of names:", type(names))
# print("Type of scores:", type(scocres))
# print("ID of names list:", id(names))
# print("ID of scores list:", id(scocres))

# # step 7:filter passing students (>=50)
# passing = list(filter(lambda s: s>=50, scocres))
# print("\nPassing scores:", passing)

# # atep 8: map names to upper case
# upper_names = list(map(lambda n : n.upper(),names))
# print("Upeercase Names:", upper_names)

# # Step 9: Use help() to show documentation of len
# print("\nHelp on len():")
# help(len)


# USER-DEFINED FUNCTION 
def greet():
    print("Hello, welcome to AI fellowship!")

greet()
def greet(name):
    print("Hello",name, "welcome to AI fellowship!")

greet("Class rep")
greet("Ridwan")

def greeet(name):
    print("Hello", name)

result = greeet("Esther")
print("Result:", result)

def add(a,b):
    return a + b
result = add(4,6)
print("The sum is:",result)

def count_up_to(n):
    i = 1
    while i <= n:
        yield i   # pause and return i
        i += 1
for number in count_up_to(6):
    print(number)

# positional areguments
def introduce(name, track):
    print("My name is", name)
    print(f"I am learning {track}.")
# function call
introduce("Nogozi","AI Engineering")
introduce("AI Engineering","Ngozi")
# keywoord arguments
def introduce(name, track):
    print("My name is", name)
    print(f"I am learning {track}.")
# function call
introduce(name = "Ngozi", track = "AI Engineering")
introduce(track = "AI Engineering",name = "Ngozi")

# default argument
def introducce(name, track = "AI Engineering"):
    print("My name is", name)
    print(f"I am learning {track}.")

introducce("Paul")

introduce("Tunji Paul", track = "AI Development")

# varying length arguments
# non-keyword(tuple)
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
        print("Sum:", total)
add_numbers(2,4,6)
add_numbers(10,20,30,40,50)
# keyword argument(dictionary)
def student_details(**kwargs):
    for key,value in kwargs.items():
        print(key, ":", value)

student_details(name="Peter", track = "AI Engineering", interest="Block Chain")

def participant_profile(name, age, track = "AI Engineering", *skills, **extra_info):
     """
    Generate a profile for a bootcamp participant using different types of arguments.
    """
     profile = f"\n--- Bootcamp Participant Profile ---\n"
     profile += f"Name: {name}\n"
     profile += f"Age: {age}\n"
     profile += f"Track: {track}\n"

     #skills from(*args)
     if skills:
         profile += "Skills: " + ",".join(skills) + "\n"
     else:
         profile += "Skills: Not yet specified\n"

     # Extra info (from **kwargs)
     if extra_info:
         profile += "Additional:\n"
         for key, value in extra_info.items():
             profile += f"- {key.capitalize()}: {value}\n"

     return profile
# Example 1: Using only positional arguments
print(participant_profile("Peter", 24))
# Example 2: Adding keyword/default argument
print(participant_profile("Ridwan", 29, track="AI Engineering"))
# Example 3: Adding variable-length positional arguments (*args)
print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine Learning"))
print(participant_profile(
    "Sophia", 30, "Cybersecurity",
    "Networking", "Ethical Hacking", "Python",
    interest="Blockchain", city="Shagamu", phone="08123456789"
))


