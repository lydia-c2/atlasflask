import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.colleges import Colleges
from __init__ import db

college_api = Blueprint('college_api', __name__,
                   url_prefix='/api/colleges')

api = Api(college_api)

# API docs https://flask-restful.readthedocs.io/en/latest/api.html

class CollegesAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate college

            college = body.get('college')
            if college is None or len(college) < 2:
                return {'message': f'Input College Name'}, 210
 
            city = body.get('city')
            if city is None or len(city) < 1:
                return {'message': f'Input City'}, 213
                       
            area = body.get('area')
            if area is None or len(area) < 2:
                return {'message': f'Input Area'}, 210

            rate = body.get('rate')
            if rate is None or len(rate) < 0:
                return {'message': f'Input number of repetitions (must be integer)'}, 214
            
            stufac = body.get('stufac')
            if stufac is None or len(stufac) < 2:
                return {'message': f'Input Student-Faculty Ratio'}, 217
            majors = body.get('majors')
            if majors is None or len(majors) < 2:
                return {'message': f'Input Majors'}, 217

            from model.colleges import Colleges

            io = Colleges(college=college,
                        city=city,
                        rate=rate,
                        area=area,
                        stufac=stufac,
                        majors=majors)
            
            Colleges = io.create()

            # success returns json of user
            if Colleges:
                return jsonify(Colleges.read())
            # failure returns error
            return {'message': f'Processed {college}, a format error or college {college} is duplicate'}, 215
    

    class _Read(Resource):
        def get(self):
            colleges = Colleges.query.all()    # read/extract all users from database
            json_ready = [college.read() for college in colleges]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    class _Delete(Resource):
        def delete(self):
            db.session.query(Colleges).delete()
            db.session.commit()
            return {'message': 'All colleges have been deleted.'}


    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Delete, '/delete')