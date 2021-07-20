from flask import Flask
import json
from config import Config
from flask_cors import CORS
from dotenv import load_dotenv
from modules.api import api

load_dotenv()


def setup_extensions(application):
    api.init_app(application)


def load_permission():
    f = open('./permission.json', )
    data = json.load(f)
    data_permission = {}
    for i in data:
        data_permission[i['teamId']] = i

    print("data_permission", data_permission)
    Config.PERMISSION = data_permission
    f.close()


app = Flask(__name__)
CORS(app)


def main():
    load_permission()
    setup_extensions(app)
    app.run(host='localhost', port=8888)


if __name__ == '__main__':
    main()
