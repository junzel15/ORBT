import boto3

dynamodb = boto3.client("dynamodb", region_name="us-east-1")


def list_tables():
    response = dynamodb.list_tables()
    print("Tables in DynamoDB:", response["TableNames"])


list_tables()
