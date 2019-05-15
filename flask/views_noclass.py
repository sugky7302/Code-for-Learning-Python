import os
import sqlite3

from flask import Blueprint, render_template, g

home = Blueprint('', __name__)

# NOTE: 一定要用.，這樣python才能確認是當前目錄
DATABASE = "./flask/test.db"


# 讀取目錄下的資料庫並回傳操作物件
def load_db():
    # 連接資料庫
    db = getattr(g, '_database', None)
    print("1")
    if db is None:
        # 創建新的資料庫
        db = g._database = sqlite3.connect(DATABASE)
        print("2")
        db.execute("PRAGMA foreign_keys = ON")
    print("3")
    return db


import main


def init_db():
    with main.app.app_context():
        db = load_db()
        with main.app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def remove_db():
    if os.path.isfile(DATABASE):
        os.remove(DATABASE)


@main.app.teardown_appcontext
def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# 路由和處理函式配對
@home.route('/')
def index():
    if not os.path.isfile(DATABASE):
        init_db()

    db = load_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO roles (rolename) Values('Administrator')")
    cursor.execute("INSERT INTO roles (rolename) Values('Member')")

    data = []
    for role in cursor.execute("SELECT * from roles"):
        data.append(role[1])
        print(role)

    db.commit()
    close_db("any msg")

    return render_template('index.html', data=data)

# index的form action的網址要跟這裡一樣
@home.route('/load', methods=['GET'])
def load():
    return "Hello"