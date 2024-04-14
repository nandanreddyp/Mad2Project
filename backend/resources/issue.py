from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from resources import api

from database import db, Book, Issue, User
from .rbac import access_for



class IssueResource(Resource): #✅
    @jwt_required()
    def __init__(self):
        self.user = User.query.filter_by(email=get_jwt_identity()).first()
    @access_for(['librarian'])
    def get(self, issue_id=None):
        issues = Issue.query.filter_by(user_id=self.user.id).all()
        issues = [issue.to_dict() for issue in issues]
        return {'issues':issues}, 200
    @access_for(['librarian'])
    def delete(self, issue_id=None): #admin
        if not issue_id: return {'msg':'issue id is requried'}, 400
        issue = Issue.query.get(issue_id)
        if not issue: return {'msg':'issue not found'}, 404
        db.session.remove(issue)
        db.session.commit()
        return {'msg','Deleted issue'}, 200
api.add_resource(IssueResource,
                 '/api/issues',
                 '/api/issues/<int:issue_id>')