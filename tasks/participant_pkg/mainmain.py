# TEE AND TEE WORK SHOP
while True:
    print("\nWelcome to learning AI 101:")
    print("1. Register")
    print("2. Registration Slip")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        try:
            name = (input("Enter your name: ")) # collects user name
            age = int(input("Enter your age: "))
            phone = input("Enter Phone Num: ")
            track = input("Enter Track: ")
            if name.isalpha() == False:
                raise ValueError("Invalid Input, Enter a name.")
            # collects user age
            # elif len(phone) != 11:
            #     raise ValueError("Enter Valid Number")
            # elif track.isalpha() == False:
            #     raise ValueError("Track cannot be empty")
        except ValueError as e:
           print("Error: ", e)