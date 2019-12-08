import json
import boto3
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

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

# Returns info about an image
def lambda_handler(event, context):
    AlbumID = event['AlbumID']
    ImageID = event['ImageID']
    
    img = table.get_item(
        Key={
            'AlbumID': AlbumID,
            'ImageID': ImageID
        }
    )
    
    if 'Item' in img:
        return {
            'statusCode': 200,
            'body': json.dumps(img['Item'], cls=DecimalEncoder)
        }
    else:
        return {
            'statusCode': 400,
            'body': 'Error: Item not found'
        }
    