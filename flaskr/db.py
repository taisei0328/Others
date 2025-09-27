import sqlite3

DATABASE = "database.db"


def create_recipes_table():
    con = sqlite3.connect(DATABASE)
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            ingredients TEXT,
            cooking_time TEXT,
            price REAL,
            comment TEXT
        )
    """
    )
    con.close()
