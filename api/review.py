import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building

# from model.users import User
from model.reviews import Review
from __init__ import db

review_api = Blueprint('review_api', __name__,
                   url_prefix='/api/reviews')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(review_api)

class ReviewPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            school = body.get('school')
            if school is None or len(school) < 2:
                return {'message': f'School is missing, or is less than 2 characters'}, 400
            # validate review
            review = body.get('review')
            if review is None or len(review) < 1:
                return {'message': f'Review is missing'}, 400

            ''' #1: Key code block, setup USER OBJECT '''
            so = Review(school=school, 
                      review=review)
            
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            user = so.create()
            # success returns json of user
            if user:
                return jsonify(user.read())
            # failure returns error
            return {'message': f'Processed {school}, either a format error or User ID {review} is duplicate'}, 400

    class _Read(Resource):
        def get(self):
            users = Review.query.all()    # read/extract all users from database
            json_ready = [user.read() for user in users]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
    
    class _Delete(Resource):
        def delete(self):
            db.session.query(Review).delete()
            db.session.commit()
            return {'message': 'All reviews have been deleted.'}
            

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Delete, '/delete')