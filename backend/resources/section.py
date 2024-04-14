from flask import request
from flask_restful import Resource
from sqlalchemy import and_, exists, insert
from flask_jwt_extended import jwt_required

from resources import api
from database import db, Section, Book, book_section_association
from .rbac import access_for



class SectionResource(Resource): #✅
    @jwt_required()
    def __init__(self):
        pass
    def get(self, section_id=None):
        if section_id:
            section = Section.query.get(section_id)
            if section: return section.to_dict()
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
        sections = [section.to_dict() for section in result]
        print(len(sections))
        results = {'msg':msg,'sections':sections}
        return results, 200
    @access_for(['librarian'])
    def post(self, section_id=None):
        if section_id: return {'msg':"Can't post with id"}, 400
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
        if name:
            section = Section(
                name = name, description = description, img_path = img_path
            )
            db.session.add(section)
            db.session.commit()
            return {'msg':f"Section created",'id':section.id}, 200
        return {'msg':"Name of section can't be empty"},400
    @access_for(['librarian'])
    def put(self, section_id=None):
        if not section_id: return {'msg':'section id is required'}, 400
        if not request.is_json: return {'msg':'Missing JSON in request'}, 400
        data = request.json; section = Section.query.get(section_id)
        if not data: return {'msg':'No data provided'}, 400
        if not section: return {'msg':f'Section not found'}, 404
        try:
            name = data.get('name','').strip() or None
            if not name: raise ValueError("Name can't be empty")
            description = data.get('description','').strip() or None; 
            img_path = data.get('img_path','').strip() or None
        except ValueError as e: return {'msg':str(e)}, 400
        except: return {'msg':'Make sure all fileds are given and they are in correct format.'}, 400
        # update section values
        section.name = name
        section.description = description
        if img_path: section.img_path = img_path
        else:        section.set_default_img_path()
        db.session.commit()
        return {'msg':'Section updated','id':section_id}, 200
    @access_for(['librarian'])
    def delete(self, section_id):
        section = Section.query.get(section_id)
        if section:
            db.session.delete(section)
            db.session.commit()
            return {'msg':'Deleted section'}, 200
        return {'msg':'Section not found'}, 404
api.add_resource(SectionResource,
                 '/api/sections',
                 '/api/sections/<int:section_id>')



class SectionBook(Resource): #✅
    @jwt_required()
    def __init__(self):
        pass
    def get(self, section_id, book_id=None):
        section = Section.query.get(section_id); 
        if not section: return {'msg':f"Section not found"}, 404
        if book_id: # check if association exists
            book = Book.query.get(book_id)
            if not book: return {'msg':f"book not found"}, 404
            is_associated = db.session.query(
                exists().where(and_(
                    book_section_association.c.section_id == section_id,
                    book_section_association.c.book_id == book_id,
                ))).scalar()
            if is_associated: return {'msg':"Association Found",'is_associated':True}, 200
            return {'msg':f"Assocaitaion Not Found",'is_associated':False}, 200
        # BUILDING QUERY
        result = Book.query.join(book_section_association).filter(book_section_association.c.section_id == section_id)
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
            result = result
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
    # @access_for(['librarian'])
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
    # @access_for(['librarian'])
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
api.add_resource(SectionBook,
                 '/api/sections/<int:section_id>/books',
                 '/api/sections/<int:section_id>/books/<int:book_id>')
        