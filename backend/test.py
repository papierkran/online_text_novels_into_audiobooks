from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:123456@192.168.137.111:3306/audio_novels"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/test_db')
def test_db():
    try:
        # 尝试连接数据库
        db.session.execute(text('SELECT * from novels_info'))
        return "数据库连接成功！"
    except Exception as e:
        return f"数据库连接失败: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
