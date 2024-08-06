from flask import Flask, request, jsonify

app = Flask(__name__)

servers = []

@app.route('/create-server', methods=['POST'])
def create_server():
    data = request.json
    server_name = data.get('name')
    if not server_name:
        return jsonify({'success': False, 'message': 'Server name is required'}), 400
    new_server = {'name': server_name, 'id': len(servers) + 1}
    servers.append(new_server)
    return jsonify({'success': True, 'server': new_server})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
