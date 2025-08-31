from flaskr import app
from flask import render_template, request, redirect, url_for
import sqlite3
DATABASE = 'database.db'

@app.route('/')#スラッシュはWebアプリのトップURL(root)
def index(): #トップ画面にアクセスしたときに実行される
    con = sqlite3.connect(DATABASE)
    db_books = con.execute("SELECT * FROM books").fetchall()
    con.close()

    books = [] #リスト　

    for row in db_books:
        books.append({'title': row[0], 'price':row[1], 'arrival_day': row[2]})

    return render_template(
        'index.html',
        books=books #html側に渡す(引数の名前はbookで、html側と一緒)
    )

@app.route('/form') #関数formの処理とformというURLをひもづける
def form():
    return render_template(
        'form.html'
    )

@app.route('/register', methods=['POST']) #POSTというリクエストの場合に下のregisterという関数が呼び出される
def register():
    title=request.form['title']
    price=request.form['price']
    arrival_day = request.form['arrival_day']

    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO books VALUES(?,?,?)',
    [title, price, arrival_day])
    con.commit()
    con.close()

    return redirect(url_for('index')) #登録が終わったら自動でトップページに戻る


    