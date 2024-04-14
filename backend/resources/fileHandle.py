from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
import os

from resources import api
from functions import get_unique_filename, count_pdf_pages, extract_first_page_as_png


image_domain = 'http://127.0.0.1:5000'

class profileImage(Resource): #✅
    def __init__(self):
        self.main_path = os.path.join(os.getcwd(),'static','images','profiles')
        self.link_path = '/static/images/profiles/'
    def get(self):
        try: 
            file_path = request.args.get('path').strip()
            if file_path == '': raise NameError
        except: return {'msg':'File path is requried'}, 400
        if not file_path: return {'msg':'File path can not be empty'}, 400
        if os.path.exists(os.path.join(self.main_path,str(file_path).split('/')[-1])):
            return {'url':image_domain+self.link_path+file_path.split('/')[-1]}, 200
        return {'msg':'File doesn\'t exists'}
    def post(self):
        file = request.files.get('file')
        if file and file.filename != '':
            unique_file_name = get_unique_filename(file.filename)
            path = os.path.join(self.main_path,unique_file_name)
            file.save(path)
            link_path = self.link_path + unique_file_name
            return {'msg':'File uploaded successfully','path': link_path}
        return {'msg':'File not given to upload'}, 400
    def put(self):
        file = request.files.get('file')
        try: 
            file_path = request.form.get('path').strip()
            if file_path == '': raise NameError
        except: return {'msg':'File path is requried'}, 400
        if file and file.filename != '' :
            path = os.path.join(self.main_path,os.path.split(file_path)[-1])
            if not os.path.exists(path):
                return {'msg':'File not found by given id'}, 404
            file.save(path)
            return {'msg':'File updated','path':file_path}
        return {'msg':'File not given to update'}, 400
    @jwt_required()
    def delete(self):
        try:
            file_path = request.form.get('path').strip()
            if file_path == '': raise NameError
        except: return {'msg':'File path is requried'}, 400
        path = os.path.join(self.main_path,os.path.split(file_path)[-1])
        if not os.path.exists(path): return {'msg':'File not exists for given file\'s path'}, 400
        if path.split('/')[-1] == 'default.png': return {'msg':'Default images can not be deleted'},400
        os.remove(path)
        return {'msg':'Image deleted successfully'}, 200
api.add_resource(profileImage,'/api/files/images/profiles')

class sectionImage(Resource): #✅
    @jwt_required()
    def __init__(self):
        self.main_path = os.path.join(os.getcwd(),'static','images','sections')
        self.link_path = '/static/images/sections/'
    def get(self):
        try: 
            file_path = request.args.get('path').strip()
            if file_path == '': raise NameError
        except: return {'msg':'File path is requried'}, 400
        if not file_path: return {'msg':'File path can not be empty'}, 400
        if os.path.exists(os.path.join(self.main_path,str(file_path).split('/')[-1])):
            return {'url':image_domain+self.link_path+file_path.split('/')[-1]}, 200
        return {'msg':'File doesn\'t exists'}
    def post(self):
        file = request.files.get('file')
        if file and file.filename != '':
            unique_file_name = get_unique_filename(file.filename)
            path = os.path.join(self.main_path,unique_file_name)
            file.save(path)
            link_path = self.link_path + unique_file_name
            return {'msg':'File uploaded successfully','path': link_path}
        return {'msg':'File not given to upload'}, 400
    def put(self):
        file = request.files.get('file')
        try: 
            file_path = request.form.get('path').strip()
            if file_path == '': raise NameError
        except: return {'msg':'File path is requried'}, 400
        if file and file.filename != '' :
            path = os.path.join(self.main_path,os.path.split(file_path)[-1])
            if not os.path.exists(path):
                return {'msg':'File not found by given id'}, 404
            file.save(path)
            return {'msg':'File updated','path':file_path}
        return {'msg':'File not given to update'}, 400
    def delete(self):
        try:
            file_path = request.form.get('path').strip()
            if file_path == '': raise NameError
        except: return {'msg':'File path is requried'}, 400
        path = os.path.join(self.main_path,os.path.split(file_path)[-1])
        if not os.path.exists(path): return {'msg':'File not exists for given file\'s path'}, 400
        if path.split('/')[-1] == 'default.png': return {'msg':'Default images can not be deleted'},400
        os.remove(path)
        return {'msg':'Image deleted successfully'}, 200
api.add_resource(sectionImage,'/api/files/images/sections')

class authorImage(Resource): #✅
    @jwt_required()
    def __init__(self):
        self.main_path = os.path.join(os.getcwd(),'static','images','authors')
        self.link_path = '/static/images/authors/'
    def get(self):
        try: 
            file_path = request.args.get('path').strip()
            if file_path == '': raise NameError
        except: return {'msg':'File path is requried'}, 400
        if not file_path: return {'msg':'File path can not be empty'}, 400
        if os.path.exists(os.path.join(self.main_path,str(file_path).split('/')[-1])):
            return {'url':image_domain+self.link_path+file_path.split('/')[-1]}, 200
        return {'msg':'File doesn\'t exists'}
    def post(self):
        file = request.files.get('file')
        if file and file.filename != '':
            unique_file_name = get_unique_filename(file.filename)
            path = os.path.join(self.main_path,unique_file_name)
            file.save(path)
            link_path = self.link_path + unique_file_name
            return {'msg':'File uploaded successfully','path': link_path}
        return {'msg':'File not given to upload'}, 400
    def put(self):
        file = request.files.get('file')
        try: 
            file_path = request.form.get('path').strip()
            if file_path == '': raise NameError
        except: return {'msg':'File path is requried'}, 400
        if file and file.filename != '' :
            path = os.path.join(self.main_path,os.path.split(file_path)[-1])
            if not os.path.exists(path):
                return {'msg':'File not found by given id'}, 404
            file.save(path)
            return {'msg':'File updated','path':file_path}
        return {'msg':'File not given to update'}, 400
    def delete(self):
        try:
            file_path = request.form.get('path').strip()
            if file_path == '': raise NameError
        except: return {'msg':'File path is requried'}, 400
        path = os.path.join(self.main_path,os.path.split(file_path)[-1])
        if not os.path.exists(path): return {'msg':'File not exists for given file\'s path'}, 400
        if path.split('/')[-1] == 'default.png': return {'msg':'Default images can not be deleted'},400
        os.remove(path)
        return {'msg':'Image deleted successfully'}, 200
