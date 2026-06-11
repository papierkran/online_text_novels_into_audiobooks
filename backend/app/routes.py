# app/routes.py

from flask import request, jsonify, send_file

from module.ReadingHistory import ReadingHistory
from module.novel_info import novels_info
from app import app
from app.count_words import count_words_in_novels
from app.tts_gtts import tts_gtts_file, tts_gtts_text
from app.tts_sovits import tts_sovits
from app.search_for_novels import search_novels
from app.basic_operations_all_novels import get_all_novels, get_novel, add_novel, update_novel, delete_novel
from app.user_management import register_user, login_user
from app.reading_history import save_reading_history, get_reading_history, get_recent_reading_history


# 用户注册登录
# 用户注册路由
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        return register_user(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 用户登录路由
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        return login_user(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500




# 增删改查小说信息
# 获取所有小说
@app.route('/api/get_all_novels', methods=['GET'])
def get_all_novels_api():
    return get_all_novels()

# 根据ID获取单本小说
@app.route('/api/get_novel_id/<int:id>', methods=['GET'])
def get_novel_api(id):
    return get_novel(id)

# 添加新小说
@app.route('/api/add_novel', methods=['POST'])
def add_novel_api():
    return add_novel(request)

# 更新小说信息
@app.route('/api/update_novel/<int:id>', methods=['PUT'])
def update_novel_api(id):
    return update_novel(id, request)

# 删除小说
@app.route('/api/delete_novel/<int:id>', methods=['DELETE'])
def delete_novel_api(id):
    return delete_novel(id)





# 保存阅读历史记录的路由
@app.route('/api/save_reading_history', methods=['POST'])
def record_reading_history():
    data = request.get_json()
    user_id = data.get('user_id')
    novel_id = data.get('novel_id')
    content = data.get('content')

    if not all([user_id, novel_id, content]):
        return jsonify({"error": "缺少必要的字段"}), 400

    response = save_reading_history(user_id, novel_id, content)
    return jsonify(response), 200 if "message" in response else 500

# 获取阅读历史记录的路由
@app.route('/api/get_reading_history/<int:user_id>', methods=['GET'])
def fetch_reading_history(user_id):
    history = get_reading_history(user_id)
    return jsonify(history), 200 if "error" not in history else 500



@app.route('/api/get_recent_reading_history/<int:user_id>', methods=['GET'])
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



# 路由处理函数
@app.route('/api/tts_gtts_file', methods=['POST'])
def tts_gtts_file_api():
    try:
        response = tts_gtts_file()
        return response
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

@app.route('/api/tts_gtts_text', methods=['POST'])
def tts_gtts_text_api():
    try:
        response = tts_gtts_text()
        return response
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


@app.route('/api/tts_sovits', methods=['POST'])
def tts_sovits_api():
    try:
        response = tts_sovits(request)
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/search_for_novels', methods=['GET'])
def search_novels_api():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "查询参数是必需的"}), 400

    try:
        results = search_novels(query)
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# def download_novel_api():
#     try:
#         data = request.get_json()
#         url = data.get('url')
#         file_path = data.get('file_path')
#         # 调用业务逻辑函数进行文本转语音
#         response = download_novel(url, file_path)
#         return response
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500




@app.route('/api/count_words', methods=['GET'])
def count_words_api():
    try:
        # 调用业务逻辑函数来统计字数
        word_count = count_words_in_novels()
        return jsonify({"total_word_count": word_count}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 获取小说标题的API
@app.route('/api/novels', methods=['GET'])
def get_novels():
    try:
        novels = novels_info.query.all()  # 从数据库中查询所有小说
        novel_list = [{"title": novel.title, "url": novel.url} for novel in novels]  # 构建小说列表
        return jsonify(novel_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 获取小说内容的API
@app.route('/api/get_all_novels/<title>', methods=['GET'])
def get_novel_content(title):
    try:
        novel = novels_info.query.filter_by(title=title).first()  # 根据标题查询小说
        if novel:
            return jsonify({"content": novel.content})  # 返回小说内容
        else:
            return jsonify({"error": "Novel not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


