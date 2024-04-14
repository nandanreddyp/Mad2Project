api = None; BLOCKLIST = None
from flask_restful import Resource

from database import User

def create_apis(apz, blocklist):
    global api; global BLOCKLIST
    api = apz; BLOCKLIST = blocklist

    from .auth import Login
    from .librarian import librarianAnalytics
    from .user import UserResource
    from .section import SectionResource
    from .author import AuthorResource
    from .book import BookResource
    from .request import UserRequest
    from .issue import IssueResource
    from .fileHandle import profileImage