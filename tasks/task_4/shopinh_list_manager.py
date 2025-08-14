# task_2
items = [] # empty list
itm_1 = input("Enter item: ") # collects input
itm_2 = input("Enter item: ") # collects input
itm_3 = input("Enter item: ") # collects input
items.append(itm_1) # add to the empty list
items.append(itm_2) # add to the empty list
items.append(itm_3) # add to the empty list
res = (",".join(items)) # joins the list 
print(str(res)) # convert to string