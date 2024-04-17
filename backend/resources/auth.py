from flask_restful import Resource
from flask import request, session
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, get_jwt
from datetime import datetime, timedelta
import random

from send_mail import welcome_mail
from resources import api, BLOCKLIST
from database import db, User        

from .fileHandle import profileImage


class Login(Resource):
    def get(self):
        email = request.args.get('email')
        if not email: return {'msg':'Not found'}, 400
        user = User.query.filter_by(email=email).first()
        if user: return {'found':True}, 200
        return {'found':False}, 200
    def post(self):
        if not request.is_json: return {'msg':'Missing JSON in request'}, 400
        data = request.json
        if not data: return {'msg':'No data provided'}, 400
        try:
            reqData = {
                'email': data.get('email'),
                'password': data.get('password'),
            }
        except: return {'msg':'Error in given data format.'}, 400
        if reqData['email'] and reqData['password']:
            user = User.query.filter_by(email=reqData['email']).first()
            if user and user.verify_password(reqData['password']):
                from datetime import datetime
                user.last_login = datetime.now() # setting last login info of user
                db.session.commit()
                access_token = create_access_token(identity=user.email, expires_delta=timedelta(hours=6))
                return {'msg':'Logged in, successfully!','access_token':access_token, 'user':user.to_dict()}, 200
            return {'msg':'Incorrect email or password.'}, 200
        return {'msg':'Provide all required fields and check format!'}, 400
api.add_resource(Login,'/api/auth/login')

class Register(Resource):
    def post(self):
        data = request.form; files = request.files
        if not data : return {'msg':'No data provided'}, 400
        reqData = {
            'email': data.get('email'),
            'f_name': data.get('f_name'),
            'l_name': data.get('l_name'),
        }
        if User.query.filter_by(email=reqData['email']).first():
            return {'exists':True}, 200
        user = User(**reqData)
        password = data.get('password')
        user.hash_password(password)
        img_file = files.get('img_file')
        if img_file: 
            img_path = profileImage().save(img_file)
            user.img_path = img_path
        db.session.add(user); db.session.commit()
        welcome_mail(user.email, user.f_name+' '+user.l_name) #send welcome mail
        return {'exists':False}, 200
api.add_resource(Register,'/api/auth/register')

class Logout(Resource): # jwt required
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        BLOCKLIST.add(jti)
        return {'msg':'Successfully logged out'}, 200
api.add_resource(Logout,'/api/auth/logout')
