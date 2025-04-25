import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserGreeter')

def lambda_handler(event, context):
    try:
        http_method = event['httpMethod']
        
        if http_method == 'POST':
            body = json.loads(event['body'])
            name = body.get('name', 'Anonymous')
            item_id = str(uuid.uuid4())
            
            table.put_item(Item={
                'id': item_id,
                'name': name
            })
            
            return {
                'statusCode': 200,
                'body': json.dumps({'message': f'Hello, {name}! Saved with ID: {item_id}'})
            }
            
        elif http_method == 'GET':
            items = []
            response = table.scan(Limit=10, ConsistentRead=True)
            items.extend(response.get('Items', []))
            while 'LastEvaluatedKey' in response:
                response = table.scan(Limit=10, ExclusiveStartKey=response['LastEvaluatedKey'], ConsistentRead=True)
                items.extend(response.get('Items', []))
            return {
                'statusCode': 200,
                'body': json.dumps({'names': items})
            }
            
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Unsupported method'})
            }
            
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
