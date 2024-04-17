from flask import request
from flask_restful import Resource
from sqlalchemy import and_, exists, insert
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

from resources import api
from database import db, User, Book, Section, Author, Rating, Request, Issue, book_author_association, book_section_association
from functions import convert_str_to_date
from .rbac import access_for

from .fileHandle import bookImage, bookPdf


class BookResource(Resource): #final
    @jwt_required()
    def __init__(self):
        pass
    def get(self, book_id=None):
        if book_id:
            book = Book.query.get(book_id)
            if book: return {'book':book.to_dict()}, 200 
            return {'msg':'Book Not Found'}, 404
        # BUILDING QUERY
        result = Book.query
        query = request.args.get('query','')
        sort = request.args.get('sort','')
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
        msg = 'Successfully fetced Books'
        page = request.args.get('page',1,type=int); per_page = request.args.get('per_page',3,type=int)
        pagination = result.paginate(page=page, per_page=per_page)
        page_data = {'current_page': pagination.page,'next_page': pagination.next_num,'has_next': pagination.has_next,'has_prev': pagination.has_prev,'per_page': pagination.per_page,'current_page_count': len(pagination.items),'total_items':pagination.total}
        books = [book.to_dict() for book in pagination.items]
        results = {'msg':msg,'page_data':page_data,'books':books}
        return results, 200
    @access_for(['librarian'])
    def post(self, book_id=None):
        if book_id: return {'msg':"Can't post with id"}, 400
        data = request.form; files = request.files
        try: 
            name = data.get('name','').strip() or None
            if not name: raise ValueError('Name can not be empty')
            description = data.get('description','').strip() or None
            page_count = data.get('page_count') or None # int
            if page_count:
                try: page_count = int(page_count)
                except: raise ValueError('Page count should be integer or int in string')
            publication_date = data.get('publication_date') or None # date
            if publication_date: publication_date = convert_str_to_date(publication_date)
            isbn = data.get('isbn') or None # int
            if isbn:
                try: isbn = int(isbn)
                except: raise ValueError('ISBN should be integer or int in string')
        except ValueError as e: return {'msg':str(e)}, 400
        except: return {'msg':'Make sure all fileds are given and they are in correct format.'}, 400
        pdf_file = files.get('pdf_file')
        if pdf_file: pdf_path = bookPdf().save(pdf_file)
        else: pdf_path = None
        img_file = files.get('image_file')
        if img_file: img_path = bookImage().save(img_file)
        else: img_path = None
        book = Book(
            name = name, description = description,
            page_count = page_count, publication_date = publication_date,
            isbn = isbn,
            img_path = img_path, pdf_path = pdf_path
        )
        db.session.add(book)
        db.session.commit()
        return {'msg':'Book created','id':book.id},200
    @access_for(['librarian'])
    def put(self, book_id=None):
        if not book_id: return {'msg':'Book id is required'}, 400
        book = Book.query.get(book_id)
        if not book: return {'msg':f'Book not found'}, 404
        data = request.form; files = request.files
        try:
            name = data.get('name','').strip() or None
            description = data.get('description','').strip() or None
            page_count = data.get('page_count') or None # int
            if page_count:
                try: page_count = int(page_count)
                except: raise ValueError('Page count should be integer or int in string')
            publication_date = data.get('publication_date') or None # date
            if publication_date: publication_date = convert_str_to_date(publication_date)
            isbn = data.get('isbn') or None # int
            if isbn:
                try: isbn = int(isbn)
                except: raise ValueError('ISBN should be integer or int in string')
        except ValueError as e: return {'msg':str(e)},400
        except: return {'msg':'Make sure all fields are given and they are in correct format.'}, 400
        pdf_file = files.get('pdf_file')
        if pdf_file: pdf_path = bookPdf().update(book.pdf_path,pdf_file)
        else: pdf_path = None
        img_file = files.get('image_file')
        if img_file: img_path = bookImage().update(book.img_path,img_file)
        else: img_path = None
        # udpate values
        book.name = name
        book.description = description
        book.page_count = page_count
        book.publication_date = publication_date
        book.isbn = isbn
        if img_path: book.img_path = img_path
        if pdf_path: book.pdf_path = pdf_path
        db.session.commit()
        return {'msg':'Book updated','id':book_id}, 200
    @access_for(['librarian'])
    def delete(self, book_id=None):
        if not book_id: return {'msg':'Book id is required'}, 400
        book = Book.query.get(book_id)
        if not book: return {'msg':'Book not found'}, 404
        bookImage().delete(book.img_path)
        bookPdf().delete(book.pdf_path)
        db.session.delete(book); db.session.commit()
        return {'msg':'Deleted book'}, 200
