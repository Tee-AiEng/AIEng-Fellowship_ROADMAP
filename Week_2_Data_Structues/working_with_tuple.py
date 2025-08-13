fruits = ("apple","banana","cherry")
print(fruits)

number = 1,2,3,4
print(number)

single_item = ("apple",)
print(single_item)
print(type(single_item))

fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

colors = ("red","green","blue")
print(colors[0])

numbers = (1, 2, 2, 3)
print(numbers)

mixed = ("apple", 3, True, 5.6)
print(mixed)

nested = (("a", "b"), (1, 2))
print(nested)

fruits_1 = ("apple","banana","cherry","pineapple")
print(fruits[1])
print(fruits_1[-1])
print(fruits_1[0:2])
print(fruits_1[::-1])


tuple1 = (1,2)
tuple2 =(3,4)
result = tuple1 + tuple2
print(result)

num = (1,2)
print(num * 3)

fruits_2 = ("apple", "banana", "cherry")
print("banana" in fruits_2)
print("grape" not in fruits_2)

for fruit in fruits_2:
    print(fruit)

person = ("John", 25, "Nigeria")
name, age, country = person
print(name)
print(age)
print(country)


nums = (1,2,3,4)
print(nums.count(2))
print(nums.index(3))

t = (1,2,3)
lst = list(t)
lst.append(4)
print(lst)


t = tuple(lst)
print(t)

numbs = (4, 1, 7, 3)
print(len(numbs))
print(max(numbs))
print(min(numbs))
print(sum(numbs))