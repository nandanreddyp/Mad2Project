from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import UniqueConstraint
from datetime import date, datetime

db = SQLAlchemy()


image_domain = 'http://127.0.0.1:5000'

book_author_association = db.Table('book_author_association',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('authors.id'), primary_key=True)
)
book_section_association = db.Table('book_section_association',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('section_id', db.Integer, db.ForeignKey('sections.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String, default='user') # librarian or user
    password = db.Column(db.String)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String)
    last_login = db.Column(db.DateTime, default=datetime.now)
    img_path = db.Column(db.String,default= image_domain+'/static/images/profiles/default.png',nullable=False)
    request_count = db.Column(db.Integer, default=0)
    last_read_book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    created_datetime = db.Column(db.DateTime, default=datetime.now)
    # Define relationships
    requests = db.relationship('Request', backref='user', cascade='all, delete-orphan')
    issues = db.relationship('Issue', backref='user', cascade='all, delete-orphan')
    ratings = db.relationship('Rating',backref='user', cascade='all, delete-orphan')
    def hash_password(self, password):
        from werkzeug.security import generate_password_hash
        self.password = generate_password_hash(password)
    def verify_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'role': self.role,
            'f_name': self.f_name,
            'l_name': self.l_name,
            'last_login': self.last_login.isoformat(),
            'img_path': self.img_path,
            'last_read_book_id': self.last_read_book_id,
            'request_count': self.request_count,
            'created_datetime': self.created_datetime.isoformat(),
        }

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    page_count = db.Column(db.Integer, default=1)
    rating = db.Column(db.Integer, default=None)
    publication_date = db.Column(db.DateTime)
    isbn = db.Column(db.Integer)
    img_path = db.Column(db.String, default= image_domain+'/static/images/books/default.png')
    pdf_path = db.Column(db.String, default= image_domain+'/static/pdfs/default.pdf')
    created_datetime = db.Column(db.DateTime, default=datetime.now)
    # Define relationships
    authors = db.relationship('Author', secondary=book_author_association, backref='books', cascade="all, delete-orphan", single_parent=True)
    sections = db.relationship('Section', secondary=book_section_association, backref='books', cascade="all, delete-orphan", single_parent=True)
    requests = db.relationship('Request', backref='book', cascade='all, delete-orphan')
    issues = db.relationship('Issue', backref='book', cascade='all, delete-orphan')
    ratings = db.relationship('Rating', backref='book', cascade='all, delete-orphan')
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'page_count': self.page_count,
            'rating': self.rating,
            'publication_date': self.publication_date.isoformat() if self.publication_date else None,
            'isbn': self.isbn,
            'img_path': self.img_path,
            'pdf_path': self.pdf_path,
            'created_datetime': self.created_datetime.isoformat(),
        }
    def update_ratings(self):
        ratings = self.ratings
        if len(ratings) == 0:
            self.rating = None
        else:
            total = 0
            for rating in ratings:
                count += rating.rating
            self.rating = total/len(ratings)

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    img_path = db.Column(db.String, default= image_domain+'/static/images/authors/default.png')
    created_datetime = db.Column(db.DateTime, default=datetime.now)
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'img_path': self.img_path,
            'created_datetime': self.created_datetime.isoformat(),
        }

class Section(db.Model):
    __tablename__ = 'sections'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    books_count = db.Column(db.Integer,default=0)
    img_path = db.Column(db.String, default= image_domain+'/static/images/sections/default.png')
    created_datetime = db.Column(db.DateTime, default=datetime.now)
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'books_count': self.books_count,
            'img_path': self.img_path,
            'created_datetime': self.created_datetime.isoformat(),
        }

class Request(db.Model):
    __tablename__ = 'book_requests'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    status = db.Column(db.String, default='pending') #['pending',['denied','issued',],]
    created_datetime = db.Column(db.DateTime, default=datetime.now)
    end_datetime = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'status': self.status,
            'created_datetime': self.created_datetime.isoformat(),
            'end_datetime': self.end_datetime.isoformat()
        }
    def update_status(self,status):
        if status == 0:
            self.status = 'denied'
        else:
            self.status = 'issued'
        self.read = False

class Issue(db.Model):
    __tablename__ = 'book_issues'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    created_datetime = db.Column(db.DateTime, default=datetime.now)
    revoke_datetime = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String, default='pending') #['active','expired']

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'status': self.status,
            'created_datetime': self.created_datetime.isoformat(),
            'revoke_datetime': self.revoke_datetime.isoformat(),
        }

class Rating(db.Model):
    __tablename__ = 'book_ratings'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String)
    created_datetime = db.Column(db.DateTime, default=datetime.now)

    __table_args__ = (UniqueConstraint('user_id', 'book_id'),)
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'rating': self.rating,
            'description': self.description,
            'created_datetime': self.created_datetime.isoformat(),
        }