from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class user_info(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # 保存密码哈希值

    # 设置密码时，保存哈希
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # 验证密码时，进行哈希比对
    def check_password(self, password):
        return check_password_hash(self.password, password)  # 对比哈希值
