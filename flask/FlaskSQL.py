# 提供使用者操作資料庫的功能
# 隱藏SQLite3的操作函數
class FlaskSQL:
    def __init__(self, path="test.db", table_mode=""):
        self.path = path

        if not os.path.isfile(path):
            self.create(table_mode)

        self.object = self.get()

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
            db.commit()

    def remove(self):
        if os.path.isfile(self.path):
            os.remove(self.path)

# app.teardown_appcontext
    def close(self, exception="None"):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

# function insert(表, 欄位, 值)
#   執行SQL的execute(INSERT INTO + 表 + (欄位) + Values('值'))
# end

# function delete(表, 欄位)
#   執行SQL的execute(DELETE FROM + 表 + WHERE NAME = + 欄位)
# end

# function load(表, 欄位: "")
#   if 欄位的字串長度 > 0
#       執行SQL的execute(SELECT * FROM + 表 + WHERE ID = 欄位)
#   else
#       執行SQL的execute(SELECT * FROM + 表)
#   end
# end