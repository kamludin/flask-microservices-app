from flask import Flask
from app.routes import api  # Ensure this path is correct

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix="/api")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
