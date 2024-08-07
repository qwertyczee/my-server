from http.server import BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # Předpokládejme, že data jsou ve formátu JSON
        data = json.loads(post_data.decode('utf-8'))
        
        # Zpracování dat
        response = {
            'success': True,
            'message': f"Server {data['name']} vytvořen"
        }
        
        # Odpověď
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))
