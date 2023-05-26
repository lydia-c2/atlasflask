import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.colleges import Colleges

College_api = Blueprint('College_api', __name__,
                   url_prefix='/api/College')

api = Api(College_api)

# API docs https://flask-restful.readthedocs.io/en/latest/api.html

class CollegeAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate exercise type
            college = body.get('college')
            if college is None or len(college) < 2:
                return {'message': f'Input College Name'}, 210
            
            area = body.get('area')
            if area is None or len(area) < 2:
                return {'message': f'Input Area'}, 217
            
            # validate uid
            id = body.get('id')
            uid = str(datetime.now()) # temporary UID that is unique to fill garbage data
            if uid is None or len(uid) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 212

            cityName = body.get('cityName')
            if cityName is None or len(cityName) < 1:
                return {'message': f'Input City'}, 213
            
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

            io = Colleges(id=id,
                            uid=uid,
                            college=college,
                            cityName=cityName,
                            rate=rate,
                            area=area,
                            stufac=stufac,
                            majors=majors
                        )
            
            Colleges = io.create()

            # success returns json of user
            if Colleges:
                return jsonify(Colleges.read())
            # failure returns error
            return {'message': f'Processed {college}, a format error or User ID {uid} is duplicate'}, 215
    

    class _Read(Resource):
        def get(self):
            College = Colleges.query.all()    # read/extract all users from database
            json_ready = [College.read() for College in Colleges]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')