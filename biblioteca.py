from decimal import Decimal
from pprint import pprint
import boto3
from botocore.exceptions import ClientError
from robot.libraries.BuiltIn import BuiltIn


def put(title, year, plot, rating, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8005")

    table = dynamodb.Table('Movies')
    response = table.put_item(
       Item={
            'year': year,
            'title': title,
            'info': {
                'plot': plot,
                'rating': rating
            }
        }
    )
    return response

def get(Artist,AlbumTitle ,dynamodb=None):
    if not dynamodb:
        BuiltIn().log_to_console("##### PASSOU AQUI#####")
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8006")
        BuiltIn().log_to_console(dynamodb)
    BuiltIn().log_to_console("##### PASSOU AQUI#####")
    table = dynamodb.Table('Music')

    try:
        BuiltIn().log_to_console(table)
        BuiltIn().log_to_console(Artist)
        BuiltIn().log_to_console(AlbumTitle)
        response = table.get_item(Key={'Artist': Artist, 'SongTitle': AlbumTitle})
        BuiltIn().log_to_console(response)
    except ClientError as e:
        print(e.response['Error']['Message'])
        BuiltIn().log_to_console(e.response['Error']['Message'])
    except Exception as e:
        BuiltIn().log_to_console(e)
    else:
        return response['Item']

def update(title, year, rating_increase, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8005")

    table = dynamodb.Table('Movies')

    response = table.update_item(
        Key={
            'year': year,
            'title': title
        },
        UpdateExpression="set info.rating = info.rating + :val",
        ExpressionAttributeValues={
            ':val': Decimal(rating_increase)
        },
        ReturnValues="UPDATED_NEW"
    )
    return response