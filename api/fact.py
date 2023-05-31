import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from model.facts import Fact
from __init__ import db

fact_api = Blueprint('fact_api', __name__, url_prefix='/api/facts')

api = Api(fact_api)

class FactAPI:
    class Create(Resource):
        def post(self):
            body = request.get_json()
            
            # Validate school
            school = body.get('school')
            if school is None or len(school) < 2:
                return {'message': 'School is missing or is less than 2 characters'}, 400
            
            # Validate fact
            fact = body.get('fact')
            if fact is None or len(fact) < 1:
                return {'message': 'Fact is missing'}, 400

            # Create a new Fact object
            new_fact = Fact(school=school, fact=fact)
            
            # Add the fact to the database
            db.session.add(new_fact)
            db.session.commit()

            return jsonify(new_fact.read()), 201

    class Read(Resource):
        def get(self):
            facts = Fact.query.all()
            json_ready = [fact.read() for fact in facts]
            return jsonify(json_ready)

    class Delete(Resource):
        def delete(self):
            db.session.query(Fact).delete()
            db.session.commit()
            return {'message': 'All facts have been deleted.'}

    # Build REST API endpoints
    api.add_resource(Create, '/create')
    api.add_resource(Read, '/')
    api.add_resource(Delete, '/delete')
