from flask import Flask
app = Flask(__name__) #__init__.pyを受け取る　__ は半角　この__name__に入るファイルを起点としてつくってとFlaskに指示
import flaskr.main

from flaskr import db
db.create_books_table()

