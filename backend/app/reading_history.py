from app import db
from module.ReadingHistory import ReadingHistory
from datetime import datetime

# 保存阅读历史记录
def save_reading_history(user_id, novel_id, content):
    try:
        # 创建阅读历史记录
        new_history = ReadingHistory(
            user_id=user_id,
            novel_id=novel_id,
            read_content=content,
            read_time=datetime.utcnow()  # 使用当前时间
        )
        db.session.add(new_history)
        db.session.commit()
        return {"message": "阅读历史记录已保存"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

# 查询用户的所有阅读历史记录
def get_reading_history(user_id):
    try:
        # 查询用户的阅读历史记录
        histories = ReadingHistory.query.filter_by(user_id=user_id).all()
        history_list = [{
            "id": history.id,
            "novel_title": history.novel.title,
            "read_content": history.read_content,
            "read_time": history.read_time
        } for history in histories]

        return history_list
    except Exception as e:
        return {"error": str(e)}


def get_recent_reading_history(user_id):
    try:
        # 查询用户的阅读历史记录，按 read_time 降序排列，获取最近的一条记录
        recent_history = ReadingHistory.query.filter_by(user_id=user_id).order_by(
            ReadingHistory.read_time.desc()).first()

        if not recent_history:
            return {"message": "No reading history found."}, 404

        history_data = {
            "id": recent_history.id,
            "novel_title": recent_history.novel.title,
            "read_content": recent_history.read_content,
            "read_time": recent_history.read_time
        }

        return history_data
    except Exception as e:
        return {"error": str(e)}, 500