from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
os.chdir(Path(__file__).parent)
ThreadingHTTPServer(('0.0.0.0',3000),SimpleHTTPRequestHandler).serve_forever()
