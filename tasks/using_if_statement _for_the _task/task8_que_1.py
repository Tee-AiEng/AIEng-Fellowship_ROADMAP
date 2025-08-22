# it can be use to check eligibilty for air hostess job

# code line for second use case
normal_height = 160 # cut-off height
age = 25 # cut-off age
user_height = int(input('Enter your height: ')) # user"s height
user_age = int(input("Enter age: ")) # user's age
# the if statement below ensures that the user"s age and height meet the requirment and prompt them to next age.
if user_age >= age :
    if user_age >= normal_height:
        print("User can proceed to the next stage")
    else:
        print("Sorry you aren't eligble but you can try again next time")
else:
    print("Ouch too young, but you can try again next year.")