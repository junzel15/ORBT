import boto3
import json

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table("bookings")


def debug_scan_full():
    last_evaluated_key = None
    all_items = []

    while True:
        scan_kwargs = {}
        if last_evaluated_key:
            scan_kwargs["ExclusiveStartKey"] = last_evaluated_key

        response = table.scan(**scan_kwargs)
        items = response.get("Items", [])

        if items:
            all_items.extend(items)
        else:
            print("No items found in bookings.")
            return

        last_evaluated_key = response.get("LastEvaluatedKey")
        if not last_evaluated_key:
            break

    print(json.dumps(all_items, indent=2))


debug_scan_full()
