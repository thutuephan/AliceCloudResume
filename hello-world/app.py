import boto3
import json


print('Loading function')
# resource: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.update_item

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('alice-resume-cloud2')


def lambdaHandler(event, context):
    response = table.update_item(
        Key={
            'ID': 'visitors'
        },
        UpdateExpression="ADD #att :val1",
        ConditionExpression="attribute_not_exists(#a)",
        ExpressionAttributeNames={"#att": "Counts", "#a": "attribute"},
        ExpressionAttributeValues={":val1": 1},
        ReturnValues="UPDATED_NEW"
    )
    visitorCounter = response['Attributes']['Counts']
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS, GET, PUT',
            'Access-Control-Allow-Headers': '*',
            'Accept': '*/*',
            'Content-Type': 'application/json'
        },

        'body': visitorCounter
    }
