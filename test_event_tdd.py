from event_tdd import Event


def test_booking_a_user():
    event = Event()
    result = event.book("Amina")
    assert result == "Booked"


def test_booking_count():
    event = Event()
    event.book("Amina")
    event.book("John")
    assert event.count() == 2


def test_event_full():
    event = Event()
    event.book("Amina")
    event.book("John")
    event.book("Sara")
    result = event.book("Ali")
    assert result == "Event full"


def test_duplicate_booking():
    event = Event()
    event.book("Amina")
    result = event.book("Amina")
    assert result == "Already booked"
    assert event.count() == 1


def test_cancel_booking():
    event = Event()
    event.book("Amina")
    result = event.cancel("Amina")
    assert result == "Cancelled"
    assert event.count() == 0


def test_cancel_invalid_booking():
    event = Event()
    result = event.cancel("David")
    assert result == "Booking not found"


if __name__ == "__main__":
    tests = [
        ("Test 1: Booking a user", test_booking_a_user),
        ("Test 2: Booking count", test_booking_count),
        ("Test 3: Event full", test_event_full),
        ("Test 4: Duplicate booking", test_duplicate_booking),
        ("Test 5: Cancel booking", test_cancel_booking),
        ("Test 6: Cancel invalid booking", test_cancel_invalid_booking),
    ]
    passed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"{name} -> PASS")
            passed += 1
        except AssertionError:
            print(f"{name} -> FAIL")
    print(f"\n{passed}/{len(tests)} tests passed")
