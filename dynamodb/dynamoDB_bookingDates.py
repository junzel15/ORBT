import boto3


def dynamo_read_all(table_name, region_name="us-east-1"):
    dynamodb = boto3.resource("dynamodb", region_name=region_name)
    table = dynamodb.Table(table_name)

    scan_kwargs = {}
    items = []

    while True:
        response = table.scan(**scan_kwargs)
        items.extend(response.get("Items", []))
        if "LastEvaluatedKey" in response:
            scan_kwargs["ExclusiveStartKey"] = response["LastEvaluatedKey"]
        else:
            break

    return items


if __name__ == "__main__":
    TABLE_NAME = "bookingDates"
    region = "us-east-1"
    all_items = dynamo_read_all(TABLE_NAME, region)

    for item in all_items:
        print(item)
