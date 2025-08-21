Ussd = input("Dial code (*297#): ")
while True:
    print("\nWelcome to Tee communications, thanks for using our services")
    print("MainMenu:")
    print("1.Check Balance")
    print("2.Buy ")
    print("3.Borrow")
    print("4.Share")
    print("5.Exit")
    choice = input("Enter option: ")
    if choice == "1":
        print("\n Option")
        print("1. Airtime")
        print("2. Data")
        option = input("Enter your option: ")
        if option == "1":
            balance_airtime = 3000.45
            print(f"Your balance is: {balance_airtime}.Thank you for using our services\nPress 5 to exit")
        elif option == "2":
             balance_data = "2048gb"
             print(f"Your balance is: {balance_data}.Thank you for using our services\nPress 5 to exit")
        else:
            print("Select a new option on the mainmenu.")
    elif choice == "2":
        print("\nOptions")
        print("1. Airtime")
        print("2. Data")
        opt = input("Enter your option: ")
        if opt == "1":
            print("1.Buy for self")
            print("2.Buy for others")
            opt = input("Enter your option: ")
            if opt == "1":
                amount = input("Enter amount: ")
                print("Are you sure?\n1.\tYes\n2.\tNo")
                optin = input("Enter your option: ")
                if optin == "1":
                    print(f"Your line has been credited with {amount}. Thank you for using our services\nPress 5 to exit")
                else:
                    print("Select a new option on the mainmenu.")
            elif opt == "2":
                number = input("Enter the number: ")
                print(f"Are you sure of {number}?\nPress 1 to proceed")
                proceed = input("Enter 1 to procced:")
                if proceed == "1":
                    amnt = input("Enter amount: ")
                    print(f"The {number} has been credited with {amnt}. Thank you for using our services\nPress 5 to exit")
                else:
                    print("Select a new option on the mainmenu.")
            else:
                print("Select a new option on the mainmenu.")
        elif opt == "2":
            print("1.Buy for self")
            print("2.Buy for others")
            opt = input("Enter your option: ")
            if opt == "1":
                print("\nData Menu")
                print("1. #400 - 1gb")
                print("2. #700 - 2gb")
                print("3. #1500 - 5gb")
                print("4. #3500 - 12gb")
                print("5. #5000 - 17gb")
                amount = input("Enter amount in gb: ")
                print("Are you sure?\n1.\tYes\n2.\tNo")
                optin = input("Enter your option: ")
                if optin == "1":
                     print(f"Your line has been credited with {amount}. Thank you for using our services\nPress 5 to exit")
                else:
                    print("Select a new option on the mainmenu.")
            elif opt == "2":
                number = input("Enter the number: ")
                print(f"Are you sure of {number}?\nPress 1 to proceed")
                proceed = input("Enter 1 to procced:")
                if proceed == "1":
                    print("\nData Menu")
                    print("1. #400 - 1gb")
                    print("2. #700 - 2gb")
                    print("3. #1500 - 5gb")
                    print("4. #3500 - 12gb")
                    print("5. #5000 - 17gb")
                    amnt = input("Enter amount in gb: ")
                    print(f"The {number} has been credited with {amnt}. Thank you for using our services\nPress 5")
                else:
                    print("Select a new option on the mainmenu.")
            else:
                print("Select a new option on the mainmenu.")
    elif choice == "3":
        print("\n Option")
        print("1. Airtime")
        print("2. Data")
        opt = input("Enter your option: ")
        if opt == "1":
            print("1.Borrow for self")
            print("2.Borrow for others")
            opt = input("Enter your option: ")
            if opt == "1":
                amount = input("Enter amount: ")
                print("Are you sure?\n1.\tYes\n2.\tNo")
                optin = input("Enter your option: ")
                if optin == "1":
                    print(f"Your line has been credited with {amount}. Thank you for using our services\nPress 5 to exit")
                else:
                    print("Select a new option on the mainmenu.")
            elif opt == "2":
                number = input("Enter the number: ")
                print(f"Are you sure of {number}?\nPress 1 to proceed")
                proceed = input("Enter 1 to procced:")
                if proceed == "1":
                    amnt = input("Enter amount: ")
                    print(f"The {number} has been credited with {amnt}. Thank you for using our services\nPress 5 to exit")
                else:
                    print("Select a new option on the mainmenu.")
            else:
                print("Select a new option on the mainmenu.")

        

            

                



