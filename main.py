from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users')
def users():
    return 'You are here at users page!'

@app.route('/users/<int:id>')
def users_by_id(id):
    return 'You are here at users page! %s'%id

if __name__ == '__main__':
   app.run()
