# name = input("Enter your name: ") # collects the name of the users
# age = int(input("Enter your age: "))# collects the age of the users
# score = int(input("Enter your test score: ")) # collects the test score of the users
# # Must be younger than 18 AND score above 80
# eligibility = (age < 18) and (score > 70) 
# # Outpu: candidate's name, age, score, and eligibilty status
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

print("\nFederal Government Scholarship Key Eligibility Requirements:")
name = input("Enter name: ").lower()# collects the name of the users
nationality = input("Enter your nationality: ").lower()# collects the nationality of the users
employment_status = input("Enter employment status(undergrad/grad/employed): ").lower()# collects the employment status of the users
Scholar_enrolled = input("Are you enrolled in other schorlaship from an entity in the Oil and Gas industry: ").lower()# collects the onformation on schorlaship they are enrolled in
Academic_subject = input("Enter 5 subjects separated by comma: ")
academic_qualiafication = [input(f"Enter grade for {subject}: ") for subject in Academic_subject]
accepeted_grade = ("A" in academic_qualiafication) or ("B" in academic_qualiafication)

eligibility = (nationality == "nigerian") and (employment_status == "undergraduate") and (Scholar_enrolled == "no") and (accepeted_grade = True)


