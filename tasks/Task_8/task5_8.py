store = {"Book": 10, "Pen": 20, "Bag": 10} # key-item, value-quantity
item = input("Enter item: ") 
quantity = int(input("Enter quantity: "))
print("Before purchase: ", store)
store[item] -= quantity
print("After purchase: ", store)