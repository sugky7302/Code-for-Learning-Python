import os
import sqlite3

from flask import Blueprint, render_template, g


home = Blueprint('', __name__)


import main


# 提供使用者操作資料庫的功能
# 隱藏SQLite3的操作函數
class FlaskSQL:
    def __init__(self, path="./test.db", table_mode=""):
        self.path = path

        if not os.path.isfile(path):
            self.create(table_mode)

        self.database = self.get()

    # 讀取目錄下的資料庫並回傳操作物件
    def get(self):
        # 連接資料庫
        db = getattr(g, '_database', None)
        print("1")
        if db is None:
            # 創建新的資料庫
            db = g._database = sqlite3.connect(self.path)
            print("2")
            db.execute("PRAGMA foreign_keys = ON")
        print("3")
        return db

    def create(self, table_mode):
        with main.app.app_context():
            db = self.get()
            with main.app.open_resource(table_mode, mode='r') as f:
                db.cursor().executescript(f.read())
            print("4")
            db.commit()
            print("5")

    def remove(self):
        if os.path.isfile(self.path):
            os.remove(self.path)

    @main.app.teardown_appcontext
    def close(self, exception="None"):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    def execute(self, command):
        cursor = self.database.cursor()
        return cursor.execute(command)

    def commit(self):
        self.database.commit()


# 路由和處理函式配對
@home.route('/')
def index():
    db = FlaskSQL(path="./flask/test.db", table_mode="schema.sql")
    db.execute("INSERT INTO stations Values('A000', 0, '3,200,2,0', 1, '', '', 0, '')")
    db.execute("INSERT INTO stations Values('A001', 2, '0', 1, '', '2,3,3,201,2,1', 0, '4,5,6,7')")
    db.commit()

    data = []
    for t in db.execute("SELECT * from stations"):
        tb = []
        for v in t:
            tb.append(v)
        data.append(tb)
        print(t)
        print(t[0])

    db.close()

    return render_template('index.html', data=data)

# index的form action的網址要跟這裡一樣
@home.route('/load', methods=['GET'])
def load():
    return "Hello"