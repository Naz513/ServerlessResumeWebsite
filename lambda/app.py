import boto3
import json
import os


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    DynamoDBTable = os.environ['databaseName']
    table = dynamodb.Table(DynamoDBTable)

    updated_response = table.update_item(
        Key={
            'visits': "views"
        },
        UpdateExpression='ADD Counts :value',
        ExpressionAttributeValues={
            ':value': 1
        },
        ReturnValues="UPDATED_NEW"
    )

    print(updated_response)

    responseBody = json.dumps(
        {"views": int(float(updated_response["Attributes"]["Counts"]))})

    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": responseBody,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,OPTIONS"
        },
    }

    return apiResponse
