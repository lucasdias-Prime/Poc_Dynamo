from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_movie(title, year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8006")

    table = dynamodb.Table('Music')

    try:
        response = table.get_item(Key={'year': year, 'title': title})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return print(response['Item'])


if __name__ == '__main__':
    movie = get_movie("The Big New Movie", 2015,)
    if movie:
        print("Get movie succeeded:")
        pprint(movie, sort_dicts=False)


aws dynamodb get-item --consistent-read \ --table-name Music \ --key '{ "Artist": {"S": "Acme Band"}, "SongTitle": {"S": "Happy Day"}}'

aws dynamodb get-item --consistent-read --table-name Movies --key file://get.json