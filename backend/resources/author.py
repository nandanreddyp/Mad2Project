from flask import request
from flask_restful import Resource
from sqlalchemy import and_, exists, insert
from flask_jwt_extended import jwt_required

from resources import api
from database import db, Author, Book, book_author_association
from .rbac import access_for

from.fileHandle import authorImage



class AuthorResource(Resource): #final
    @jwt_required()
    def __init__(self):
        pass
    def get(self, author_id=None):
        if author_id:
            author = Author.query.get(author_id)
            if author: return {'author':author.to_dict()}, 200
            return {'msg':'Author Not Found'}, 404
        # BUILDING QUERY
        result = Author.query
        query = request.args.get('query','')
        sort = request.args.get('sort','')
        # APPLYING QUERY
        if query:
            result = result.filter(Author.name.ilike('%'+query.lower()+'%'))
        # APPLYING FILTER
        if sort:
            if sort == 'newest':
                result = result.order_by(Author.created_datetime.desc())
            elif sort == 'oldest':
                result = result.order_by(Author.created_datetime.asc())
            elif sort == 'asc':
                result = result.order_by(Author.name.asc())
            elif sort == 'desc':
                result = result.order_by(Author.name.desc())
        # DEFAULT FILTER
        if not query and not sort:
            result = result.order_by(Author.created_datetime.desc()) # default sorting
        msg = 'Successfully fetced Authors'
        page = request.args.get('page',1,type=int); per_page = request.args.get('per_page',3,type=int)
        pagination = result.paginate(page=page, per_page=per_page)
        page_data = {'current_page': pagination.page,'next_page': pagination.next_num,'has_next': pagination.has_next,'has_prev': pagination.has_prev,'per_page': pagination.per_page,'current_page_count': len(pagination.items),'total_items':pagination.total}
        authors = [author.to_dict() for author in pagination.items]
        results = {'msg':msg,'page_data':page_data,'authors':authors}
        return results, 200
    @access_for(['librarian'])
    def post(self, author_id=None): #admin
        if author_id: return {'msg':"Can't post with id"}, 400
        data = request.form; files = request.files
        try:
            name = data.get('name') or None
            if not name: raise ValueError('Name can not be empty')
            description = data.get('description') or None
        except ValueError as e: return {'msg':str(e)}, 400
        except: return {'msg':'Make sure all fileds are given and they are in correct format.'}, 400
        img_file = files.get('image_file')
        if img_file: img_path = authorImage().save(img_file)
        else: img_path = None
        author = Author(
            name = name, description = description, img_path = img_path
        )
        db.session.add(author)
        db.session.commit()
        return {'msg':f"Author created",'id':author.id}, 200
    @access_for(['librarian'])
    def put(self, author_id=None):
        if not author_id: return {'msg':'Author id is required'}, 400
        author = Author.query.get(author_id)
        if not author: return {'msg':f'Author not found'}, 404
        data = request.form; files = request.files
        try:
            name = data.get('name') or None; 
            if not name: raise ValueError("Name can't be empty")
            description = data.get('description') or None
        except ValueError as e: return {'msg':str(e)}, 400
        except: return {'msg':'Make sure all fileds are given and they are in correct format.'}, 400
        img_file = files.get('image_file')
        if img_file: img_path = authorImage().update(author.img_path,img_file)
        else: img_path = None
        # update values
        author.name = name
        author.description = description
        if img_path: author.img_path = img_path
        db.session.commit()
        return {'msg':f'Author updated','id':author_id}, 200
    @access_for(['librarian'])
    def delete(self, author_id):
        author = Author.query.get(author_id)
        if not author: return {'msg':'Author not found'}, 404
        authorImage().delete(author.img_path)
        db.session.delete(author)
        db.session.commit()
        return {'msg':f'Deleted author'}, 200
api.add_resource(AuthorResource,
                 '/api/authors',
                 '/api/authors/<int:author_id>')


class AuthorBook(Resource): # show books of author
    @jwt_required()
    def __init__(self):
        pass
    def get(self, author_id, book_id=None):
        author = Author.query.get(author_id); 
        if not author: return {'msg':f"Author not found"}, 404
        if book_id: return {'msg':'not required book id'}, 400
        # BUILDING QUERY
        result = Book.query.join(book_author_association).filter(book_author_association.c.author_id == author_id)
        # APPLYING QUERY
        query = request.args.get('query')
        sort = request.args.get('sort')
        if query:
            result = result.filter(Book.name.ilike('%'+query.lower()+'%'))
        # APPLYING FILTER
        if sort:
            if sort == 'oldest':
                result = result.order_by(Book.created_datetime.asc())
            if sort == 'newest':
                result = result.order_by(Book.created_datetime.desc())
            if sort == 'alpha-asc':
                result = result.order_by(Book.name.asc())
            if sort == 'alpha-desc':
                result = result.order_by(Book.name.desc())
        # DEFAULT FILTER
        if not query and not sort:
            msg = f'Recent book'
            result.order_by(Book.created_datetime.desc()) # apply default sorting
        # Pagination parameters
        msg = 'fetched author books'
        page = request.args.get('page',1,type=int); per_page = request.args.get('per_page',3,type=int)
        pagination = result.paginate(page=page, per_page=per_page)
        page_data = {'current_page': pagination.page,'next_page': pagination.next_num,'has_next': pagination.has_next,'has_prev': pagination.has_prev,'per_page': pagination.per_page,'current_page_count': len(pagination.items),'total_items':pagination.total}
        books = [book.to_dict() for book in pagination.items]
        # RESULTS
        results = {'msg':msg,'page_data':page_data,'books':books}
        return results, 200
api.add_resource(AuthorBook,
                 '/api/authors/<int:author_id>/books',)


class AuthorAddBooks(Resource):
    @jwt_required()
    def __init__(self):
        pass
    @access_for(['librarian'])
    def get(self, author_id):
        author = Author.query.get(author_id)
        if not author: return {'msg':'Author Not Found'}, 404
        # building query
        result = Book.query
        query = request.args.get('query')
        sort = request.args.get('sort')
        # APPLYING QUERY
        if query:
            result = result.filter(Book.name.ilike('%'+query.lower()+'%'))
        # APPLYING FILTER
        if sort:
            if sort == 'newest':
                result = result.order_by(Book.created_datetime.desc())
            elif sort == 'oldest':
                result = result.order_by(Book.created_datetime.asc())
            elif sort == 'asc':
                result = result.order_by(Book.name.asc())
            elif sort == 'desc':
                result = result.order_by(Book.name.desc())
        # DEFAULT FILTER
        if not query and not sort:
            result = result.order_by(Book.created_datetime.desc()) # default sorting
        msg = 'Successfully fetced books with or without association to author'
        page = request.args.get('page',1,type=int); per_page = request.args.get('per_page',3,type=int)
        pagination = result.paginate(page=page, per_page=per_page)
        page_data = {'current_page': pagination.page,'next_page': pagination.next_num,'has_next': pagination.has_next,'has_prev': pagination.has_prev,'per_page': pagination.per_page,'current_page_count': len(pagination.items),'total_items':pagination.total}
        books = [book.to_dict() for book in pagination.items]
        for book in books:
            is_associated = db.session.query(
                exists().where(and_(
                    book_author_association.c.author_id == author_id,
                    book_author_association.c.book_id == book['id'],
                ))).scalar()
            book['is_associated'] = is_associated
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
    
api.add_resource(AuthorAddBooks,
                 '/api/authors/<int:author_id>/add/books',
                 '/api/authors/<int:author_id>/add/books/<int:book_id>')