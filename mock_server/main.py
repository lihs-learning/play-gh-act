import argparse
import logging
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # 处理 GET 请求
    def do_GET(self):
        logging.info('GET request,\nPath: %s\nHeaders:\n%s\n', str(self.path), str(self.headers))
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, world!')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--port',
        type=int,
        default=8000,
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
        format='[%(asctime)s %(levelname)s] %(message)s',
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    server_address = ('', args.port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    logging.info('Mock Server running on port {}...'.format(args.port))
    httpd.serve_forever()


if __name__ == '__main__':
    main()
