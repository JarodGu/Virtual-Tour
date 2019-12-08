import json
import boto3
import boto3
import json
import decimal

db = boto3.resource('dynamodb')
table = db.Table('AlbumTable')

# Amazon's decimal encoder code
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

# Returns info about an album
def lambda_handler(event, context):
    AlbumID = event['AlbumID']

    img = table.get_item(
        Key={
            'AlbumID': AlbumID,
            'ImageID': 0
        }
    )
    
    if 'Item' in img:
        
        body = {
            'AlbumID': AlbumID,
            'AlbumDescription': img['Item']['AlbumDescription'],
            'TotalImages': img['Item']['TotalImages']
        }
        return {
            'statusCode': 200,
            'body': json.dumps(body, cls=DecimalEncoder)
        }
    else:
        return {
            'statusCode': 400,
            'body': 'Error: Item not found'
        }
    