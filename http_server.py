import os
import json
import http.server
from color_pprint import cprint


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        _directory = os.path.dirname(os.path.abspath(__file__))
        super().__init__(*args, directory=_directory, **kwargs)

    def list_directory(self, path):
        with open("index.html", "r") as fr:
            return fr.read()

    def do_GET(self) -> None:
        cprint(dict(self.headers))
        if self.path == "/health-check":
            self.send_response(200)
        http.server.SimpleHTTPRequestHandler.do_GET(self)


def run(server_class=http.server.HTTPServer, handler_class=http.server.BaseHTTPRequestHandler, port=8080):
    server_address = ('', secrets.get("PORT"))
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    secret_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings/secrets.json')

    with open(secret_file, encoding='utf-8') as f:
        secrets = json.loads(f.read())

    cprint(f"SERVER NAME : {secrets.get('SERVER_NAME')}")
    cprint(f"SERVER PORT : {secrets.get('PORT')}")

    run(handler_class=Handler, port=secrets.get("PORT"))
