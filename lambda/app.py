import json
import boto3
import os


dynamodb = boto3.resource('dynamodb')
tbl_name = os.environ['databaseName']
table = dynamodb.Table(tbl_name)

def lambda_handler(event, context):
    
    ddbResponse = table.update_item(
        Key={
            'id': 'roche_resume'
        },
        UpdateExpression='add visit_count :value',
        ExpressionAttributeValues={
            ":value": 1},
        ReturnValues="UPDATED_NEW"
    )

    # Format dynamodb response into variable
    responseBody = json.dumps({"Count":int(ddbResponse["Attributes"]["visit_count"])})

    # Create api response object
    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": responseBody,
        "headers": {
            "Access-Control-Allow-Headers" : "Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,OPTIONS" 
        }
    }

    # Return api response object
    return apiResponse