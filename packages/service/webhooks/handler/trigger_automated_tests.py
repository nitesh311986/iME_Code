import json
import os

import boto3
from ime_aws_tools.common.logging import Logger

ENVIRONMENT_BRANCH_MAP = {
    'staging': 'staging',
    'uat': 'uat'
}

def handler(event, context):
    Logger.info(event)
    data = json.loads(event['body'])
    branch_name = data.get('payload', {}).get('deployment', {}).get('meta', {}).get('githubCommitRef')

    stage = ENVIRONMENT_BRANCH_MAP.get(branch_name)

    if not stage:
        return {
            'statusCode': 200,
            'body': json.dumps('CodeBuild triggered successfully!')
        }

    client = boto3.client('codebuild')
    response = client.start_build(
        projectName=os.getenv('CODE_BUILD_PROJECT_NAME'),
        environmentVariablesOverride=[
            {
                'name': 'STAGE',
                'value': stage,
                'type': 'PLAINTEXT'
            },
        ],
    )
    Logger.info(response)
    return {
        'statusCode': 200,
        'body': json.dumps('CodeBuild triggered successfully!')
    }
