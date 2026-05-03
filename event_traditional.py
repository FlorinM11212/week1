class Event:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.bookings = []

    def book(self, person):
        if len(self.bookings) >= self.capacity:
            return "Event full"
        if person in self.bookings:
            return "Already booked"
        self.bookings.append(person)
        return "Booked"

    def cancel(self, person):
        if person in self.bookings:
            self.bookings.remove(person)
            return "Cancelled"
        return "Booking not found"

    def count(self):
        return len(self.bookings)


if __name__ == "__main__":
    event = Event("Python Workshop", 3)
    print(event.book("Amina"))
    print(event.book("John"))
    print(event.book("Sara"))
    print(event.book("Ali"))
    print(event.cancel("John"))
    print(event.cancel("David"))
    print(event.count())
