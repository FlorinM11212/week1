class Event:
    def __init__(self):
        self.bookings = []
        self.capacity = 3

    def book(self, person):
        if person in self.bookings:
            return "Already booked"
        if len(self.bookings) >= self.capacity:
            return "Event full"
        self.bookings.append(person)
        return "Booked"

    def cancel(self, person):
        if person in self.bookings:
            self.bookings.remove(person)
            return "Cancelled"
        return "Booking not found"

    def count(self):
        return len(self.bookings)
