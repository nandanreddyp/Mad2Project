from flask_restful import Resource
from flask_jwt_extended import jwt_required
from resources import api

from .rbac import access_for



class librarianAnalytics(Resource):
    @jwt_required()
    @access_for(['librarian'])
    def get(self):
        return 'image links by storing images in static'
api.add_resource(librarianAnalytics,'/api/librarian/analytics')
