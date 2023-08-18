from flask import Flask
from dotenv import load_dotenv
import os
from config.dev import config_dev
from config.prod import config_prod

load_dotenv()

app = Flask(__name__)

# Load config
if os.environ.get('MODE') == 'DEVELOPMENT':
    app.config.update(**config_dev)
elif os.environ.get('MODE') == 'PRODUCTION':
    app.config.update(**config_prod)


@app.route("/")
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
