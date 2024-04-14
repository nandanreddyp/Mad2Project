from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from resources import api

from database import db, User, Request, Book
from functions import convert_str_to_date
from .rbac import access_for



class UserRequest(Resource): #✅
    @jwt_required()
    def __init__(self):
        self.user = User.query.filter_by(email=get_jwt_identity()).first()
    def get(self, request_id=None):
        result = Request.query.filter_by(user_id = self.user.id)
        pending_requests = []; processed_requests = []
        for request in result:
            request = request.to_dict()
            request['book_name'] = Book.query.get(request['book_id']).name
            if request['status'] == 'pending': pending_requests.append(request)
            else: processed_requests.append(request)
        results = {'msg':'fetched requests','pending_requests':pending_requests,'processed_requests':processed_requests}
        return results, 200
    def post(self, request_id=None):
        if request_id: return {'msg':"Can't post with id"}, 400
        if not request.is_json: return {'msg':'Missing JSON in request'}, 400
        data = request.json
        if not data: return {'msg':'No data provided'}, 400
        try:
            book_id = data.get('book_id','').strip() or None
            if not book_id: raise ValueError('Book id can not be empty')
            end_datetime = data.get('end_datetime').strip() or None
            if end_datetime: end_datetime = convert_str_to_date(end_datetime)
            else: return {'msg':'End date is requried'}, 400
        except ValueError as e: return {'msg':str(e)}, 400
        except: return {'msg':'Make sure all fileds are given and they are in correct format.'}, 400
        if not Book.query.get(book_id): return {'msg':'Book not exists'}, 400
        req = Request(
            user_id = self.user.id, book_id = book_id, end_datetime = end_datetime
        )
        db.session.add(request)
        db.session.commit()
        return {'msg':"Section created",'id':req.id}, 200
    def put(self, request_id=None): # user
        if not request_id: return {'msg':'request id is required'}, 400
        req = Request.query.get(request_id)
        if not req: return {'msg':'request not found'}, 404
        if not request.is_json: return {'msg':'Missing JSON in request'}, 400
        data = request.json
        if not data: return {'msg':'No data provided'}, 400
        try:
            book_id = data.get('book_id','').strip() or None
            if not book_id: raise ValueError('Book id can not be empty')
            end_datetime = data.get('end_datetime').strip() or None
            if end_datetime: end_datetime = convert_str_to_date(end_datetime)
            else: return {'msg':'End date is requried'}, 400
        except ValueError as e: return {'msg':str(e)}, 400
        except: return {'msg':'Make sure all fileds are given and they are in correct format.'}, 400
        if not Book.query.get(book_id): return {'msg':'Book not exists'}, 400
        req.book_id = book_id; req.end_datetime = end_datetime
        db.session.commit()
        return {'msg':'Section updated'}, 200
    def delete(self, request_id = None): # user
        if not request_id: return {'msg':'request id is required'}
        request = Request.query.get(request_id)
        if request:
            db.session.delete(request)
            db.session.commit()
            return {'msg':'Deleted request'}, 200
        return {'msg':'Request not found'}, 404
api.add_resource(UserRequest,
                 '/api/requests',
                 '/api/requests/<int:id>')

class LibrarianRequest(Resource): #✅
    @jwt_required()
    def __init__(self):
        pass
    @access_for(['librarian'])
    def get(self, request_id=None):
        if request_id: return {'msg':'request id is not needed'}, 400
        # BUILDING QUERY
        result = Request.query
        query = request.args.get('query')
        filter = request.args.get('filter')
        if query:
            msg = f"Showing results for '{query}'"
            result = result.filter_by( email = query )
        if filter:
            msg = f"Filtere applied"
            sort = request.args.get('sort')
            if sort == 'newest':
                result = result.order_by(Request.created_datetime.desc())
            if sort == 'oldest':
                result = result.order_by(Request.created_datetime.asc())
        if not query and not filter:
            msg = 'Recently added requests'
            result = result.order_by(Request.created_datetime.desc())
        page = request.args.get('page',1,type=int); per_page = request.args.get('per_page',3,type=int)
        pagination = result.paginate(page=page, per_page=per_page)
        page_data = {'current_page': pagination.page,'next_page': pagination.next_num,'has_next': pagination.has_next,'has_prev': pagination.has_prev,'per_page': pagination.per_page,'current_page_count': len(pagination.items),'total_items':pagination.total}
        requests = [author.to_dict() for author in pagination.items]
        results = {'msg':msg,'page_data':page_data,'requests':requests}
        return results, 200
    @access_for(['librarian'])
    def put(self, request_id=None):
        if not request_id: return {'msg':'request id is required'}, 400
        req = Request.query.get(request_id)
        if not req: return {'msg':'request not found'}, 404
        if not request.is_json: return {'msg':'Missing JSON in request'}, 400
        data = request.json
        if not data: return {'msg':'No data provided'}, 400
        try:
            status = data.get('status')
            if status: 
                try: status = int(status)
                except: raise ValueError('Status update value 0 for reject 1 for accept')
                if not status in [0,1]: return {'msg':'status can only be 0 or 1'}, 400
            else: return {'msg':'Status number is required'}, 400
        except ValueError as e: return {'msg':str(e)}, 400
        except: return {'msg':'Make sure all fileds are given and they are in correct format.'}, 400
        req.update_status(status)
        db.session.commit()
        return {'msg':'Request updated'}, 200
api.add_resource(LibrarianRequest,
                 '/api/librarian/requests',
                 '/api/librarian/requests/<int:request_id>')
