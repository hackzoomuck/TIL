import boto3
import json
def lambda_handler(event, context):
    print(event)
    return return_json_product_code()
    
def scan_product_code(dynamo_client, *, TableName, **kwargs):
    paginator = dynamo_client.get_paginator("scan")

    for page in paginator.paginate(TableName=TableName, **kwargs):
        yield from page["Items"]

def return_json_product_code():
    dynamo_client = boto3.client("dynamodb")
    print(dynamo_client)
    dict_product_code = {}
    list_product_code = []
    for item in scan_product_code(dynamo_client, TableName="product_code_table"):
        i = item['product_code']
        p = i['S']
        list_product_code.append(p)
    dict_product_code['product_code']=list_product_code
    j = json.dumps(dict_product_code)
    print(j)
    return j

if __name__ == '__lambda_function__':
    lambda_handler()
