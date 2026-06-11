# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # 启用跨域

# 初始化

# 创建 Flask 应用
app = Flask(__name__)
app.config.from_pyfile('../config.py')

# 启用 SQLAlchemy 数据库
db = SQLAlchemy(app)

# 启用跨域
CORS(app)


# 导入应用路由
from app import routes
