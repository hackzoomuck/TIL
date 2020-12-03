import json
import boto3
from botocore.exceptions import ClientError
from datetime import datetime

def get_email(email, gn, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('collection_table')

    try:
        response = table.get_item(Key={'user_id': email,'group_number':gn})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        
        return response.get('Item')



def make_init_table(user_id,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('collection_table')
    dt = datetime.now()
    dt_transfer = datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')
    
    response = table.put_item(
       Item={
            'user_id': user_id,
            'createdat': dt_transfer,
            'updatedat': dt_transfer,
            'group_number': '1',
            'group_lists':[
                {
                    "title": "프린터사용설명서들",
                    "pos": 65535,
                    "createdAt" : "2020-11-12-02:54PM",
                    "updatedAt" : "2020-11-12-02:54PM",
                    "cards": [
                    {
                        "id": 1,
                        "title": "SL_2032"
                    }
                    ]
                }
            ]
        }
    )
    return response    
    
    
def lambda_handler(event, context):
    # TODO implement
    print(event)
    select_query_userid = event['userId']
    print(select_query_userid)
    
    response_db = get_email(select_query_userid, '1')
    print('plz',response_db)
    if response_db:
        return {
            'statusCode': 200,
            'body': json.dumps('YES TABLE')
        }
    else :
        print('init table:', make_init_table(select_query_userid))
        return {
            'statusCode': 201,
            'body': json.dumps('NO TABLE')
        }
        

if __name__ == '__lambda_function__':
    lambda_handler()
