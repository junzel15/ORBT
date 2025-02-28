import boto3

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table("bookingDates")


def fix_incorrect_key():
    response = table.scan()
    items = response.get("Items", [])

    with table.batch_writer() as batch:
        for item in items:
            updated = False

            if "dates" in item and isinstance(item["dates"], list):
                for date_entry in item["dates"]:
                    if isinstance(date_entry, list):
                        for i, value in enumerate(date_entry):
                            if isinstance(value, str) and "sselect_a_time" in value:
                                date_entry[i] = value.replace(
                                    "sselect_a_time", "select_a_time"
                                )
                                updated = True

            if updated:
                batch.put_item(Item=item)

    print(f"Updated {len(items)} records successfully.")


fix_incorrect_key()
