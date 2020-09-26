from flask import Flask
from flask_restful import Api

from party_people import PartyPeople


def main():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(PartyPeople, '/')

    app.run(host='0.0.0.0', port=80, debug=True)
