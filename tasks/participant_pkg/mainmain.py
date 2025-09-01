# # TEE AND TEE WORK SHOP
# while True:
#     print("\nWelcome to learning AI 101:")
#     print("1. Register")
#     print("2. Registration Slip")
#     print("3. Exit")
#     choice = input("Enter choice: ")
#     if choice == "1":
#         try:
#             name = (input("Enter your name: ")) # collects user name
#             age = int(input("Enter your age: "))
#             phone = input("Enter Phone Num: ")
#             track = input("Enter Track: ")
#             if name.isalpha() == False:
#                 raise ValueError("Invalid Input, Enter a name.")
#             # collects user age
#             # elif len(phone) != 11:
#             #     raise ValueError("Enter Valid Number")
#             # elif track.isalpha() == False:
#             #     raise ValueError("Track cannot be empty")
#         except ValueError as e:
#            print("Error: ", e)

def get_age():
    while True:    
        try:
            age = (input("Enter your age: ")) # collects user age
            if not age.isnumeric():# validates user's input and ensure it's a  number
                print("Invalid input, Age must be a number")
        #     else:
        #         age_input = int(age) # converts the input to an intereger
        #         if age <=0:# validates user's input and ensure it's not 0 or negative
        #             print("Age can\'t be 0 or a negative number")
        #         else:
        #             return age_input # returns the age if all the right condition are met
        # except ValueError:
        #     print("Invalid Input, must be a number.")# prints Error message
        # except Exception:
        #     print("\nAn unexpected error occured")

get_age()