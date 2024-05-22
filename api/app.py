from flask import Flask, request
from markupsafe import escape
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

#@app.route('/')
#def hello():
#    name = request.args.get("name", "World")
#    return f'Hello, {escape(name)}!'

