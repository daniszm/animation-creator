import json, boto3, uuid, os

sqs = boto3.resource('sqs', region_name="eu-central-1")
tweets = sqs.get_queue_by_name(QueueName=os.getenv('APP_QUEUE_NAME'))
response = tweets.send_message(MessageBody='Działa?')
