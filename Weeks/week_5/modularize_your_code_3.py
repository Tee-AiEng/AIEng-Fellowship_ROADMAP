# class Student:
#     def __init__(self,name,course,level):
#         print("Creating a new student...")
#         self.name = name
#         self.course = course
#         self.level = level
#         print(f"Student {name} has been created")

# kemi = Student("Kemi Adebayo", "Computer Science", 300)


# class NigerianStudent:
#     def __init__(self,name,state, course):
#         print(f"Step 1: Creating student object...")
#         self.name = name
#         self.state_of_origin = state
#         self.course = course
#         self.student_id = self.generate_id()
#         print(f"Step 6: {self.name} from {self.state_of_origin} is ready!")

#     def generate_id(self):
#         import random
#         return f"UNISAIL{random.randint(1000, 9999)}"
    
# ayo = NigerianStudent("Ayo Daniel","Lagos","Street Statistics")

# print(ayo.name)
# print(ayo.student_id)


# class PhoneUser:
#     def __init__(self, name, network):
#         self.name = name
#         self.network = network
#         self.airtime = 0
#         print(f"{self.name} joined {self.network} network")

#     def buy_airtime(self, amount):
#         self.airtime += amount
#         return f"{self.name} now has ₦{self.airtime} airtime"
    

# abeeb = PhoneUser("Abeeb Bakare","MTN")
# onisemo = PhoneUser("Onisemo Williams", "Airtel") 

# print(abeeb.buy_airtime(500))   
# print(onisemo.buy_airtime(1000)) 
# print(abeeb.airtime)             
# print(onisemo.airtime) 


# from datetime import datetime

# date = datetime.today().strftime("%Y-%m-%d")
# print(date)

# date_1 = datetime(2025, 8, 8)
# date_1
# for_date = date_1.strftime("%m-%d-%Y")
# print(for_date)


# class Student:
#     def __init__(self,name, course,level, state_of_origin):
#         self.name = name
#         self.course = course
#         self.level = level
#         self.state_origin = state_of_origin
#         self.cgpa = 0.0

# Fathia = Student("Fathia Abdul", "Biochemistry", 300, "Ogun State")

# print(Fathia.name)
# print(Fathia.course)
# print(Fathia.state_origin)
# print(Fathia.cgpa)


# student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
# student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")

# print(student1.name)  
# print(student2.name) 



# class Student:
#     university = "Federal University of Technology Akure"

#     def __init__(self,name,course):
#         self.name = name
#         self.course = course

# print(Student.university)     
# # print(student1.university)   
# # print(student2.university)   


# class Student_1:
#     def __init__(self, name, course, level):
#         #Attributtes
#         self.name = name
#         self.course = course
#         self.level = level
#         self.cgpa = 0.0
#         self.fees_paid = False

#     #Method: action the student can do
#     def pay_school_fees(self):
#         self.fees_paid = True
#         return f"{self.name} has paid school fees for {self.level} level"
#     def register_courses(self):
#         if self.fees_paid:
#             return f"{self.name} has registered courses for {self.course}"
#         else:
#             return f"{self.name} must pay school fees first!"
        
#      # Method: calculates CGPA
#     def calculate_cgpa(self, grades):           
#         if grades:
#             self.cgpa = sum(grades) / len(grades)
#             return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
#         return "No grades provided"
# Abiodun = Student_1("Abiodun Akinola","Gistology",600)
# print(Abiodun.pay_school_fees())
# print(Abiodun.register_courses())
# print(Abiodun.calculate_cgpa([4.2,3.8,4.0,3.5]))

# Defining Attributes of a student
class Student:
    def __init__(self, name, course, level, state_of_origin,):
        self.name = name                   
        self.course = course              
        self.level = level                
        self.state_of_origin = state_of_origin  
        self.cgpa = 0.0      
    
    def cal_gp(self, gp):
        self.cgpa += gp  # self ensures it goes to the RIGHT person
        return f"{self.name} now has {self.cgpa} gpa"
    

cunyie = Student("Kayinsoal Fagbayi", "radiology", 100, "lagos")
print(cunyie.cal_gp(4.5))