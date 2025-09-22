from flaskr import app
from flask import render_template, request, redirect, url_for
import sqlite3

DATABASE = 'database.db'

@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    db_books = con.execute("SELECT * FROM books").fetchall()
    con.close()

    return render_template(
        'index.html',
        books=db_books
    )

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )

@app.route('/edit')
def edit():
    id = request.args.get('id', type=int)
    if id is None:
        return 'IDが指定されていません。'

    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    book = con.execute("SELECT * FROM books WHERE id = ?", (id,)).fetchone()
    con.close()

    if book is None:
        return '該当するデータが見つかりませんでした。'

    return render_template(
        'edit.html',
        book=book
    )


@app.route('/register', methods=['POST'])
def register():
    title = request.form['title']
    price = request.form['price']
    arrival_day = request.form['arrival_day']

    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO books (title, price, arrival_day) VALUES(?,?,?)',
    [title, price, arrival_day])
    con.commit()
    con.close()

    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])  #/updateへのPOSTリクエストをedit.htmlから受け取る、以下のupdate()関数を実行
def update():
    id = request.form['id']
    title = request.form['title']
    price = request.form['price']
    arrival_day = request.form['arrival_day']
    
    con = sqlite3.connect(DATABASE)
    con.execute('UPDATE books SET title = ?, price = ?, arrival_day = ? WHERE id = ?',
    [title, price, arrival_day, id])
    con.commit()
    con.close()
    
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])  #/updateへのPOSTリクエストをedit.htmlから受け取る、以下のupdate()関数を実行
def delete():
    id = request.form['id']
    
    con = sqlite3.connect(DATABASE)
    con.execute('DELETE FROM books WHERE id = ?', (id,))
    con.commit()
    con.close()
    
    return redirect(url_for('index'))