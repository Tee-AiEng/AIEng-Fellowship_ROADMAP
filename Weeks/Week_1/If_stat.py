
T_T_code= int(input("Enter your code: "))
print("Welcome to Tee&Tee your one stop shop for your necessities\n1.Buy Frozen Foods\n2.Buy Raw Foods\n3.Buy Toiletries\n4.Pay Bills")
option = int(input("Enter option: "))
if option == 1:
    print("1.Fish\n2.Meat\n3.Chicken")
    opt = int(input("Enter option: "))
    print("1.PrePackaged\n2.Weighted")
    opt = int(input("Enter option: "))
    if opt == 1:
        print("1.Individual size(5000)\n2.Family size(7000)")
        opt = int(input("Enter option: "))
        dev_deat = input("Enter your deliver details:----------------------")
        print("make payment to the bank deatils below\nFBN(323456987)\nYour order is on the way\nThank you for your patronage\nHave a lovely day")
    else:
        weg = input("Enter weight in kg:3500 perkg")
        print("make payment to the bank deatils below\nFBN(323456987)\nYour order is on the way\nThank you for your patronage\nHave a lovely day")
elif option == 2:
    print("1.Rice\n2.Beans\n3.Garri")
    opt = int(input("Enter option: "))
    print("1.PrePackaged\n2.Weighted")
    opt = int(input("Enter option: "))
    if opt == 1:
        print("1.Individual size(5000)\n2.Family size(7000)")
        opt = int(input("Enter option: "))
        dev_deat = input("Enter your deliver details:----------------------")
        print("make payment to the bank deatils below\nFBN(323456987)\nYour order is on the way\nThank you for your patronage\nHave a lovely day")
    else:
        weg = input("Enter weight in kg:-------")
        print("make payment to the bank deatils below\nFBN(323456987)\nYour order is on the way\nThank you for your patronage\nHave a lovely day")

elif option == 3:
    needs = input("list your needs in market price:----------------")
    print("make payment to the bank deatils below\nFBN(323456987)\nYour order is on the way\nThank you for your patronage\nHave a lovely day")
    
elif option == 4:
    print("click the link below\nwww.t&t.website.com\nThank you for your patronage👍")
else:
    print("You have reached T&T, kindly redial your code")