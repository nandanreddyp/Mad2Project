from flask_restful import Resource
from flask import request, session
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, get_jwt
from datetime import datetime, timedelta
import random

from resources import api, BLOCKLIST
from database import db, User        



class Login(Resource):
    def get(self):
        email = request.args.get('email','').strip() or None
        if email:
            user = User.query.filter_by(email=email).first()
            if user: return {'msg':'Found'}, 200
        return {'msg':'Not found'}, 404
    def post(self):
        if not request.is_json: return {'msg':'Missing JSON in request'}, 400
        data = request.json
        if not data: return {'msg':'No data provided'}, 400
        try:
            reqData = {
                'email': data.get('email','').strip() or None,
                'password': data.get('password','').strip() or None,
            }
        except: return {'msg':'Error in given data format.'}, 400
        if reqData['email'] and reqData['password']: 
            print(reqData['email'])
            user = User.query.filter_by(email=reqData['email']).first()
            if user and user.verify_password(reqData['password']):
                from datetime import datetime
                user.last_login = datetime.now() # setting last login info of user
                db.session.commit()
                access_token = create_access_token(identity=user.email, expires_delta=timedelta(hours=6))
                return {'msg':'Logged in, successfully!','access_token':access_token, 'user':user.to_dict()}, 200
            return {'msg':'Incorrect email or password.'}, 404
        return {'msg':'Provide all required fields and check format!'}, 400
api.add_resource(Login,'/api/auth/login')

class Register(Resource):
    def post(self):
        if not request.is_json: return {'msg':'Missing JSON in request'}, 400
        data = request.json
        if not data: return {'msg':'No data provided'}, 400
        try:
            reqData = {
                'email': data.get('email','').strip() or None,
                'f_name': data.get('f_name','').strip() or None,
                'l_name': data.get('l_name','').strip() or None,
                'img_path': data.get('img_path','').strip() or None,
            }
            password = data.get('password','').strip() or None
        except: return {'msg':'Error in given data format.'}, 400
        if reqData['email'] and reqData['f_name'] and password:
            if not User.query.filter_by(email=reqData['email']).first():
                user = User(**reqData)
                user.hash_password(password)
                db.session.add(user); db.session.commit()
                return {'msg':'Account created, successfully!'}, 200
            return {'msg':'Account already exists'}, 409
        return {'msg':'Provide all required fields.'}, 400
api.add_resource(Register,'/api/auth/register')

class Logout(Resource): # jwt required
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        BLOCKLIST.add(jti)
        return {'msg':'Successfully logged out'}, 200
api.add_resource(Logout,'/api/auth/logout')
