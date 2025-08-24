while True:
    print("\n UNILAG Portal")
    print("1. Check Jamb Cut-off")
    print("2. Check Admission Status")
    print("3. Exit")
    choice = input("Enter option: ")
    if choice == "1":
        jamb_score = int(input("Enter your jamb score: "))
        if jamb_score >= 200:
            print("You have meet the cut-off mark, Proceed to check your Admission Status")
        else:
            print("You didn't not meet the cut-off mark.")
    elif choice == "2":
        name = input("Enter full name: ").title()
        age = int(input("Enter your age: "))
        jamb_score = int(input("Enter your jamb score: "))
        print("Please note write university name in full not acronym")
        university_choice = input("Enter first university of choice: ").upper()
        print("Did you participate in the Post-Utme online screening?\n1. Yes\n2. No")
        Utme_screening = input("Enter option: ") 
        Post_Utme = int(input("Enter your Post_Utme score: "))
        O_level_requirement = input("Enter 5 relvant subjects separated by comma including Mathematics and English: ").title().split(",")
        score_dict ={
            "A":15,
            "B":12,
            "C":9,
            "D":6,
            "E":3,
            "F":0
            }
        print(score_dict)
        O_level_score = int(input("Enter O'level score calculated base on the dict printed above: "))
        department = input("Enter Department: ")
        dept_cut_off = (jamb_score + Post_Utme)/2

        if (age >= 16) and (jamb_score >= 200) and ( university_choice == "UNIVERSITY OF LAGOS") and ( Utme_screening == "1") and ("Mathematics" in O_level_requirement) and ("English" in O_level_requirement) and (O_level_score >= 45) and (dept_cut_off >= 200):
            print(f"Congratulations,{name} has been offered tentative admission to the Department of {department}.\nClick on the link below to scan your original documents to confirm Admission.\n\"www.scan_documents.com\"\nRequirded Documents:\n1. Birth Certificate\n2. Original Jamb Result\n3. Jamb Registration Slip\n4. Original Waec or Neco Result(not both)\n5. Post-Utme Registration Slip and  Post-Utme Screening Result(can be printed on the Post-Utme portal)")
        else:
            print("Sorry, You do not qualify for Admission you can try again Next Year. Thank you")
    elif choice == "3":
        print("Are you sure you want to exit?\n1. Yes\n2. No")
        option = input("Enter option: ")
        if option  == "1":
            print("Thank you!")
            break
        else:
            pass




