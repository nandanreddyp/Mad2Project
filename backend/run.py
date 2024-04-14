from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from database import init_db

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.secret_key = 'LadyGagaAteAnApple'
app.config['JWT_SECRET_KEY'] = 'LadyGagaAteAnApple'

jwt = JWTManager(app)
BLOCKLIST = set()

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_data):
    jti = jwt_data['jti']
    return jti in BLOCKLIST

from flask_restful import Api, Resource
api = Api(app)
from resources import create_apis
create_apis(api, BLOCKLIST)

import os
cwd = os.getcwd()
db_path = os.path.join(cwd,'database','database.db')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
