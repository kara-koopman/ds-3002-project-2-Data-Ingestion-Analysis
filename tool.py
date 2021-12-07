import requests
import json 
import boto3
import decimal
import datetime
import sched
import time

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('project2')
print('Connected to a database')

scheduler = sched.scheduler(time.time, time.sleep)

def insert(factor, pi, time):
    response = table.put_item(
        Item= {
            'factor': factor,
            'time': time,
            'pi': pi
        }
    )
    print(datetime.datetime.now())
    print(response)
    print('--------------------------')

def fetch():
    call = requests.get('https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi')
    info = json.loads(call.text, parse_float=decimal.Decimal)
    print(info)
    insert(info['factor'],info['pi'],info['time'])

for i in range(60):
    scheduler.enter(i * 60, 1, fetch)

scheduler.run()

        
