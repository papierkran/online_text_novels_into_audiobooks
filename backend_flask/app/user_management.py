# app/user_management.py

from flask import jsonify
from app import db
from module.user_info import user_info


# 用户注册逻辑
def register_user(data):
    username = data.get('username')
    password = data.get('password')

    # 检查用户名和密码是否为空
    if not username or not password:
        return jsonify({"error": "用户名和密码是必需的"}), 400

    # 检查用户是否已存在
    existing_user = user_info.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"error": "用户已存在"}), 400

    # 创建新用户并存储到数据库
    new_user = user_info(username=username)
    new_user.set_password(password)  # 哈希化密码
    db.session.add(new_user)

    try:
        db.session.commit()  # 提交更改
    except Exception as e:
        db.session.rollback()  # 回滚会话
        return jsonify({"error": str(e)}), 500  # 返回错误信息

    return jsonify({"message": "注册成功"}), 201


# 用户登录逻辑
def login_user(data):
    username = data.get('username')
    password = data.get('password')

    # 检查用户名和密码是否为空
    if not username or not password:
        return jsonify({"error": "用户名和密码是必需的"}), 400

    # 查询用户是否存在
    user = user_info.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "用户名或密码不正确"}), 401

    return jsonify({"message": "登录成功"}), 200
