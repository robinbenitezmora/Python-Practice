import datetime

class Room:
    def __init__(self, number, price, capacity):
        self.number = number
        self.price = price
        self.capacity = capacity
        self.is_booked = False

    def is_available(self):
        return not self.is_booked
    
class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Booking:
    def __init__(self, room, customer, date):
        self.room = room
        self.customer = customer
        self.date = date
        room.is_booked = True

class HotelManagementSystem:
    def __init__(self):
        self.rooms = []
        self.customers = []
        self.bookings = []

    def add_room(self, number, price, capacity):
        room = Room(number, price, capacity)
        self.rooms.append(room)

    def add_customer(self, name, email, phone):
        customer = Customer(name, email, phone)
        self.customers.append(customer)

    def book_room(self, room_number, customer_name, date):
        for room in self.rooms:
            if room.number == room_number and room.is_available():
                for customer in self.customers:
                    if customer.name == customer_name:
                        booking = Booking(room, customer, date)
                        self.bookings.append(booking)
                        return f"Room {room_number} is booked by {customer_name}"
        return "Room is not available"
    
    def get_available_rooms(self):
        return [room for room in self.rooms if room.is_available()]
    
    def get_bookings(self):
        return [(booking.room.number, booking.customer.name, booking.date) for booking in self.bookings]
    
    def get_customer_bookings(self, customer_name):
        return [(booking.room.number, booking.date) for booking in self.bookings if booking.customer.name == customer_name]
    
    def get_room_bookings(self, room_number):
        return [(booking.customer.name, booking.date) for booking in self.bookings if booking.room.number == room_number]
    
    def get_total_revenue(self):
        return sum([booking.room.price for booking in self.bookings])
    
    def get_revenue_by_date(self, date):
        return sum([booking.room.price for booking in self.bookings if booking.date == date])
    
    def get_revenue_by_month(self, month):
        return sum([booking.room.price for booking in self.bookings if booking.date.month == month])
    
    def get_revenue_by_year(self, year):
        return sum([booking.room.price for booking in self.bookings if booking.date.year == year])
    
    def get_revenue_by_customer(self, customer_name):
        return sum([booking.room.price for booking in self.bookings if booking.customer.name == customer_name])
    
    def get_revenue_by_room(self, room_number):
        return sum([booking.room.price for booking in self.bookings if booking.room.number == room_number])
    
    def get_revenue_by_room_type(self, room_type):
        return sum([booking.room.price for booking in self.bookings if booking.room.capacity == room_type])
    
    def get_revenue_by_room_capacity(self, room_capacity):
        return sum([booking.room.price for booking in self.bookings if booking.room.capacity == room_capacity])
    
    def get_revenue_by_room_availability(self, is_available):
        return sum([booking.room.price for booking in self.bookings if booking.room.is_available() == is_available])
    
    def get_revenue_by_room_bookings(self, room_number):
        return sum([booking.room.price for booking in self.bookings if booking.room.number == room_number])
    
    def get_revenue_by_customer_bookings(self, customer_name):
        return sum([booking.room.price for booking in self.bookings if booking.customer.name == customer_name])
    
    def get_revenue_by_date_bookings(self, date):
        return sum([booking.room.price for booking in self.bookings if booking.date == date])
    
    def get_revenue_by_month_bookings(self, month):
        return sum([booking.room.price for booking in self.bookings if booking.date.month == month])
    
    def get_revenue_by_year_bookings(self, year):
        return sum([booking.room.price for booking in self.bookings if booking.date.year == year])
    

hms = HotelManagementSystem()
hms.add_room(101, 100, 2)
hms.add_room(102, 200, 4)
hms.add_room(103, 300, 6)
hms.add_room(104, 400, 8)
hms.add_customer('Alice', 'Peter', '1234567890')
hms.add_customer('Bob', 'John', '0987654321')
hms.add_customer('Charlie', 'Doe', '6789012345')
hms.add_customer('David', 'Smith', '4567890123')
print(hms.get_available_rooms())
print(hms.book_room(101, 'Alice', datetime.date(2021, 1, 1)))
print(hms.book_room(102, 'Bob', datetime.date(2021, 2, 2)))
print(hms.book_room(103, 'Charlie', datetime.date(2021, 3, 3)))
print(hms.book_room(104, 'David', datetime.date(2021, 4, 4))
print(hms.get_available_rooms())
print(hms.get_bookings())
print(hms.get_customer_bookings('Alice'))
print(hms.get_room_bookings(101))
print(hms.get_total_revenue())
print(hms.get_revenue_by_date(datetime.date(2021, 1, 1)))
print(hms.get_revenue_by_month(1))
print(hms.get_revenue_by_year(2021))
print(hms.get_revenue_by_customer('Alice'))
print(hms.get_revenue_by_room(101))
