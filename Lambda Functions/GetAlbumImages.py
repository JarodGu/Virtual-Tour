import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

db = boto3.resource('dynamodb')
table = db.Table('AlbumTable')

# Returns a sequential list of all image URL's in an album
# Takes an AlbumID or AlbumName

def lambda_handler(event, context):
    response = table.query(
        KeyConditionExpression=Key('AlbumID').eq(event['AlbumID'])
    )
    S3URLList = []
    for i in response['Items']:
        print(i['S3URL'])
        S3URLList.append(i['S3URL'])
        
    if len(S3URLList) > 0: # results found
         return {
            'statusCode': 200,
            'body': json.dumps(S3URLList)
        }
    else: # no results found, album is empty/doesn't exist
        return {
            'statusCode': 400,
            'body': json.dumps('No results found')
        }