api.add_resource(BookResource,
                 '/api/books',
                 '/api/books/<int:book_id>')



class BookSection(Resource):
    @jwt_required()
    def __init__(self):
        pass
    def get(self, book_id, section_id=None):
        book = Book.query.get(book_id)
        if not book: return {'msg':f"Book not found"}, 404
        if section_id: # check if association exists
            section = Section.query.get(section_id)
            if not section: return {'msg':f"section not found"}, 404
            is_associated = db.session.query(
                exists().where(and_(
                    book_section_association.c.book_id == book_id,
                    book_section_association.c.section_id == section_id,
                ))).scalar()
            if is_associated: return {'msg':"Association Found",'is_associated':True}, 200
            return {'msg':f"Assocaitaion Not Found",'is_associated':False}, 200
        # BUILDING QUERY
        result = Section.query.join(book_section_association).filter(book_section_association.c.book_id == book_id)
        query = request.args.get('query','')
        sort = request.args.get('sort','')
        # APPLYING QUERY
        if query:
            result = result.filter(Section.name.ilike('%'+query.lower()+'%'))
        # APPLYING FILTER
        if sort:
            if sort == 'newest':
                result = result.order_by(Section.created_datetime.desc())
            elif sort == 'oldest':
                result = result.order_by(Section.created_datetime.asc())
            elif sort == 'asc':
                result = result.order_by(Section.name.asc())
            elif sort == 'desc':
                result = result.order_by(Section.name.desc())
        # DEFAULT FILTER
        # DEFAULT FILTER
        if not query and not sort:
            result = result.order_by(Section.created_datetime.desc()) # default sorting
        msg = 'Successfully fetced Books'
        page = request.args.get('page',1,type=int); per_page = request.args.get('per_page',3,type=int)
        pagination = result.paginate(page=page, per_page=per_page)
        page_data = {'current_page': pagination.page,'next_page': pagination.next_num,'has_next': pagination.has_next,'has_prev': pagination.has_prev,'per_page': pagination.per_page,'current_page_count': len(pagination.items),'total_items':pagination.total}
        sections = [section.to_dict() for section in pagination.items]
        results = {'msg':msg,'page_data':page_data,'sections':sections}
        return results, 200
    @access_for(['librarian'])
    def post(self, book_id, section_id):
        book = Book.query.get(book_id); section = Section.query.get(section_id)
        if not book: return {'msg':f"Book not found with id '{book_id}'"}, 404
        if not section: return {'msg':f"Section not found with id {section_id}"}, 404
        is_associated = is_associated = db.session.query(
            exists().where(and_(book_section_association.c.book_id == book_id, 
                                book_section_association.c.section_id == section_id))).scalar()
        if is_associated: return {'msg':'Association found'}, 200
        # Add the association to the association table
        db.session.execute(
            insert(book_section_association).values(book_id=book_id, section_id=section_id)
        )
        db.session.commit()
        return {'msg':'Section associated to Book'}, 200
    @access_for(['librarian'])
    def delete(self, book_id, section_id):
        book = Book.query.get(book_id); section = Section.query.get(section_id)
        if not book: return {'msg':f"Book not found"}, 404
        if not section: return {'msg':f"Section not found"}, 404
        # Check if the section is associated with the book in the database
        is_associated = is_associated = db.session.query(
            exists().where(and_(book_section_association.c.book_id == book_id, 
                                book_section_association.c.section_id == section_id))).scalar()
        if not is_associated: return {'msg':'Association not found'}, 200
        # Remove the association from the association table
        association = book_section_association.delete().where(
            (book_section_association.c.book_id == book_id) &
            (book_section_association.c.section_id == section_id)
        )
        db.session.execute(association); db.session.commit()
        return {'msg': f"Section dissociated from Book"}, 200
api.add_resource(BookSection,
                 '/api/books/<int:book_id>/sections',
                 '/api/books/<int:book_id>/sections/<int:section_id>')



