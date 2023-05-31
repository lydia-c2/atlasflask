import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building

from model.facts import Fact
from __init__ import db

fact_api = Blueprint('fact_api', __name__,
                   url_prefix='/api/facts')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(fact_api)

class FactPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate school
            school = body.get('school')
            if school is None or len(school) < 2:
                return {'message': f'School is missing, or is less than 2 characters'}, 400
            # validate fact
            fact = body.get('fact')
            if fact is None or len(fact) < 1:
                return {'message': f'fact is missing'}, 400

            ''' #1: Key code block, setup fact OBJECT '''
            so = Fact(school=school, 
                      fact=fact)
            
            
            ''' #2: Key Code block to add fact to database '''
            # create fact in database
            fact = so.create()
            # success returns json of fact
            if fact:
                return jsonify(fact.read())
            # failure returns error
            return {'message': f'Processed {school}, either a format error or rEVEIE {fact} is duplicate'}, 400

    class _Read(Resource):
        def get(self):
            facts = Fact.query.all()    # read/extract all facts from database
            json_ready = [fact.read() for fact in facts]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
    
    class _Delete(Resource):
        def delete(self):
            db.session.query(Fact).delete()
            db.session.commit()
            return {'message': 'All facts have been deleted.'}
            

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Delete, '/delete')