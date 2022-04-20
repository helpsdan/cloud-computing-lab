import boto3
from boto3.dynamodb.conditions import Key


class FilesDAO:
    def __init__(self, table_name):
        self.__table = boto3.resource('dynamodb').Table(table_name)


    def put_item(self, item):
        return self.__table.put_item(
            Item=item,
            ReturnConsumedCapacity='TOTAL'
        )
  