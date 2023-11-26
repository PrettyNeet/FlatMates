from flask import Flask

app = Flask(FlatMates)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if FlatMates == '__main__':
    app.run()
