# TEE AND TEE WORK SHOP
while True:
    print("\nWelcome to learning AI 101:")
    print("1. Register")
    print("2. Registration Slip")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        # collect user details
        
        name = str(input("Enter your name: ")) # collects user name
        if not name.isalpha():
            print("Name should only contain letters.")

        try:
            age = int(input("Enter your age: ")) # collects user age
        except ValueError:
            print("Age must be a number!")
        phone = input("Enter Phone Num: ")
        if len(phone) != 11:
            print("Enter a correct number")
        else:
            pass
        print("List of Track:\n1. AI Engineer\n2. AI Developer\n3. Data Science\n4. CyberSecurity\n5. Project Development")
        track = input("Enter Track: ")
        if track != "":
            pass
        else:
            print("Track cannot be empty")

    # put the user info in a dictiobary

        Contact_info = {}
        Contact_info["Student Name"] = name
        Contact_info["Age"] = age
        Contact_info["Phone Number"] = phone
        Contact_info["Track"] = track

        Contact_info.update()
    elif choice == "2":
        



    
    



