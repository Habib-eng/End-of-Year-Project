from bottle import run
from src.main import app

run(app,host="127.0.0.1",port="8080",debug=True,reloader=True)