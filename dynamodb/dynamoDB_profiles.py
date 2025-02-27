import boto3
from botocore.exceptions import ClientError


def dynamo_write(table_name, item):
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table(table_name)

    try:
        update_expression = "SET " + ", ".join(
            [f"#{k} = :{k}" for k in item if k != "email"]
        )
        expression_attribute_names = {f"#{k}": k for k in item if k != "email"}
        expression_attribute_values = {f":{k}": item[k] for k in item if k != "email"}

        response = table.update_item(
            Key={"email": item["email"]},
            UpdateExpression=update_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values,
        )
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


def dynamo_delete(table_name, primary_key, primary_value):
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table(table_name)

    key = {primary_key: primary_value}

    try:
        response = table.delete_item(Key=key)
        print("Item deleted successfully:", response)
    except ClientError as e:
        print("Error deleting item:", e)
