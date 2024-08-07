from typing import Dict
import json
import os
from supabase import create_client

# Vložení vašeho Supabase URL a API klíče do environment variables
SUPABASE_URL = os.environ['SUPABASE_URL']
SUPABASE_API_KEY = os.environ['SUPABASE_API_KEY']

# Inicializace klienta Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)

def handler(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        server_name = data.get('name')

        if not server_name:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Server name is required"})
            }

        # Uložení serveru do Supabase
        response = supabase.table('servers').insert({"name": server_name}).execute()

        return {
            "statusCode": 200,
            "body": json.dumps({"success": True, "server": response.data[0]})
        }
    else:
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Method not allowed"})
        }
