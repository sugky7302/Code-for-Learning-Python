from flask import Flask
from config import DevConfig
from datetime import timedelta

# 初始化 Flask 類別成為 instance
app = Flask(__name__)
app.config.from_object(DevConfig)

from views import home
app.register_blueprint(home)

# 判斷自己執行非被當做引入的模組，因為 __name__ 這變數若被當做模組引入使用就不會是 __main__
if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=1)
    app.jinja_env.auto_reload = True
    app.run(port=6010, debug=True)