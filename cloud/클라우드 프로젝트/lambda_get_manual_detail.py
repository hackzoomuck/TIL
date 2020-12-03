import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('product_table')
    
    product_code = ''
    try:
        if event["product_code"]:
            product_code = event["product_code"]
    except:
        return {
        'statusCode': 400,
        'body': "No Product Code"
    }

    response = table.query(
        KeyConditionExpression=Key('product_code').eq(event["product_code"])
    )
    items = response['Items']

  
    return {
        'statusCode': 200,
        'body': items
    }


