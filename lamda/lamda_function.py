import json

def lamda_handler(event, context):
    return {
        'statusCode':200,
        'body': json.dumps('Hello from our CICD github actions workflow vscode')
    }