class BookAuthor(Resource):
    @jwt_required()
    def __init__(self):
        pass
    def get(self, book_id, author_id=None):
        book = Book.query.get(book_id); 
        if not book: return {'msg':f"Book not found"}, 400
        if author_id: # check if association exists
            author = Author.query.get(author_id)
            if not author: return {'msg':f"author not found"}, 400
            is_associated = db.session.query(
                exists().where(and_(
                    book_author_association.c.book_id == book_id,
                    book_author_association.c.author_id == author_id,
                ))).scalar()
            if is_associated: return {'msg':"Association Found",'is_associated':True}, 200
            return {'msg':f"Assocaitaion Not Found",'is_associated':False}, 404
        # BUILDING QUERY
        result = Author.query.join(book_author_association).filter(book_author_association.c.book_id == book_id)
        # APPLYING QUERY
        query = request.args.get('query')
        filter = request.args.get('filter')
        if query:
            msg = f"Showing results for '{query}'"
            result = result.filter(Author.name.ilike('%'+query.lower()+'%'))
        # APPLYING FILTER
        if filter:
            if query: msg+=', with filter applied'
            else: msg = f'Applied filter'
            result = result
        # DEFAULT FILTER
        if not query and not filter:
            msg = f'Recently added authors'
            result.order_by(Author.created_datetime.desc()) # apply default sorting
        # Pagination parameters
        page = request.args.get('page',1,type=int); per_page = request.args.get('per_page',3,type=int)
        pagination = result.paginate(page=page, per_page=per_page)
        page_data = {'current_page': pagination.page,'next_page': pagination.next_num,'has_next': pagination.has_next,'has_prev': pagination.has_prev,'per_page': pagination.per_page,'current_page_count': len(pagination.items),'total_items':pagination.total}
        authors = [author.to_dict() for author in pagination.items]
        # RESULTS
        results = {'msg':msg,'page_data':page_data,'authors':authors}
        return results, 200
    @access_for(['librarian'])
    def post(self, book_id, author_id):
        book = Book.query.get(book_id); author = Author.query.get(author_id)
        if not book: return {'msg':f"Book not found with id '{book_id}'"}, 404
        if not author: return {'msg':f"Author not found with id {author_id}"}, 404
        is_associated = is_associated = db.session.query(
            exists().where(and_(book_author_association.c.book_id == book_id, 
                                book_author_association.c.author_id == author_id))).scalar()
        if is_associated: return {'msg':'Association found'}, 200
        # Add the association to the association table
        db.session.execute(
            insert(book_author_association).values(book_id=book_id, author_id=author_id)
        )
        db.session.commit()
        return {'msg':'Author associated to Book'}, 200
    @access_for(['librarian'])
    def delete(self, book_id, author_id):
        book = Book.query.get(book_id); author = Author.query.get(author_id)
        if not book: return {'msg':f"Book not found"}, 404
        if not author: return {'msg':f"Author not found"}, 404
        # Check if the author is associated with the book in the database
        is_associated = is_associated = db.session.query(
            exists().where(and_(book_author_association.c.book_id == book_id, 
                                book_author_association.c.author_id == author_id))).scalar()
        if not is_associated: return {'msg':'Association not found'}, 200
        # Remove the association from the association table
        association = book_author_association.delete().where(
            (book_author_association.c.book_id == book_id) &
            (book_author_association.c.author_id == author_id)
        )
        db.session.execute(association); db.session.commit()
        return {'msg': f"Author dissociated from Book"}, 200
api.add_resource(BookAuthor,
                 '/api/books/<int:book_id>/authors',
                 '/api/books/<int:book_id>/authors/<int:author_id>')



class BookRequest(Resource):
    @jwt_required()
    def __init__(self):
        self.user = User.query.filter_by(email = get_jwt_identity()).first()
    def get(self, book_id):
        book = Book.query.get(book_id)
        if not book: return {'msg':'Book not found'}, 400
        requested = False
        request = Request.query.filter_by(book_id=book_id,user_id=self.user.id).first()
        if request: requested = True
        return {'requested':requested}, 200
api.add_resource(BookRequest,'/api/books/<int:book_id>/request')



class BookIssue(Resource):
    @jwt_required()
    def __init__(self):
        self.user = User.query.filter_by(email = get_jwt_identity()).first()
    def get(self, book_id):
        book = Book.query.get(book_id)
        if not book: return {'msg':'Book not found'}, 400
        allowed = False
        issue = Issue.query.filter_by(book_id=book_id,user_id=self.user.id).first()
        if issue: allowed = True
        return {'allowed':allowed}, 200
api.add_resource(BookIssue,'/api/books/<int:book_id>/issue')



