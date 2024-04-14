from flask import request
from flask_restful import Resource

from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from resources import api, BLOCKLIST
from database import db, User



class UserResource(Resource): #✅
    @jwt_required()
    def __init__(self):
        self.user = User.query.filter_by(email = get_jwt_identity()).first()
    @jwt_required()
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            return {'user':user.to_dict()}, 200
        return {'msg':'user not found'}, 404
    @jwt_required()
    def put(self, user_id):
        if not self.user.id == user_id:
            return {'msg':'Can not update others'}
        if not request.is_json: return {'msg':'Missing JSON in request'}, 400
        data = request.json; user = self.user
        if not data: return {'msg':'No data provided'}, 400
        try:
            f_name = data.get('f_name','').strip() or None
            if not f_name: raise ValueError('Name can not be empty')
            l_name = data.get('l_name','').strip() or None
            password = data.get('password','').strip() or None
            if not password: raise ValueError('Password can not be empty')
            img_path = data.get('img_path','').strip() or None
        except ValueError as e: return {'msg':str(e)}, 400
        except: return {'msg':'Make sure all fields are given and they are in correct format.'}, 400 
        user.f_name = f_name; user.l_name = l_name
        user.password = password
        if img_path: user.img_path = img_path
        else: user.set_default_img_path()
        db.session.commit()
        return {'msg':'User updated'}, 200
    @jwt_required()
    def delete(self, user_id):
        if not self.user.id == user_id:
            return {'msg':'Can not delete others'}, 400
        if self.user.role == 'librarian':
            return {'msg':'Can not delete librarian'}, 400
        db.session.delete(self.user); db.session.commit()
        jti = get_jwt()['jti']
        BLOCKLIST.add(jti)
        return {'msg':'Account deleted and token revoked'}, 200
api.add_resource(UserResource,'/api/users/<int:user_id>')