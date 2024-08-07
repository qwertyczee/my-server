from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_API_KEY = os.getenv('SUPABASE_API_KEY')
SUPABASE_TABLE = 'servers'

@app.route('/create-server', methods=['POST'])
def create_server():
    data = request.json
    server_name = data.get('name')
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}",
        headers={
            "apikey": SUPABASE_API_KEY,
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        },
        json={"name": server_name}
    )
    if response.status_code == 201:
        return jsonify({'success': True, 'server': response.json()[0]})
    else:
        return jsonify({'success': False, 'error': response.text}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