class BookRating(Resource):
    @jwt_required()
    def __init__(self):
        self.user = User.query.filter_by(email=get_jwt_identity()).first()
    def get(self, book_id, rating_id=None):
        book = Book.query.get(book_id); user_id = request.args.get('user_id',type=int)
        if not book: return {'msg':f"Book not found"}, 400
        if rating_id:
            rating = Rating.query.get(rating_id)
            if rating: return {'msg':'Found rating', 'rating':rating.to_dict()}, 200
            else: return {'msg':'Rating not found'}, 404
        if user_id:
            book_rating = Rating.query.filter_by(user_id=user_id,book_id=book_id).first()
            if book_rating: return {'msg':'Rating found', 'rating':book_rating.to_dict()}, 200
            return {'msg':'Rating not found'},  404
        # BUILDING QUERY
        result = Rating.query.filter_by(book_id=book_id)
        # APPLYING FILTER
        filter = request.args.get('filter')
        if filter:
            msg = 'Applied filter'
            result = result
        # DEFAULT FILTER
        if not filter:
            msg = "Recently added reviews"
            result.order_by(Rating.created_datetime.desc())
        # PAGINATION params
        page = request.args.get('page',1,type=int); per_page = request.args.get('per_page',3,type=int)
        pagination = result.paginate(page=page, per_page=per_page)
        page_data = {'current_page': pagination.page,'next_page': pagination.next_num,'has_next': pagination.has_next,'has_prev': pagination.has_prev,'per_page': pagination.per_page,'current_page_count': len(pagination.items),'total_items':pagination.total}
        reviews = [review.to_dict() for review in pagination.items]
        # RESULTS
        results = {'msg':msg, 'page_data':page_data, 'reviews':reviews}
        return results, 200
    def post(self, book_id, rating_id=None):
        if rating_id: return {'msg':"Can't post with id"}, 400
        book = Book.query.get(book_id); 
        if not book: return {'msg':f"Book not found"}, 400
        rating = Rating.query.filter_by(book_id=book_id, user_id=self.user.id).first()
        if rating: return {'msg':'Your Rating exists'}, 400
        if not request.is_json: return {'msg':'Missing JSON in request'}, 400
        data = request.json
        if not data: return {'msg':'No data provided'}, 400
        try:
            rating = data.get('rating') or None # int
            if rating:
                try: rating = int(rating)
                except: raise ValueError('Rating should be integer or int in string')
            else: return {'msg':'Rating is required'}, 400
            description = data.get('description','').strip() or None
        except ValueError as e: return {'msg':str(e)}, 400
        except: return {'msg':"Make sure all fields are given and they are in correct format."}, 400
        rating = Rating(
            book_id = book_id, user_id = self.user.id,
            rating = rating, description = description
        )
        db.session.add(rating); db.session.commit()
        return {'msg':'Rating created','id':rating.id}, 200
    def put(self, book_id, rating_id):
        book = Book.query.get(book_id); rating = Rating.query.get(rating_id)
        if not book: return {'msg':f"Book not found"}, 404
        if not rating: return {'msg':f"Rating not found"}, 404
        if not rating.user.id == self.user.id: return {'msg':'Not your review to edit'}
        if not request.is_json: return {'msg':'Missing JSON in request'}, 400
        data = request.json
        if not data: return {'msg':'No data provided'}, 400
        try:
            rating = data.get('rating') or None # int
            if rating:
                try: rating = int(rating)
                except: raise ValueError('Rating should be integer or int in string')
            else: return {'msg':'Rating is required'}, 400
            description = data.get('description','').strip() or None
        except ValueError as e: return {'msg':str(e)}, 400
        except: return {'msg':"Make sure all fields are given and they are in correct format."}, 400
        rating.rating = rating; rating.description = description
        db.session.commit()
        return {'msg':"Updated review"}, 200
    def delete(self, book_id, rating_id=None):
        if rating_id is None: return {'msg': 'Rating ID is required'}, 400
        rating = Rating.query.get(rating_id)
        if not rating: return {'msg':'Rating not exists'}
        if rating.book_id == book_id and rating.user_id == self.user.id:
            db.session.delete(rating); db.session.commit()
            return {'msg':'Rating deleted'}, 200
        return {'msg':'You can not delete others reivews'}, 400
api.add_resource(BookRating,
                 '/api/books/<int:book_id>/ratings',
                 '/api/books/<int:book_id>/ratings/<int:rating_id>')
