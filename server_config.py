import os
from route_config import *

# Run debug mode while testing
# app.debug = True

host = os.environ.get("IP", '0.0.0.0')
port = int(os.environ.get("PORT", 8080))
app.run(host = host, port = port)
