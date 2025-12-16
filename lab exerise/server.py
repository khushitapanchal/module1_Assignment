import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

class CustomHandler(Handler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "<h1>Hello, World!</h1><p>My first Python server!</p>"
        self.wfile.write(bytes(message, "utf8"))

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}")
    # Keep the server running indefinitely
    httpd.serve_forever()
