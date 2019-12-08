import json
import boto3

db = boto3.resource('dynamodb')
table = db.Table('AlbumTable')

# Returns the current list of albums stored in the database
# and their respective partition keys
# Album list is tracked in the first database entry at P:0 S:0


def lambda_handler(event, context):
    response = table.get_item(
        Key={
            'AlbumID': 0,
            'ImageID': 0
        }
    )
    
    albumList = []
    albumIndices = []
    
    for index, item in enumerate((response['Item']['AlbumList'])[1:]):
        if(item.strip()):
            albumList.append(item)
            albumIndices.append(index + 1)
    
    body = {
        'AlbumList': albumList,
        'AlbumIndices': albumIndices
    }
    
    return{
        'statusCode': 200,
        'body': json.dumps(body)
    }