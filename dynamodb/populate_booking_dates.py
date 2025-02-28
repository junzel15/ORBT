from dynamodb.dynamoDB_bookings import dynamo_write

data_to_insert = {
    "dinning": {
        "JANUARY 01, 2025": "08:00 AM",
        "JANUARY 02, 2025": "09:00 AM",
        "JANUARY 03, 2025": "10:00 AM",
        "JANUARY 04, 2025": "11:00 AM",
        "JANUARY 05, 2025": "12:00 PM",
    },
    "bar": {
        "JANUARY 01, 2025": "08:00 AM",
        "JANUARY 02, 2025": "09:00 AM",
        "JANUARY 03, 2025": "10:00 AM",
        "JANUARY 04, 2025": "11:00 AM",
        "JANUARY 05, 2025": "12:00 PM",
    },
    "experiences": {
        "JANUARY 01, 2025": "08:00 AM",
        "JANUARY 02, 2025": "09:00 AM",
        "JANUARY 03, 2025": "10:00 AM",
        "JANUARY 04, 2025": "11:00 AM",
        "JANUARY 05, 2025": "12:00 PM",
    },
}

for category, dates in data_to_insert.items():
    for date, time_info in dates.items():
        item = {
            "id": category,
            "select_a_date": date,
            "select_a_time": time_info,
        }
        response = dynamo_write("bookingDates", item)
