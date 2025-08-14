# collecting votters names
voters = set() # emptry set
v_name = input("Enter name: ") # collects votters name
voters.add(v_name) # adds to the empty set
v_name_1 = input("Enter name: ") # collects votters name
voters.add(v_name_1) # adds to the empty set
v_name_2 = input("Enter name: ")# collects votters name
voters.add(v_name_2) # adds to the empty set 
# creates a system that raise error when there is duplicates
if v_name_2 in voters:
    print(f"{v_name_2} has already being registered")
else: 
    print(f"{v_name_2} has being registered fully")

print(len(voters)) #print number of registered votters  
          

