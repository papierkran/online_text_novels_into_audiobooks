from flask import Flask, jsonify, request, send_file
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)

# 手动输入文本的 TTS 处理
def tts_gtts_text():
    try:
        data = request.get_json()  # 获取 JSON 数据
        text = data.get("text", "")  # 获取文本

        if not text:  # 检查文本是否为空
            return jsonify({"error": "Text content is required."}), 400

        # 使用 gTTS 将文本转换为语音
        tts = gTTS(text, lang='zh')

        # 使用 BytesIO 将音频存储在内存中
        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)  # 重置指针到开始位置

        # 返回音频流
        return send_file(audio_buffer, mimetype='audio/mpeg', as_attachment=False, download_name="output.mp3")

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 上传文件的 TTS 处理

def tts_gtts_file():
    try:
        if 'file' not in request.files:  # 检查是否上传了文件
            return jsonify({"error": "No file part"}), 400

        file = request.files['file']
        if file.filename.endswith('.txt'):  # 确保是文本文件
            text = file.read().decode('utf-8')
        else:
            return jsonify({"error": "Only .txt files are allowed."}), 400

        if not text:  # 检查文本是否为空
            return jsonify({"error": "Text content is required."}), 400

        # 使用 gTTS 将文本转换为语音
        tts = gTTS(text,lang='zh')

        # 使用 BytesIO 将音频存储在内存中
        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)  # 重置指针到开始位置

        # 返回音频流
        return send_file(audio_buffer, mimetype='audio/mpeg', as_attachment=False, download_name="output.mp3")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

