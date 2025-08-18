student ={}
name = input("Enter name: ")
age = input("Enter age: ")
student["Name"] = name
student["Age"] = age
scores = [70,85,95]
student["Score"] = scores
average = sum(scores)/len(scores)
student["Passed"] = average >=50
student["Teenage"] = (age > 13) and (age < 19)
print(f"Student Record\nName: {student["Name"]}\nAge: {student["Age"]}\nScores :{student["Score"]}\nPasseed: {student["Passed"]}\nTeenage: {student["Teenage"]}")
