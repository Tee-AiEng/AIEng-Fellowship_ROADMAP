empty_list = [] # empty list
print(empty_list)

empty_list2 = list() # empty list
print(empty_list2)

numbers = [1,2,3,4,5] # list of intergers
print(numbers)

fruits = ["apple","banana","cherry"] # list of strings
print(fruits)

mixed_list =["Alice",24, 5.6, True] # a lsit with different data type
print(mixed_list)
charc = list("hello") # list from another sequence
print(charc)

my_tuple = (10,20,30,40,50) # list from a tuple
list_from_tuple = list(my_tuple)
print(list_from_tuple) 
numbers_range = list(range(5))
print(numbers_range) # list from range
squares = [x**2 for x in range(5)] # list comprenhensions
print(squares)

even = [x for x in range(11) if x % 2 == 0] # list comprenhensions with an if statement
print(even)

# nesting a list in a list gives a matrix-like list
matrix = [[1,2],[2,4],[4,6],[6,8]]
# accesing elements ina neseted list, if you want the list in the neted list then you index it else you can sub-index it
print(matrix[0])
print(matrix[0][1])

fruits_1 = ["mango","orange","apple","banana","cherry"]
print(fruits_1)
print(fruits_1[0])
print(fruits_1[2])
print(fruits_1[1])
print(fruits_1[3])

items = ["rice","beans","yam","rice"]
print(items)
numbers_1 = [1,2,3,4,5,6,7] 
numbers_1[2] = 20
print(numbers_1)

mixed =["Alice",24, 5.6, True,"Nigeria"]
print(mixed)

nested_list = [[1, 2], ["a", "b"]]
print(nested_list)   
print(nested_list[1][1]) 

names = ["Ada"]
names.append("Bola")
names.append("Ade")
print(names) 