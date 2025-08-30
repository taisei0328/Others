from flaskr import app
from flask import render_template

@app.route('/')#スラッシュはWebアプリのトップURL(root)
def index(): #トップ画面にアクセスしたときに実行される
    books = [
        {'title': 'はらぺこ',
        'price': '1200',
        'arrival_day':'2025年8月30日'
    },{'title': 'ぐりとぐら',
        'price': '1000',
        'arrival_day':'2025年8月25日'
    },] #リスト　

    return render_template(
        'index.html',
        books=books #html側に渡す(引数の名前はbookで、html側と一緒)
    )

@app.route('/form') #関数formの処理とformというURLをひもづける
def form():
    return render_template(
        'form.html'
    )