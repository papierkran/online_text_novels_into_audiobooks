# app/count_words.py
from app import db
from module.novel_info import novels_info  # 导入 Novel 模型

def count_words_in_novels():
    try:
        # 查询所有已转换为有声小说的小说
        novels = novels_info.query.all()

        total_word_count = 0
        # 计算所有小说的总字数
        for novel in novels:
            if novel.content:  # 确保内容不为空
                total_word_count += len(novel.content)

        return total_word_count
    except Exception as e:
        # 捕捉并抛出错误
        raise Exception(f"Error counting words: {str(e)}")
