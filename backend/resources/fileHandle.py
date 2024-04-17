from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
import os

from resources import api
from functions import get_unique_filename


image_domain = 'http://127.0.0.1:5000'

class profileImage():
    def __init__(self):
        self.main_path = os.path.join(os.getcwd(),'static','images','profiles')
        self.link_path = '/static/images/profiles/'

    def save(self, file):
        unique_file_name = get_unique_filename(file.filename)
        path = os.path.join(self.main_path,unique_file_name)
        file.save(path)
        link_path = image_domain + self.link_path + unique_file_name
        return link_path

    def update(self, file_path, file):
        file_name = file_path.split('/')[-1]
        path = os.path.join(self.main_path, file_name)
        self.delete(file_path)
        return self.save(file)

    def delete(self, file_path):
        file_name = file_path.split('/')[-1]
        path = os.path.join(self.main_path, file_name)
        if not os.path.exists(path) or file_name == 'default.png' :
            return False
        os.remove(path)
        return True

class sectionImage():
    def __init__(self):
        self.main_path = os.path.join(os.getcwd(),'static','images','sections')
        self.link_path = '/static/images/sections/'

    def save(self, file):
        unique_file_name = get_unique_filename(file.filename)
        path = os.path.join(self.main_path,unique_file_name)
        file.save(path)
        link_path = image_domain + self.link_path + unique_file_name
        return link_path

    def update(self, file_path, file):
        file_name = file_path.split('/')[-1]
        path = os.path.join(self.main_path, file_name)
        self.delete(file_path)
        return self.save(file)

    def delete(self, file_path):
        file_name = file_path.split('/')[-1]
        path = os.path.join(self.main_path, file_name)
        if not os.path.exists(path) or file_name == 'default.png' :
            return False
        os.remove(path)
        return True

class authorImage():
    def __init__(self):
        self.main_path = os.path.join(os.getcwd(),'static','images','authors')
        self.link_path = '/static/images/authors/'

    def save(self, file):
        unique_file_name = get_unique_filename(file.filename)
        path = os.path.join(self.main_path,unique_file_name)
        file.save(path)
        link_path = image_domain + self.link_path + unique_file_name
        return link_path

    def update(self, file_path, file):
        file_name = file_path.split('/')[-1]
        path = os.path.join(self.main_path, file_name)
        self.delete(file_path)
        return self.save(file)

    def delete(self, file_path):
        file_name = file_path.split('/')[-1]
        path = os.path.join(self.main_path, file_name)
        if not os.path.exists(path) or file_name == 'default.png' :
            return False
        os.remove(path)
        return True
    
class bookImage():
    def __init__(self):
        self.main_path = os.path.join(os.getcwd(),'static','images','books')
        self.link_path = '/static/images/books/'
       
    def save(self, file):
        unique_file_name = get_unique_filename(file.filename)
        path = os.path.join(self.main_path,unique_file_name)
        file.save(path)
        link_path = image_domain + self.link_path + unique_file_name
        return link_path

    def update(self, file_path, file):
        file_name = file_path.split('/')[-1]
        path = os.path.join(self.main_path, file_name)
        self.delete(file_path)
        return self.save(file)

    def delete(self, file_path):
        file_name = file_path.split('/')[-1]
        path = os.path.join(self.main_path, file_name)
        if not os.path.exists(path) or file_name == 'default.png' :
            return False
        os.remove(path)
        return True

class bookPdf():
    def __init__(self):
        self.main_path = os.path.join(os.getcwd(),'static','pdfs')
        self.link_path = '/static/pdfs/'
       
    def save(self, file):
        unique_file_name = get_unique_filename(file.filename)
        path = os.path.join(self.main_path,unique_file_name)
        file.save(path)
        link_path = image_domain + self.link_path + unique_file_name
        return link_path

    def update(self, file_path, file):
        file_name = file_path.split('/')[-1]
        path = os.path.join(self.main_path, file_name)
        self.delete(file_path)
        return self.save(file)

    def delete(self, file_path):
        file_name = file_path.split('/')[-1]
        path = os.path.join(self.main_path, file_name)
        if not os.path.exists(path) or file_name == 'default.pdf' :
            return False
        os.remove(path)
        return True