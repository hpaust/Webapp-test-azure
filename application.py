
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

from flask import Flask
from flask_restful import Resource, Api
 
app = Flask(__name__)
api = Api(app)
 
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
 
api.add_resource(HelloWorld, '/')
 
if __name__ == '__main__':
    app.run(debug=True)
