import sqlite3

DATABASE='database.db'
def create_books_table():
    con =  sqlite3.connect(DATABASE)#データベースに登録したら自動でIDが付与される、IDを付与することで、登録項目を識別し、それぞれだけを編集できるようにする
    con.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title, price, arrival_day)")
    con.close()