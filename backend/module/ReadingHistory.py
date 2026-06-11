from app import db
from datetime import datetime

# 阅读历史记录模型
class ReadingHistory(db.Model):
    __tablename__ = 'reading_history'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'), nullable=False)
    novel_id = db.Column(db.Integer, db.ForeignKey('novels_info.id'), nullable=False)
    read_time = db.Column(db.DateTime, default=datetime.utcnow)  # 记录阅读时间
    read_content = db.Column(db.Text, nullable=False)  # 保存阅读的内容

    # 关系设置
    user = db.relationship('user_info', backref=db.backref('reading_history', lazy=True))
    novel = db.relationship('novels_info', backref=db.backref('reading_history', lazy=True))
