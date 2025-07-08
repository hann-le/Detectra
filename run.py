import os
from flask import Flask
from app.routes import routes

app = Flask(__name__, template_folder="app/templates")  # Tell Flask where templates are

app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

app.register_blueprint(routes)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
