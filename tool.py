import requests
import json 
import boto3
import decimal
import datetime
import time

current = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('project2')

def insert(factor, pi, time):
    response = table.put_item(
        Item= {
            'factor': factor,
            'time': time,
            'pi': pi,
            'inserton': current
        }
    )

def fetch():
    call = requests.get('https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi')
    info = json.loads(call.text, parse_float=decimal.Decimal)
    print(info)
    insert(info['factor'],info['pi'],info['time'])
        
fetch()