# from test import *  # in order to add data in database

# from run import app
# from database import db, User, Book, Section, Rating

# with app.app_context():
#     section = db.session.get(Section,1)
#     print(section.books)

# from functions import remove_static_files
# remove_static_files()

import os
db_path = os.path.join(os.getcwd(),'database','database.db')
if os.path.exists(db_path): os.remove(db_path)
from run import *
