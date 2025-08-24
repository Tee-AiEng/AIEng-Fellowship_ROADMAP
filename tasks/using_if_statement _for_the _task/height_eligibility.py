#  it can be use to check eligibilty for air hostess job
normal_height = 160 # cut-off height
age = 25
user_height = int(input('Enter your height: ')) # user"s
user_age = int(input("Enter your age: "))
if (user_height >= normal_height) and (user_age >= age):
    print(f"User is eligible you can procced to next stage")
else:
    print(f"User is not eligible.")


