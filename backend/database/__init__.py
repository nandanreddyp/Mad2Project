from .models import *
from functions import remove_static_files
import os

def init_db(app):
    db.init_app(app)
    if not os.path.exists(os.path.join(os.getcwd(),'database','database.db')):
        remove_static_files() # remove unnecessary 
        print('Creating database')
        with app.app_context():
            db.create_all()
            print('Creating Admin, creds:\nEmail: librarian@elibri.com , Password: 12345678')
            admin = User(f_name='Librarian',email='librarian@elibri.com',role='librarian')
            db.session.add(admin)
            admin.hash_password('12345678')
            db.session.commit()
