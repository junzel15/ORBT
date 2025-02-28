import boto3
import json

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")


table = dynamodb.Table("bookings")


def debug_scan_full():
    last_evaluated_key = None

    while True:

        if last_evaluated_key:
            response = table.scan(ExclusiveStartKey=last_evaluated_key)
        else:
            response = table.scan()

        items = response.get("Items", [])
        if not items:
            print("No items found in bookingDates.")
            return

        for item in items:
            print(json.dumps(item, indent=2))

        last_evaluated_key = response.get("LastEvaluatedKey")
        if not last_evaluated_key:
            break


debug_scan_full()
