from flask import Flask
app=Flask (__name__)
app.route('/')
def index():
    return "Hello World"

if name == '__main__':
    app.run(debug=True)