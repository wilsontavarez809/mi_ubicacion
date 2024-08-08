from http.server import SimpleHTTPRequestHandler, HTTPServer

class MiHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

def run(server_class=HTTPServer, handler_class=MiHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Iniciando servidor...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
