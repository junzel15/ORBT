from dynamodb.dynamoDB_profiles import dynamo_read


def get_user_from_dynamodb(email):
    try:

        return dynamo_read("profiles", "email", email)
    except Exception as e:
        print(f"Error retrieving user from DynamoDB: {e}")
        return None
