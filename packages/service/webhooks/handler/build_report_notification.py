import os
import json
import boto3
import urllib.parse

import requests

s3_client = boto3.client('s3')


def handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    file_url = f"https://{bucket_name}.s3.amazonaws.com/{object_key}"

    stage = object_key.split('/')[0]

    slack_message = {
        "text": f"Automated Tests build report for *{stage}* environment is ready.",
        "attachments": [
            {
                "fallback": "Test report link",
                "actions": [
                    {
                        "type": "button",
                        "text": "View Report",
                        "url": file_url
                    }
                ]
            }
        ]
    }

    webhook_url = os.environ['SLACK_WEBHOOK_URL']
    response = requests.post(webhook_url, data=json.dumps(slack_message), headers={'Content-Type': 'application/json'})

    if response.status_code != 200:
        raise ValueError(
            f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")
