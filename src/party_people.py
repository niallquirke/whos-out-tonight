from flask_restful import Resource


class PartyPeople(Resource):

    def get(self):
        return {'party-people': 'niall, donal'}
