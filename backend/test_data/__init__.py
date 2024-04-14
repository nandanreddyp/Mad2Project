from database.models import db, User, Section, Book, Author, Request, Issue, Rating

from .user import add_users
from .author import add_authors
from .section import add_sections
from .book import add_books # in that only add book_author & book_section
from .request_issues import add_IssueRequests
from .rating import add_ratings

def add_test_data(app):
    with app.app_context():
        add_users(db,User)
        add_authors(db,Author)
        add_sections(db,Section)
        add_books(db,Book, Section, Author)
        add_IssueRequests(db,Request, Issue)
        add_ratings(db,Rating)

        db.session.commit()
        print('Added test data')
