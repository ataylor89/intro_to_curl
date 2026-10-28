from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

products = [
    {
        "id": 1,
        "name": "MacBook Neo",
        "price": 600
    },
    {
        "id": 2,
        "name": "MacBook Air",
        "price": 700
    },
    {
        "id": 3,
        "name": "MacBook Pro",
        "price": 800
    },
    {
        "id": 4,
        "name": "iPhone",
        "price": 600
    },
    {
        "id": 5,
        "name": "iMac",
        "price": 800
    },
    {
        "id": 6,
        "name": "Apple Watch",
        "price": 250
    },
    {
        "id": 7,
        "name": "Apple TV",
        "price": 300
    }
]

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = {k: v[0] for k, v in parse_qs(parsed_url.query).items()}
        if path == '/products':
            product_id = query_params.get('id', None)
            product_name = query_params.get('name', None)
            search_term = query_params.get('term', None)
            price = query_params.get('price', None)
            response_data = {"resultCount": 0, "results": []}
            for product in products:
                match = False
                if product_id:
                    try:
                        if int(product_id) == product['id']:
                            match = True
                    except:
                        pass
                elif product_name and product_name.lower() == product['name'].lower():
                    match = True
                elif search_term and search_term.lower() in product['name'].lower():
                    match = True
                elif price:
                    try:
                        if product['price'] <= int(price):
                            match = True
                    except:
                        pass
                if match:
                    response_data['resultCount'] += 1
                    response_data['results'].append(product)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            error_data = {"error": "URL not found"}
            self.wfile.write(json.dumps(error_data).encode('utf-8'))

def run_server(host='localhost', port=8080):
    server_address = (host, port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Starting HTTP server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping HTTP server.")
        httpd.server_close()

if __name__ == '__main__':
    run_server()
