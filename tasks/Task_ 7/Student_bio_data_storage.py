name = input("Enter your name: ") # collects user input
age = input("Enter your age: ") # collects user input
gender = input("Enter your gender: ") # collects user input
courses = input("Enter your courses separated by comma here: ")

student_bio = {}
student_bio["Student Name"] = name
student_bio["Age"] = age
student_bio["Gender"] = gender
student_bio["Courses"] = courses.split(",")
courses_fmt = ",".join(student_bio["Courses"])

print(f"Name: {student_bio["Student Name"]}\nAge: {student_bio["Age"]}\nGender: {student_bio["Gender"]}\nCourses: {courses_fmt}")