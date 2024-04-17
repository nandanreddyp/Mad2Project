from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from resources import api

from datetime import datetime

from database import db, Book, Issue, User, Request
from .rbac import access_for



class IssueResource(Resource): #✅
    @jwt_required()
    def __init__(self): # list of issues
        self.user = User.query.filter_by(email=get_jwt_identity()).first()
    def get(self, issue_id=None):
        issues = Issue.query.filter_by(user_id=self.user.id).all()
        issues = [issue.to_dict() for issue in issues]
        return {'issues':issues}, 200
    def delete(self, issue_id=None):  #return
        if not issue_id: return {'msg':'issue id is requried'}, 400
        issue = Issue.query.get(issue_id)
        if not issue: return {'msg':'issue not found'}, 404
        db.session.remove(issue)
        db.session.commit()
        return {'msg','Deleted issue'}, 200
api.add_resource(IssueResource,
                 '/api/issues',
                 '/api/issues/<int:issue_id>')

class IsIssued(Resource):
    @jwt_required()
    def __init__(self):
        self.user = User.query.filter(User.email==get_jwt_identity()).first()
    def get(self, book_id=None): # to know weather the book is issued or not
        if not book_id: return {'msg':'book id is requried'}, 400
        active_issue = Issue.query.filter(
            Issue.user_id == self.user.id,
            Issue.book_id == book_id,
            Issue.status == 'active',
            Issue.revoke_datetime > datetime.now()
        ).first()
        active_request = Request.query.filter(
            Request.user_id == self.user.id,
            Request.book_id == book_id,
            Request.status == 'pending',
        )
        if active_issue: return {'issued':True}, 200

        return {'issued':False}, 200
api.add_resource(IsIssued,
                 '/api/issues/books/<int:book_id>')