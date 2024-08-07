import json

def handler(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            response = {
                'success': True,
                'message': f"Server {data.get('name', 'unknown')} created"
            }
            return {
                'statusCode': 200,
                'body': json.dumps(response)
            }
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Invalid JSON'})
            }
    return {
        'statusCode': 405,
        'body': json.dumps({'error': 'Method Not Allowed'})
    }
