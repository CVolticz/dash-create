from waitress import serve
from index import server

# File to export on server
serve(server, listen="*:7000")