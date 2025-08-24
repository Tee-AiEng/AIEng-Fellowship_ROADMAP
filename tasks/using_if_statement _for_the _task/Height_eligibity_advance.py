# # # it can be use to check eligibilty for air hostess job
# # # Eligibility check for Air Hostess job with multiple airlines

# # # Requirements database (airline : [min_height, min_age])
# # airline_requirements = {
# #     "Air Peace": [160, 25],
# #     "Arik Air": [165, 23],
# #     "Dana Air": [158, 22],
# #     "Emirates": [170, 21],
# #     "Qatar Airways": [168, 21]
# # }

# # print("Welcome to Air Hostess Eligibility Checker")
# # print("Available Airlines:")
# # for i, airline in enumerate(airline_requirements.keys(), start=1):
# #     print(f"{i}. {airline}")
# # # User selects airline
# #     choice = int(input("\nSelect an airline (enter number): "))
# #     airline_list = list(airline_requirements.keys())
# #     if 1 <= choice <= len(airline_list):
# #         selected_airline = airline_list[choice - 1]
# #         min_height, min_age = airline_requirements[selected_airline]
# #         avg_height = 155
# #         avg_age = 21
# #         print(f"\nYou selected: {selected_airline}")
# #         print(f"Average Requirements → Min Height: {avg_height}cm, Min Age: {avg_age} years\nPlease note this requirement may differ across airlines.")
# #         # User enters details
# #         user_height = float(input("Enter your height (in cm): "))# user"s height
# #         user_age = int(input("Enter your age: "))# user's age
# #          # Check conditions
# #         if user_age >= min_age and user_height >= min_height:
# #             print(f"Congratulations! You are eligible for {selected_airline}. Proceed to the next stage.")
# #         elif user_age < min_age:
# #             print(f"Sorry, you are too young for {selected_airline}.\n Minimum age is {min_age}.You can try other availble Airline")
# #         elif user_height < min_height:
# #             print(f"Sorry, you do not meet the minimum height requirement for {selected_airline}.\nMinimum height is {min_height}You can try other availble Airline")
# #         else:
# #             print("You do not meet the eligibility criteria.")
# #     else:
# #         print("Invalid airline selection.")
# airline_requirements = {
#     "Air Peace": [160, 25],
#     "Arik Air": [165, 23],
#     "Dana Air": [158, 22],
#     "Emirates": [170, 21],
#     "Qatar Airways": [168, 21]
# }
# ava_airline = enumerate(airline_requirements.keys(), start=1)
# print("Welcome to Air Hostess Eligibility Checker")
# print("Available Airlines:")
# for i, airline in ava_airline:
#     print(f"{i}. {airline}")



#     # User selects airline
#     choice = int(input("\nSelect an airline (enter number): "))
#     airline_list = list(airline_requirements.keys())
#     if 1 <= choice <= len(airline_list):
#         selected_airline = airline_list[choice - 1]
#         min_height, min_age = airline_requirements[selected_airline]
#         avg_height = 155
#         avg_age = 21
#         print(f"\nYou selected: {selected_airline}")
#         print(f"Average Requirements → Min Height: {avg_height}cm, Min Age: {avg_age} years\nPlease note this requirement may differ across airlines.")
#         # User enters details
#         user_height = float(input("Enter your height (in cm): "))# user"s height
#         user_age = int(input("Enter your age: "))# user's age
#          # Check conditions
#         if user_age >= min_age and user_height >= min_height:
#             print(f"Congratulations! You are eligible for {selected_airline}. Proceed to the next stage.")
#         elif user_age < min_age:
#             print(f"Sorry, you are too young for {selected_airline}.\n Minimum age is {min_age}.You can try other availble Airline")
#         elif user_height < min_height:
#             print(f"Sorry, you do not meet the minimum height requirement for {selected_airline}.\nMinimum height is {min_height}You can try other availble Airline")
#         else:
#             print("You do not meet the eligibility criteria.")
#     else:
#         print("Invalid airline selection.")
