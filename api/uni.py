import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building

from model.unis import University
from __init__ import db

uni_api = Blueprint('uni_api', __name__,
                   url_prefix='/api/unis')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(uni_api)

class UniversityAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate school
            school = body.get('school')
            if school is None or len(school) < 2:
                return {'message': f'School is missing, or is less than 2 characters'}, 400
            # validate review
            rate = body.get('rate')
            if rate is None or len(rate) < 1:
                return {'message': f'Acceptance Rate is missing'}, 400
            stufac = body.get('stufac')
            if stufac is None or len(stufac) < 1:
                return {'message': f'Student Faculty Ratio is missing'}, 400

            ''' #1: Key code block, setup REVIEW OBJECT '''
            so = University(school=school, 
                      rate=rate,
                      stufac=stufac)
            
            
            ''' #2: Key Code block to add REVIEW to database '''
            # create review in database
            school = so.create()
            # success returns json of review
            if school:
                return jsonify(school.read())
            # failure returns error
            return {'message': f'Processed {school}, either a format error or rEVEIE {school} is duplicate'}, 400

    class _Read(Resource):
        def get(self):
            schools = University.query.all()    # read/extract all REVIEWS from database
            json_ready = [school.read() for school in schools]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
    
    class _Delete(Resource):
        def delete(self):
            db.session.query(University).delete()
            db.session.commit()
            return {'message': 'All schools have been deleted.'}
            

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Delete, '/delete')