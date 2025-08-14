# task 3
states = [] # empty list
state1 = input("Enter state: ")# coolects input
state2 = input("Enter state: ")# coolects input
state3 = input("Enter state: ")# coolects input
state4 = input("Enter state: ")# coolects input
state5 = input("Enter state: ")# coolects input
states.append(state1)# adds to thr empty list
states.append(state2)# adds to thr empty list
states.append(state3)# adds to thr empty list
states.append(state4)# adds to thr empty list
states.append(state5)# adds to thr empty list
states_tuple = tuple(states)# converts to tuple
print(states_tuple[0])# prints the first value in the tuple
print(states_tuple[-1])# prints the last value in the tuple
print("lagos" in states_tuple) # checks if lagos is in the tuple
print("lagos" not in states_tuple)# checks if lagos is not in the tuple
print(len(states_tuple)) # prints the length of the tuple
