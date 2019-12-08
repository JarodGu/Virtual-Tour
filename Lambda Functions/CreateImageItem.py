import json
import boto3

db = boto3.resource('dynamodb')
table = db.Table('AlbumTable')

# Creates an entry in the DynamoDB database corresponding
# to a new image. Can either create a new album or add the
# image to an existing one, depending on if the album name exists.
# Entry consists of an AlbumID, ImageID, S3URl, and more attributes

def lambda_handler(event, context):
    #AlbumID = event['AlbumID']
    #ImageID = event['ImageID']
    
    AlbumName = event['AlbumName']
    AlbumDescription = event['AlbumDescription']
    Annotations = event['Annotations']
    Location = event['Location']
    S3URL = event['S3URL']
    
    #Search if album already exists
    # if so, add to that album
    # number of images is stored in the 0'th entry
    # Maybe store DB info in the 0,0 entry too
    # List of all albums and total images
    
    # Entry contains info about the database
    dbinfo = table.get_item(
        Key={
            'AlbumID': 0,
            'ImageID': 0
        }
    )
    
    # Search list for album
    albumIndex = -1
    try:
        albumIndex = (dbinfo['Item']['AlbumList']).index(AlbumName)
    except:
        print('Existing album found')
        
    # set album index to a new value
    if albumIndex != -1: # add image item to existing album
        # Get album info stored in 0'th imageID
        albuminfo = table.get_item(
            Key={
                'AlbumID': albumIndex,
                'ImageID': 0
            }
        )
        # Create new entry in existing album
        table.put_item(
            Item={
                'AlbumID': albumIndex,
                'ImageID': albuminfo['Item']['TotalImages'],
                'AlbumName': albuminfo['Item']['AlbumName'],
                'Annotations': Annotations,
                'Location': Location,
                'S3URL': S3URL
            }
        )
        
        # Update albuminfo item
        table.update_item(
            Key={
                'AlbumID': albumIndex,
                'ImageID': 0
            },
            UpdateExpression = "set TotalImages = TotalImages + :val",
            ExpressionAttributeValues={
                ':val' : 1
            }
        )

    else: # adding item to new album
        newAlbumIndex = len(dbinfo['Item']['AlbumList'])
        # Create new entry for image
        table.put_item(
            Item={
                'AlbumID': newAlbumIndex,
                'ImageID': 0,
                'AlbumName': AlbumName,
                'AlbumDescription': AlbumDescription,
                'Deleted': False,
                'Annotations': Annotations,
                'Location': Location,
                'TotalImages': 1,
                'S3URL': S3URL
            }
        )
        
        # update dbinfo item
        table.update_item(
            Key={
                'AlbumID': 0,
                'ImageID': 0
            },
            UpdateExpression = "set TotalImages = TotalImages + :val, AlbumList = list_append(AlbumList, :a)",
            ExpressionAttributeValues={
                ':val' : 1,
                ':a' : [AlbumName]
            }
        )
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully added image to DB')
    }