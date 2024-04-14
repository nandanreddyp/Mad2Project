from flask import request
from flask_restful import Resource
from sqlalchemy import and_, exists, insert
from flask_jwt_extended import jwt_required

from resources import api
from database import db, Author, Book, book_author_association
from .rbac import access_for



class AuthorResource(Resource): #✅
    @jwt_required()
    def __init__(self):
        pass
    def get(self, author_id=None):
        if author_id:
            author = Author.query.get(author_id)
            if author: return author.to_dict()
            return {'msg':'Author Not Found'}, 404
        # BUILDING QUERY
        result = Author.query
        query = request.args.get('query','').strip()
        filter = request.args.get('filter','').strip()
        # APPLYING QUERY
        if query: 
            msg = f"Showing results for '{query}'"
            result = result.filter(Author.name.ilike('%'+query.lower()+'%'))
        # APPLYING FILTER
        if filter :
            if query: msg+=', with filter applied'
            else: msg = 'Applied filter'
            sort = request.args.get('sort')
            if sort == 'newest':
                result = result.order_by(Author.created_datetime.desc())
            if sort == 'oldest':
                result = result.order_by(Author.created_datetime.asc())
            if sort == 'alpha-asc':
                result = result.order_by(Author.name.asc())
            if sort == 'alpha-desc':
                result = result.order_by(Author.name.desc())
        # DEFAULT FILTER
        if not query and not filter:
            msg = 'Recently added Authors'
            result = result.order_by(Author.created_datetime.desc()) # default soring
        page = request.args.get('page',1,type=int); per_page = request.args.get('per_page',3,type=int)
        pagination = result.paginate(page=page, per_page=per_page)
        page_data = {'current_page': pagination.page,'next_page': pagination.next_num,'has_next': pagination.has_next,'has_prev': pagination.has_prev,'per_page': pagination.per_page,'current_page_count': len(pagination.items),'total_items':pagination.total}
        authors = [author.to_dict() for author in pagination.items]
        results = {'msg':msg,'page_data':page_data,'authors':authors}
        return results, 200
    @access_for(['librarian'])
    def post(self, author_id=None): #admin
        if author_id: return {'msg':"Can't post with id"}, 400
        if not request.is_json: return {'msg':'Missing JSON in request'}, 400
        data = request.json
        if not data: return {'msg':'No data provided'}, 400
        try:
            name = data.get('name','').strip() or None
            if not name: raise ValueError('Name can not be empty')
            description = data.get('description','').strip() or None
            img_path = data.get('img_path','').strip() or None
        except ValueError as e: return {'msg':str(e)}, 400
        except: return {'msg':'Make sure all fileds are given and they are in correct format.'}, 400
        author = Author(
            name = name, description = description, img_path = img_path
        )
        db.session.add(author)
        db.session.commit()
        return {'msg':f"Author created",'id':author.id}, 200
    @access_for(['librarian'])
    def put(self, author_id): #admin
        if not request.is_json: return {'msg':'Missing JSON in request'}, 400
        data = request.json; author = Author.query.get(author_id)
        if not data: return {'msg':'No data provided'}, 400
        if not author: return {'msg':f'Author not found'}, 404
        try:
            name = data.get('name','').strip() or None; 
            if not name: raise ValueError("Name can't be empty")
            description = data.get('description','').strip() or None; 
            img_path = data.get('img_path','').strip() or None
        except ValueError as e: return {'msg':str(e)}, 400
        except: return {'msg':'Make sure all fileds are given and they are in correct format.'}, 400
        if name :
            author.name = name
            author.description = description
            if img_path: author.img_path = img_path
            else:        author.set_default_img_path()
            db.session.commit()
            return {'msg':f'Author updated','id':author_id}, 200
        return {'msg':"Name of author can't be empty"},400
    @access_for(['librarian'])
    def delete(self, author_id): #admin
        author = Author.query.get(author_id)
        if author:
            db.session.delete(author)
            db.session.commit()
            return {'msg':f'Deleted author'}, 200
        return {'msg':f'Author not found'}, 404
