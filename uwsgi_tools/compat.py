import sys

__all__ = [
    'BaseHTTPRequestHandler', 'TCPServer', 'get_content_type',
]

PY3 = sys.version_info[0] == 3


if PY3:
    from http.server import BaseHTTPRequestHandler
    from socketserver import TCPServer
else:
    from BaseHTTPServer import BaseHTTPRequestHandler
    from SocketServer import TCPServer


def get_content_type(headers):
    if PY3:
        return headers.get('content-type')
    else:
        return headers.typeheader
