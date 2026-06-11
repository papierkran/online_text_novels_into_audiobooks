# app/novel_info.py
from app import db

# 小说信息模型
# id、title、url、content、file_path、cover_url
# id 标题 链接 内容 保存路径 封面
class novels_info(db.Model):

    # 表名
    __tablename__ = 'novels_info'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    cover_url = db.Column(db.String(255), nullable=False)

    def __init__(self, title, url, content, file_path, cover_url):
        self.title = title
        self.url = url
        self.content = content
        self.file_path = file_path
        self.cover_url = cover_url


