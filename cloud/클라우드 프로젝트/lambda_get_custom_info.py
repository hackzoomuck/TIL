import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('collection_table')
    print(event)
    user_id = ''
    try:
        if event["user_id"]:
            user_id = event["user_id"]
    except:
        return {
        'statusCode': 400,
        'body': "No User Id"
    }
    print(user_id)

    response = table.query(
        KeyConditionExpression=Key('user_id').eq(user_id)
    )
    items = response['Items']
    print(items)
  
    return {
        'statusCode': 200,
        'body': items
    }


