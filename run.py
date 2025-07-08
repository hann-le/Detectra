import os
from flask import Flask
from app.routes import routes

app = Flask(__name__)

# Allow file uploads up to 5MB (adjust as needed)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  

# Restrict file types later using file extension check if needed

app.register_blueprint(routes)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render uses PORT or defaults to 10000
    app.run(host="0.0.0.0", port=port)
