from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Load config
if os.environ.get('MODE') == 'DEVELOPMENT':
    app.config.from_object('config.config_development')
elif os.environ.get('MODE') == 'PRODUCTION':
    app.config.from_object('config.config_production')


@app.route("/")
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