api.add_resource(AuthorResource,
                 '/api/authors',
                 '/api/authors/<int:author_id>')

class AuthorBook(Resource): #✅
    def __init__(self):
        pass
    def get(self, author_id, book_id=None):
        author = Author.query.get(author_id); 
        if not author: return {'msg':f"Author not found"}, 404
        if book_id: # check if association exists
            book = Book.query.get(book_id)
            if not book: return {'msg':f"book not found"}, 404
            is_associated = db.session.query(
                exists().where(and_(
                    book_author_association.c.author_id == author_id,
                    book_author_association.c.book_id == book_id,
                ))).scalar()
            if is_associated: return {'msg':"Association Found",'is_associated':True}, 200
            return {'msg':f"Assocaitaion Not Found",'is_associated':False}, 404
        # BUILDING QUERY
        result = Book.query.join(book_author_association).filter(book_author_association.c.author_id == author_id)
        # APPLYING QUERY
        query = request.args.get('query')
        filter = request.args.get('filter')
        if query:
            msg = f"Showing results for '{query}'"
            result = result.filter(Book.name.ilike('%'+query.lower()+'%'))
        # APPLYING FILTER
        if filter:
            if query: msg+=', with filter applied'
            else: msg = 'Applied filter'
            sort = request.args.get('sort')
            if sort == 'oldest':
                result = result.order_by(Book.created_datetime.asc())
            if sort == 'newest':
                result = result.order_by(Book.created_datetime.desc())
            if sort == 'alpha-asc':
                result = result.order_by(Book.name.asc())
            if sort == 'alpha-desc':
                result = result.order_by(Book.name.desc())
        # DEFAULT FILTER
        if not query and not filter:
            msg = f'Recent book'
            result.order_by(Book.created_datetime.desc()) # apply default sorting
        # Pagination parameters
        page = request.args.get('page',1,type=int); per_page = request.args.get('per_page',3,type=int)
        pagination = result.paginate(page=page, per_page=per_page)
        page_data = {'current_page': pagination.page,'next_page': pagination.next_num,'has_next': pagination.has_next,'has_prev': pagination.has_prev,'per_page': pagination.per_page,'current_page_count': len(pagination.items),'total_items':pagination.total}
        books = [book.to_dict() for book in pagination.items]
        # RESULTS
        results = {'msg':msg,'page_data':page_data,'books':books}
        return results, 200
    @access_for(['librarian'])
    def post(self, author_id, book_id):
        author = Author.query.get(author_id); book = Book.query.get(book_id)
        if not author: return {'msg':f"Author not found with id '{author_id}'"}, 404
        if not book: return {'msg':f"Book not found with id {book_id}"}, 404
        is_associated = is_associated = db.session.query(
            exists().where(and_(book_author_association.c.author_id == author_id, 
                                book_author_association.c.book_id == book_id))).scalar()
        if is_associated: return {'msg':'Association found'}, 200
        # Add the association to the association table
        db.session.execute(
            insert(book_author_association).values(author_id=author_id, book_id=book_id)
        )
        db.session.commit()
        return {'msg':'Book associated to Author'}, 200
    @access_for(['librarian'])
    def delete(self, author_id, book_id):
        author = Author.query.get(author_id); book = Book.query.get(book_id)
        if not author: return {'msg':f"Author not found"}, 404
        if not book: return {'msg':f"Book not found"}, 404
        # Check if the book is associated with the author in the database
        is_associated = is_associated = db.session.query(
            exists().where(and_(book_author_association.c.author_id == author_id, 
                                book_author_association.c.book_id == book_id))).scalar()
        if not is_associated: return {'msg':'Association not found'}, 200
        # Remove the association from the association table
        association = book_author_association.delete().where(
            (book_author_association.c.author_id == author_id) &
            (book_author_association.c.book_id == book_id)
        )
        db.session.execute(association); db.session.commit()
        return {'msg': f"Book dissociated from Author"}, 200
api.add_resource(AuthorBook,
                 '/api/authors/<int:author_id>/books',
                 '/api/authors/<int:author_id>/books/<int:book_id>')