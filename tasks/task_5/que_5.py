# task 5
item1 = input("Enter item: ")# coolects input
item2 = input("Enter item: ")# coolects input
item3 = input("Enter item: ")# coolects input
shoping_list = (item1,item2,item3)# stores the inputs in a tuple
shoping_list_lst = list(shoping_list)# converts to list
item4 = input("Enter item: ")# coolects input
item5 = input("Enter item: ")# coolects input
shoping_list_lst.append(item4)# adds to a list
shoping_list_lst.append(item5)# adds to a list
update_list = tuple(shoping_list_lst)# converts a list to tuple
print("|".join(update_list)) #joins the tuple with a |