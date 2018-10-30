#from flask import Flask
#app = Flask(__name__)

#languages = [{'name': 'Javascript'},{'name':'Henrik'},{'name':'Ruby'}]

#@app.route('/',methods=['GET'])
#def test():
#    return jsonify({'message':'It works'})

#@app.route('/lang',methods=['GET'])
#def returnAll():
#    return jsonify({'languages': languages})

#def shutdown_server():
#    func = request.environ.get('werkzeug.server.shutdown')
#    if func is None:
#        raise RuntimeError('Not running with the Werkzeug Server')
#    func()

#@app.route('/shutdown', methods=['POST'])
#def shutdown():
#    shutdown_server()
#    return 'Server shutting down...'


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

app = Flask(__name__)



@app.route('/')

def hello_world():

  return 'Hello, World!'



if __name__ == '__main__':

  app.run()
