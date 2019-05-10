from flask import Flask, render_template, request
from config import DevConfig

# 初始化 Flask 類別成為 instance
app = Flask(__name__)
app.config.from_object(DevConfig)

# 路由和處理函式配對
@app.route('/')
def index():
    return render_template('index.html')

# index的form action的網址要跟這裡一樣
@app.route('/test', methods=["POST"])
def ab():
    name = request.form.get('username')
    return "Hello, " + name


# 判斷自己執行非被當做引入的模組，因為 __name__ 這變數若被當做模組引入使用就不會是 __main__
if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True      
    app.jinja_env.auto_reload = True
    app.run(port=6010)