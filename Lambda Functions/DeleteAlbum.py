import json
import boto3

db = boto3.resource('dynamodb')
table = db.Table('AlbumTable')

# Removes an album from the database.
# NOTE: Doesn't actually delete the data!
# Implementation:
#   Updates entry in dbinfo AlbumList to ' '
#   Sets 'deleted' in albuminfo entry to true

def lambda_handler(event, context):
    # Entry contains info about the database
    dbinfo = table.get_item(
        Key={
            'AlbumID': 0,
            'ImageID': 0
        }
    )
    if event['AlbumID'] >= len(dbinfo['Item']['AlbumList']) or event['AlbumID'] < 1:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: Album index does not exist')
    }
    
    #Update dbinfo item
    table.update_item(
        Key={
            'AlbumID': 0,
            'ImageID': 0
        },
        UpdateExpression = "SET AlbumList[" + str(event['AlbumID']) + "] = :s",
        ExpressionAttributeValues={
            ':s' : ' '
        }
    )
    # Update albuminfo item
    table.update_item(
        Key={
            'AlbumID': event['AlbumID'],
            'ImageID': 0
        },
        UpdateExpression = "SET Deleted = :d",
        ExpressionAttributeValues={
            ':d' : True
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully removed album entry from database')
    }