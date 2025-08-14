# task 2
bfs = [] # empty list
best_frind = input("Enter 5 best friends name: ") # coolects input
best_frind1 = input("Enter 5 best friends name: ")# coolects input
best_frind2 = input("Enter 5 best friends name: ")# coolects input
best_frind3 = input("Enter 5 best friends name: ")# coolects input
best_frind4 = input("Enter 5 best friends name: ")# coolects input
bfs.append(best_frind) # adds to thr empty list
bfs.append(best_frind1) # adds to thr empty list
bfs.append(best_frind2) # adds to thr empty list
bfs.append(best_frind3) # adds to thr empty list
bfs.append(best_frind4) # adds to thr empty list
friends = tuple(bfs)# converts to tuple
print(friends[::-1]) # reverse the tuple