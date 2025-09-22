from flaskr import app
from flask import render_template, request, redirect, url_for
import sqlite3

DATABASE = "database.db"


@app.route("/")
def index():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    db_recipes = con.execute("SELECT * FROM recipes").fetchall()
    con.close()

    return render_template("index.html", recipes=db_recipes)


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/edit")
def edit():
    id = request.args.get("id", type=int)
    if id is None:
        return "IDが指定されていません。"

    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    recipe = con.execute("SELECT * FROM recipes WHERE id = ?", (id,)).fetchone()
    con.close()

    if recipe is None:
        return "該当するデータが見つかりませんでした。"

    return render_template("edit.html", recipe=recipe)


@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    ingredients = request.form["ingredients"]
    cooking_time = request.form["cooking_time"]
    price = request.form["price"]
    comment = request.form["comment"]

    con = sqlite3.connect(DATABASE)
    con.execute(
        "INSERT INTO recipes (name, ingredients, cooking_time, price, comment) VALUES(?,?,?,?,?)",
        [name, ingredients, cooking_time, price, comment],
    )
    con.commit()
    con.close()

    return redirect(url_for("index"))


@app.route("/update", methods=["POST"])
def update():
    id = request.form["id"]
    name = request.form["name"]
    ingredients = request.form["ingredients"]
    cooking_time = request.form["cooking_time"]
    price = request.form["price"]
    comment = request.form["comment"]

    con = sqlite3.connect(DATABASE)
    con.execute(
        "UPDATE recipes SET name = ?, ingredients = ?, cooking_time = ?, price = ?, comment = ? WHERE id = ?",
        [name, ingredients, cooking_time, price, comment, id],
    )
    con.commit()
    con.close()

    return redirect(url_for("index"))


@app.route("/delete", methods=["POST"])
def delete():
    id = request.form["id"]

    con = sqlite3.connect(DATABASE)
    con.execute("DELETE FROM recipes WHERE id = ?", (id,))
    con.commit()
    con.close()

    return redirect(url_for("index"))
