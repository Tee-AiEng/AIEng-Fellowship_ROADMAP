print("\nPatient Profile Builder")
# basic info
name = input("Enter Patient's full name: ")
age = int(input("Enter patient's age: "))
gender = input("Enter gender (Male/Female): ")
marital_status =input("Enter gender (single/married): ")
#Medical info
M_info = ("Height","Weight","Blood Group","Genotype")
height = float(input("Enter patient's height (in meters): "))
weight = float(input("Enter patient's weight (in kg): "))
blood_group = input("Enter patient's blood group (e.g., A+, O-, B+): ")
geno_type = input("Enter patient's blood group (e.g., AA, AS, SS, SC): ")
M_value = (height,weight,blood_group,geno_type)
# Next of kin info
next_of_kin_name = input("Enter Next of kin's name: ")
next_of_kin_phn_num = input("Enter Next of kin's phone number: ")
# Allergies / Conditions
allergies_input = input("Enter allergies/medical conditions (comma-separated, at least 2)\nIf none for both write none twice: ")
allergies_set = set(a.strip().title() for a in allergies_input.split(","))

# Patient Dictionary
patient_profile = {
    "Basic Info": {
        "Name": name.title(),
        "Age": age,
        "Gender": gender.capitalize(),
        "Marital Staus": marital_status.capitalize()
    },
    "Medical Info": {info: val for info, val in zip(M_info, M_value)},
    "Next of Kin": {
        "Name": next_of_kin_name,
        "Phone number": next_of_kin_phn_num
    },
    "Allergies / Conditions": list(allergies_set)

}

# Derived Data
patient_profile["Medical Info"]["BMI"] = weight / (height ** 2)
patient_profile["Basic Info"]["Initials"] = ".".join([n[0] for n in name.split()])
patient_profile["Allergies Count"] = len(allergies_set)

# Output Section
print("\n\t=== Patient PROFILE ===")
print(f"Name:\t\t{patient_profile['Basic Info']['Name']}")
print(f"Age:\t\t{patient_profile['Basic Info']['Age']}")
print(f"Gender:\t\t{patient_profile['Basic Info']['Gender']}")
print(f"Marital Status:\t{patient_profile['Basic Info']['Marital Staus']}")
print(f"Initials:\t{patient_profile['Basic Info']['Initials']}")
print("\n--- Medical Info ---")
print(patient_profile["Medical Info"])
print("\n---  Next of Kin Info ---")
print(patient_profile["Next of Kin"])
print("\n--- Allergies / Conditions ---")
print(patient_profile["Allergies / Conditions"])
print(f"\nTotal Allergies / Conditions:\t{patient_profile['Allergies Count']}")
print(f"BMI Score:\t{patient_profile['Medical Info']['BMI'] :.2f}")