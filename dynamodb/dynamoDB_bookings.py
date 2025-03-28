import boto3
from botocore.exceptions import ClientError


def dynamo_write(table_name, item):
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table(table_name)

    try:
        response = table.put_item(Item=item)
        print("Item successfully written to DynamoDB:", response)
    except Exception as e:
        print("Error writing to DynamoDB:", e)


def dynamo_read(table_name, primary_key, primary_value):
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table(table_name)

    key = {primary_key: primary_value}

    try:
        response = table.get_item(Key=key)
        item = response.get("Item")
        print(item)
        return item
    except ClientError as e:
        print("Error reading from DynamoDB:", e)
        return None


def dynamo_read_all(table_name):
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table(table_name)

    try:
        response = table.scan()
        items = response.get("Items", [])
        print(f"Fetched items: {items}")
        return items
    except ClientError as e:
        print("Error reading from DynamoDB:", e)
        return []


def dynamo_delete(table_name, primary_key, primary_value):
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table(table_name)

    key = {primary_key: primary_value}

    try:
        response = table.delete_item(Key=key)
        print("Item deleted successfully:", response)
    except ClientError as e:
        print("Error deleting item:", e)
