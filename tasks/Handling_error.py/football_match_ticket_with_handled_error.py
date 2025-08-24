# Seat booking system

number = range(1, 51)          # generate numbers from 1 to 50
set_number = set(number)       # available seats
# prints a welcome message
# prints the seat available befoer any booking
print("Welcome to Seat Booking System")
print("Seats available: 1 - 50")

while True:
    try:
        book_seat = int(input("\nEnter seat number to book (or 0 to exit): ")) # collects input(numbers ranging from 1 to 50 for seat booking or 0 to exit )

        if book_seat == 0:
            print("Thank you for using the booking system. Goodbye!")
            break

        if book_seat in set_number:
            set_number.remove(book_seat)
            print(f"You have successfully booked seat number {book_seat}")
            print(f"Remaining seats: {len(set_number)}")
        else:
            print("Seat number not available. Try another one.")
    except ValueError:
        print("Invalid input! Please enter a valid seat number.")
