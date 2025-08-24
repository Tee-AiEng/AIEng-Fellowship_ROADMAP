# NIGERIAN CURRENCY CONVERTER
# COLLECT USERS INPUT
while True:
    print("\nConversion Services:")
    print("1. Convert from Naira to other currency")
    print("2. Check Echange rate")
    print("3. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        print("\nAvailable Currency:")
        print("1. Dollars")
        print("2. Pounds")
        option = input("Enter choice: ")
        if option == "1":
            try:
                amount = float(input("Enter amount in naira: "))
                exch_rate_dollar = 1550
                amount_in_dollars = amount/exch_rate_dollar 
                print(f"Amount in dollars: ${amount_in_dollars}")
            except ValueError:
                print("Invalid amount! Please enter a number.")
        elif option == "2":
            try:
                amount = float(input("Enter amount in naira: "))
                exch_rate_pounds = 1950
                amount_in_pounds = amount/exch_rate_pounds
                print(f"Anount in Pounds: {amount_in_pounds}")
            except ValueError:
                print("Invalid amount! Please enter a number.")
        else:
            print("Invalid input!!!")
    elif choice == "2":
        print("\n Exchange Rate Menu:")
        exch_rate_dollar = 1550
        exch_rate_pounds = 1950
        print(f"1 dollars = {exch_rate_dollar}")
        print(f"1 pounds = {exch_rate_pounds}")
    elif choice == "3":
        print("Thank you for using our Services.Goodbye!")
        break
    else:
        print("Invalid option. Try again.")