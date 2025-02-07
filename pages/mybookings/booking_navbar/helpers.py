def filter_bookings(bookings, filters):
    return [b for b in bookings if filters.get("example_filter", True)]
