number = range(1,51) # genrate number from 1 to 50 to serve as seat numbers
set_number = set(number) # to ensure there is no duplicate number
book_seat = int(input("Enter seat number: "))
        
if book_seat in set_number:
    set_number.remove(book_seat)
    print("You have succesfully book a seat number")
    print(set_number)
else:
    print("Seat Number not available.")
   