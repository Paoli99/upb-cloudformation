import json
import boto3 
 

def getUser(event, context):
    print(json.dumps({'running':True}))
    print(json.dumps(event))
    return{
        'statusCode': 200,
        'body': json.dumps('Hello from lambda!')
    }
    
def putUser(event, context):
    print(json.dumps({'running':True}))
    print(json.dumps(event))
    return{
        'statusCode': 200,
        'body': json.dumps('Hello from lambda!')
    }