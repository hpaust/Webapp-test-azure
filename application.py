
#sfrom flask import Flask, jsonify, request
#app = Flask(__name__)

#languages = [{'name': 'Javascript'},{'name':'Henrik'},{'name':'Ruby'}]

#@app.route('/')
#def test():
#    return jsonify({'message':'It works'})

#@app.route('/lang',methods=['GET'])
#def returnAll():
#    return jsonify({'languages': languages})



#@app.route('/lang/<string:name>',methods=['GET'])
#def returnOne(name):
#    langs = [language for language in languages if language['name']==name]
#    return jsonify({'language':langs[0]})

#@app.route('/lang',methods=['POST'])
#def addOne():
#    language = {'name': request.get_json(force=True).get('name')}
    
#    languages.append(language)
#    return jsonify({'languages':languages})

#if __name__ == '__main__':
#  app.run()

#from flask import Flask
#from flask_restful import Resource, Api
 
#app = Flask(__name__)
#api = Api(app)
 
#class HelloWorld(Resource):
#    def get(self):
#        return {'hello': 'world'}
 
#api.add_resource(HelloWorld, '/')
 
#if __name__ == '__main__':
#    app.run(debug=True)



from flask import Flask,jsonify,request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from flask import make_response
import datetime
from passlib.context import CryptContext
import os
import pandas as pd



app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['APPSECRET']


app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(hours=2)

api = Api(app, prefix="/api/direktedyr")



#USER_DATA = {
#    USR_HASH: PASS_HASH
#}

USER_DATA = {os.environ['USRHASH']:os.environ['PASSHHASH']}

class User(object):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "User(id='%s')" % self.id

def verify(username, password):
    crypter2 = CryptContext(schemes=['sha256_crypt'])
    if not (username and password):
        return False
    if crypter2.verify(password,USER_DATA[list(USER_DATA.keys())[0]]) and crypter2.verify(username,list(USER_DATA.keys())[0]):
        return User(id=123)

def identity(payload):
    user_id = payload['identity']
    return {"user_id": user_id}


jwt = JWT(app, verify, identity)


class PrivateResource(Resource):
    @jwt_required()
    def get(self):
        return {"meaning_of_life": 42}


api.add_resource(PrivateResource, '/meaning')

class GetDagensvitsFromExcel(Resource):
    @jwt_required()
    def get(self):
        df = pd.read_excel('testFlaskApi.xlsx')
        a = df.loc[0,'brukernavn']
        b=df.loc[0,'passord']
        return {"dagens":a,"vits":b}

api.add_resource(GetDagensvitsFromExcel,'/excel_test')


class Post_tester(Resource):
    @jwt_required()
    def post(self):
        json_data = request.get_json(force=True)
        un = json_data['username']
        ps = json_data['password']
        
        return jsonify({'brukernavn':un,'passord':ps})

api.add_resource(Post_tester,'/poster')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
   app.run(debug=False)
    
    