api.add_resource(authorImage,'/api/files/images/authors')

class bookImage(Resource): #✅
    @jwt_required()
    def __init__(self):
        self.main_path = os.path.join(os.getcwd(),'static','images','books')
        self.link_path = '/static/images/books/'
    def get(self):
        try: 
            file_path = request.args.get('path').strip()
            if file_path == '': raise NameError
        except: return {'msg':'File path is requried'}, 400
        if not file_path: return {'msg':'File path can not be empty'}, 400
        if os.path.exists(os.path.join(self.main_path,str(file_path).split('/')[-1])):
            return {'url':image_domain+self.link_path+file_path.split('/')[-1]}, 200
        return {'msg':'File doesn\'t exists'}
    def post(self):
        file = request.files.get('file')
        if file and file.filename != '':
            unique_file_name = get_unique_filename(file.filename)
            path = os.path.join(self.main_path,unique_file_name)
            file.save(path)
            link_path = self.link_path + unique_file_name
            return {'msg':'File uploaded successfully','path': link_path}
        return {'msg':'File not given to upload'}, 400
    def put(self):
        file = request.files.get('file')
        try: 
            file_path = request.form.get('path').strip()
            if file_path == '': raise NameError
        except: return {'msg':'File path is requried'}, 400
        if file and file.filename != '' :
            path = os.path.join(self.main_path,os.path.split(file_path)[-1])
            if not os.path.exists(path):
                return {'msg':'File not found by given id'}, 400
            if path.split('/')[-1] == 'default.png': return {'msg':'Default images can not be deleted'},400
            file.save(path)
            return {'msg':'File updated','path':file_path}
        return {'msg':'File not given to update'}, 400
    def delete(self):
        try:
            file_path = request.form.get('path').strip()
            if file_path == '': raise NameError
        except: return {'msg':'File path is requried'}, 400
        path = os.path.join(self.main_path,os.path.split(file_path)[-1])
        if not os.path.exists(path): return {'msg':'File not exists for given file\'s path'}, 400
        if path.split('/')[-1] == 'default.png': return {'msg':'Default images can not be deleted'},400
        os.remove(path)
        return {'msg':'Image deleted successfully'}, 200
api.add_resource(bookImage,'/api/files/images/books')

class bookPdf(Resource): #✅
    @jwt_required()
    def __init__(self):
        self.main_path = os.path.join(os.getcwd(),'static','pdfs')
        self.link_path = '/static/pdfs/'
    def get(self):
        try: 
            file_path = request.args.get('path').strip()
            if file_path == '': raise NameError
        except: return {'msg':'File path is requried'}, 400
        if not file_path: return {'msg':'File path can not be empty'}, 400
        if os.path.exists(os.path.join(self.main_path,str(file_path).split('/')[-1])):
            return {'url':image_domain+self.link_path+file_path.split('/')[-1]}, 200
        return {'msg':'File doesn\'t exists'}
    def post(self):
        file = request.files.get('file')
        if file and file.filename != '':
            unique_file_name = get_unique_filename(file.filename)
            path = os.path.join(self.main_path,unique_file_name)
            file.save(path)
            page_count = count_pdf_pages(path) # count pages
            image_path = os.path.join(os.getcwd(),'static','book_images',unique_file_name.split('.')[0]+'.png')
            extract_first_page_as_png(path,image_path) # get first page
            pdf_link_path = self.link_path + unique_file_name; image_link_path = '/static/book_images/'+unique_file_name.split('.')[0]+'.png'
            return {'msg':'File uploaded successfully',
                    'pdf': {
                        'page_count':page_count,
                        'pdf_path': pdf_link_path,
                        'image_path':image_link_path}}
        return {'msg':'File not given to upload'}, 400
    def put(self):
        file = request.files.get('file')
        try: 
            file_path = request.form.get('path').strip()
            if file_path == '': raise NameError
        except: return {'msg':'File path is requried'}, 400
        if file and file.filename != '' :
            path = os.path.join(self.main_path,os.path.splittext(file_path)[-1])
            if not os.path.exists(path):
                return {'msg':'File not found by given id'}, 404
            file.save(path)
            return {'msg':'File updated','path':file_path}
        return {'msg':'File not given to update'}, 400
    def delete(self):
        try:
            file_path = request.form.get('path').strip()
            if file_path == '': raise NameError
        except: return {'msg':'File path is requried'}, 400
        path = os.path.join(self.main_path,os.path.split(file_path)[-1])
        if not os.path.exists(path): return {'msg':'File not exists for given file\'s path'}, 400
        if path.split('/')[-1] == 'default.pdf': return {'msg':'Default pdf can not be deleted'},400
        os.remove(path)
        return {'msg':'PDF deleted successfully'}, 200
api.add_resource(bookPdf,'/api/files/pdfs')