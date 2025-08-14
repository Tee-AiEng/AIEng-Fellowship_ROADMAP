# task 3 A football match ticket system
number = range(1,51)
set_number = set(number)
print(set_number)
book_seat = int(input("Enter seat number: "))
set_number.remove(book_seat)
print(set_number)
