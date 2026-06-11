from flask import jsonify
from app import db
from module.novel_info import novels_info  # 导入小说模型

def get_all_novels():
    try:
        novels = novels_info.query.all()
        novels_list = [{
            "id": novel.id,
            "title": novel.title,
            "url": novel.url,
            "content": novel.content,
            "file_path": novel.file_path,
            "cover_url": novel.cover_url
        } for novel in novels]
        return jsonify(novels_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_novel(id):
    try:
        novel = novels_info.query.get_or_404(id)
        return jsonify({
            "id": novel.id,
            "title": novel.title,
            "url": novel.url,
            "content": novel.content,
            "file_path": novel.file_path,
            "cover_url": novel.cover_url
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_novel(request):
    try:
        data = request.get_json()

        # 检查是否包含必需字段
        title = data.get('title')
        url = data.get('url')
        content = data.get('content')
        file_path = data.get('file_path')
        cover_url = data.get('cover_url')

        if not all([title, url, content, file_path, cover_url]):
            return jsonify({"error": "所有字段都是必需的"}), 400

        # 创建新小说
        new_novel = novels_info(title=title, url=url, content=content, file_path=file_path, cover_url=cover_url)
        db.session.add(new_novel)
        db.session.commit()

        return jsonify({"message": "小说添加成功", "novel": {
            "id": new_novel.id,
            "title": new_novel.title,
            "url": new_novel.url,
            "content": new_novel.content,
            "file_path": new_novel.file_path,
            "cover_url": new_novel.cover_url
        }}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_novel(id, request):
    try:
        novel = novels_info.query.get_or_404(id)
        data = request.get_json()

        novel.title = data.get('title', novel.title)
        novel.url = data.get('url', novel.url)
        novel.content = data.get('content', novel.content)
        novel.file_path = data.get('file_path', novel.file_path)
        novel.cover_url = data.get('cover_url', novel.cover_url)

        db.session.commit()

        return jsonify({"message": "小说更新成功", "novel": {
            "id": novel.id,
            "title": novel.title,
            "url": novel.url,
            "content": novel.content,
            "file_path": novel.file_path,
            "cover_url": novel.cover_url
        }}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_novel(id):
    try:
        novel = novels_info.query.get_or_404(id)
        db.session.delete(novel)
        db.session.commit()
        return jsonify({"message": "小说删除成功"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
