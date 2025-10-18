 from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route('/hello/<name>')
def hello_name(name):
    return f'<h1>Hello, {name}!</h1>'

@app.route('/about')
def about():
    return '<p>This is a simple Flask web server</p>'
if __name__ == "__main__":
    port = 8080
    app.run(debug=True,host='0.0.0.0',port=port)
