from flask import request
from flask_restful import Resource
from sqlalchemy import and_, exists, insert
from flask_jwt_extended import jwt_required

from resources import api
from database import db, Section, Book, book_section_association
from .rbac import access_for

from .fileHandle import sectionImage


class SectionResource(Resource): #✅
    @jwt_required()
    def __init__(self):
        pass
    def get(self, section_id=None):
        if section_id:
            section = Section.query.get(section_id)
            if section: return {'section':section.to_dict()}
            return {'msg':'Section Not Found'}, 404
        # BUILDING QUERY
        result = Section.query
        query = request.args.get('query')
        sort = request.args.get('sort')
        # APPLYING QUERY
        if query:
            result = result.filter(Section.name.ilike("%"+query.lower()+"%"))
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
        # default filter
        if not query and not sort:
            result = result.order_by(Section.created_datetime.desc()) # default sorting
        msg = "Successfully etched sections"
        page = request.args.get('page',1,type=int); per_page = request.args.get('per_page',3,type=int)
        pagination = result.paginate(page=page, per_page=per_page)
        page_data = {'current_page': pagination.page,'next_page': pagination.next_num,'has_next': pagination.has_next,'has_prev': pagination.has_prev,'per_page': pagination.per_page,'current_page_count': len(pagination.items),'total_items':pagination.total}
        sections = [secion.to_dict() for secion in pagination.items]
        results = {'msg':msg,'page_data':page_data,'sections':sections}
        return results, 200
    @access_for(['librarian'])
    def post(self, section_id=None):
        if section_id: return {'msg':"Can't post with id"}, 400
        data = request.form; files = request.files
        try:
            name = data.get('name') or None
            if not name: raise ValueError('Name can not be empty')
            description = data.get('description') or None
            img_path = data.get('img_path') or None
        except ValueError as e: return {'msg':str(e)}, 400
        except: return {'msg':'Make sure all fileds are given and they are in correct format.'}, 400
        img_file = files.get('image_file')
        if img_file: img_path = sectionImage().save(img_file)
        else: img_path = None
        section = Section(
            name = name, description = description, img_path = img_path
        )
        db.session.add(section)
        db.session.commit()
        return {'msg':f"Section created",'id':section.id}, 200
    @access_for(['librarian'])
    def put(self, section_id=None):
        if not section_id: return {'msg':'section id is required'}, 400
        section = Section.query.get(section_id)
        if not section: return {'msg':f'section not found'}, 404
        data = request.form; files = request.files
        try:
            name = data.get('name')or None
            if not name: raise ValueError("Name can't be empty")
            description = data.get('description') or None
        except ValueError as e: return {'msg':str(e)}, 400
        except: return {'msg':'Make sure all fileds are given and they are in correct format.'}, 400
        img_file = files.get('image_file')
        if img_file: img_path = sectionImage().update(section.img_path,img_file)
        else: img_path = None
        # update values
        section.name = name
        section.description = description
        if img_path: section.img_path = img_path
        db.session.commit()
        return {'msg':'Section updated','id':section_id}, 200
    @access_for(['librarian'])
    def delete(self, section_id):
        section = Section.query.get(section_id)
        if not section: return {'msg':'Section not found'}, 404
        sectionImage().delete(section.img_path)
        db.session.delete(section)
        db.session.commit()
        return {'msg':'Deleted section'}, 200
api.add_resource(SectionResource,
                 '/api/sections',
                 '/api/sections/<int:section_id>')



class SectionBook(Resource): # show books of section
    @jwt_required()
    def __init__(self):
        pass
    def get(self, section_id, book_id=None):
        section = Section.query.get(section_id); 
        if not section: return {'msg':f"Section not found"}, 404
        if book_id: return {'msg':'not required book id'}, 400
        # BUILDING QUERY
        result = Book.query.join(book_section_association).filter(book_section_association.c.section_id == section_id)
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
        msg = 'fetched section books'
        page = request.args.get('page',1,type=int); per_page = request.args.get('per_page',3,type=int)
        pagination = result.paginate(page=page, per_page=per_page)
        page_data = {'current_page': pagination.page,'next_page': pagination.next_num,'has_next': pagination.has_next,'has_prev': pagination.has_prev,'per_page': pagination.per_page,'current_page_count': len(pagination.items),'total_items':pagination.total}
        books = [book.to_dict() for book in pagination.items]
        # RESULTS
        results = {'msg':msg,'page_data':page_data,'books':books}
        return results, 200
api.add_resource(SectionBook,
                 '/api/sections/<int:section_id>/books',)


class SectionAddBooks(Resource):
    @jwt_required()
    def __init__(self):
        pass
    @access_for(['librarian'])
    def get(self, section_id):
        section = Section.query.get(section_id)
        if not section: return {'msg':'Section Not Found'}, 404
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
        msg = 'Successfully fetced books with or without association to section'
        page = request.args.get('page',1,type=int); per_page = request.args.get('per_page',3,type=int)
        pagination = result.paginate(page=page, per_page=per_page)
        page_data = {'current_page': pagination.page,'next_page': pagination.next_num,'has_next': pagination.has_next,'has_prev': pagination.has_prev,'per_page': pagination.per_page,'current_page_count': len(pagination.items),'total_items':pagination.total}
        books = [book.to_dict() for book in pagination.items]
        for book in books:
            is_associated = db.session.query(
                exists().where(and_(
                    book_section_association.c.section_id == section_id,
                    book_section_association.c.book_id == book['id'],
                ))).scalar()
            book['is_associated'] = is_associated
        results = {'msg':msg,'page_data':page_data,'books':books}
        return results, 200
    @access_for(['librarian'])
    def post(self, section_id, book_id):
        section = Section.query.get(section_id); book = Book.query.get(book_id)
        if not section: return {'msg':f"Section not found with id '{section_id}'"}, 404
        if not book: return {'msg':f"Book not found with id {book_id}"}, 404
        is_associated = is_associated = db.session.query(
            exists().where(and_(book_section_association.c.section_id == section_id, 
                                book_section_association.c.book_id == book_id))).scalar()
        if is_associated: return {'msg':'Association found'}, 200
        # Add the association to the association table
        db.session.execute(
            insert(book_section_association).values(section_id=section_id, book_id=book_id)
        )
        db.session.commit()
        return {'msg':'Book associated to Section'}, 200
    @access_for(['librarian'])
    def delete(self, section_id, book_id):
        section = Section.query.get(section_id); book = Book.query.get(book_id)
        if not section: return {'msg':f"Section not found"}, 404
        if not book: return {'msg':f"Book not found"}, 404
        # Check if the book is associated with the section in the database
        is_associated = is_associated = db.session.query(
            exists().where(and_(book_section_association.c.section_id == section_id, 
                                book_section_association.c.book_id == book_id))).scalar()
        if not is_associated: return {'msg':'Association not found'}, 200
        # Remove the association from the association table
        association = book_section_association.delete().where(
            (book_section_association.c.section_id == section_id) &
            (book_section_association.c.book_id == book_id)
        )
        db.session.execute(association); db.session.commit()
        return {'msg': f"Book dissociated from Section"}, 200
    
api.add_resource(SectionAddBooks,
                 '/api/sections/<int:section_id>/add/books',
                 '/api/sections/<int:section_id>/add/books/<int:book_id>')