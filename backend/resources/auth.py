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
            user = User.query.filter_by(email=reqData['email']).first()
            if user and user.verify_password(reqData['password']):
                from datetime import datetime
                user.last_login = datetime.now() # setting last login info of user
                db.session.commit()
                access_token = create_access_token(identity=user.email, expires_delta=timedelta(hours=12))
                return {'msg':'Logged in, successfully!','access_token':access_token, 'user':user.to_dict()}, 200
            return {'msg':'Incorrect email or password.'}, 401
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
            return {'msg':'Account already exists'}, 400
        return {'msg':'Provide all required fields.'}, 400
api.add_resource(Register,'/api/auth/register')

class Verify(Resource): # jwt required
    @jwt_required()
    def get(self):
        email = request.args.get('email','').strip()
        if email:
            if request.args.get('reset') and session.get('otp'):
                session.pop('otp')
                msg = 'New OTP generated and sent to email'
            elif not session.get('otp'):
                msg = 'OTP sent to email'
            else:
                return {'msg':'OTP already sent to email'}, 400
            session['otp'] = random.randint(1000, 9999)
            # send mail with otp
            return {'msg':msg,'otp':session.get('otp')}, 200
        return {'msg':'Email required to generate otp'}, 400
    @jwt_required()
    def post(self): # get identity of user and make verified
        if not request.is_json: return {'msg':'Missing JSON in request'}, 400
        if 'otp' in session:
            data = request.json
            if not data: return {'msg':'No data provided'}, 400
            try:
                otp = int(data.get('otp'))
            except: return {'msg':'Error in given data format.'}, 400
            if otp:
                if otp == session['otp']:
                    session.pop('otp')
                    return {'msg':'Otp verified'}, 200
                return {'msg':'Wrong otp'}, 401
            return {'msg':'No otp provided'}, 400
        return {'msg':'First generate otp'}, 400
api.add_resource(Verify,'/api/auth/verify')
    
class PasswordForgot(Resource):
    def get(self):
        email = request.args.get('email','').strip()
        if email:
            if User.query.filter_by(email=email).first():
                if request.args.get('reset') and session.get('otp'):
                    session.pop('otp')
                    msg = 'New OTP generated and sent to email'
                elif not session.get('otp'):
                    msg = 'OTP sent to email'
                else:
                    return {'msg':'OTP already sent to email'}, 400
                session['otp'] = random.randint(1000, 9999)
                session['email'] = email
                # send mail with otp
                return {'msg':msg,'otp':session.get('otp')}, 200
            return {'msg':'No user exists with this email'}, 400
        return {'msg':'Email required to generate otp'}, 400
    def post(self):
        if not request.is_json: return {'msg':'Missing JSON in request'}, 400
        data = request.json
        if not data: return {'msg':'No data provided'}, 400
        try:
            reqData = {
                'email': data.get('email','').strip() or None,
                'password': data.get('password','').strip() or None,
                'otp': int(data.get('otp'))
            }
        except: return {'msg':'Error in given data format.'}, 400
        if reqData['email'] and reqData['password'] and reqData['otp']:
            user = User.query.filter_by(email=reqData['email']).first()
            if user :
                if 'otp' in session:
                    if reqData['otp'] == session['otp']:
                        session.pop('otp')
                        user.hash_password(reqData['password'])
                        db.session.commit()
                        return {'msg':'Password changed'}, 200
                    return {'msg':'Wrong otp'}, 401
                return {'msg':'First generate otp'}, 400
            return {'msg':'No user exists with this email'}, 400
        return {'msg':'Email, password, and OTP are required'}, 400
api.add_resource(PasswordForgot,'/api/auth/forgot-password')

class PasswordReset(Resource): # jwt required
    @jwt_required()
    def post(self):
        if not request.is_json: return {'msg':'Missing JSON in request'}, 400
        data = request.json
        if not data: return {'msg':'No data provided'}, 400
        try:
            reqData = {
                'email': data.get('email','').strip() or None,
                'password': data.get('password','').strip() or None,
                'otp': int(data.get('otp'))
            }
        except: return {'msg':'Error in given data format.'}, 400
        if reqData['email'] and reqData['password'] and reqData['otp']:
            user = User.query.filter_by(email=reqData['email']).first()
            user.hash_password(reqData['password'])
            db.session.commit()
        return {'msg':'Password changed'}, 200
api.add_resource(PasswordReset,'/api/auth/reset-password')

class Logout(Resource): # jwt required
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        BLOCKLIST.add(jti)
        return {'msg':'Successfully logged out'}, 200
api.add_resource(Logout,'/api/auth/logout')
