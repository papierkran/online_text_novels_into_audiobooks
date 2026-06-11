# app/tts_sovits.py


from flask import request, jsonify, send_file
import os
import subprocess

# 假设这里是你SoVITS模型的路径
SOVITS_MODEL_PATH = "audio_models/D_lty.pth"  # 替换为你的SoVITS模型路径
OUTPUT_AUDIO_PATH = "output.wav"  # 输出音频文件名

def tts_sovits(text, model_name):
    """
    使用 SoVITS 将文本转换为语音并保存为音频文件。

    :param text: 输入文本
    :param model_name: 所选模型的名称
    :return: 输出音频文件的路径
    """
    # 创建临时输入文件
    with open("input.txt", "w", encoding='utf-8') as f:
        f.write(text)

    # 使用 SoVITS 模型进行音频生成
    # 假设你有一个可以通过命令行调用的 SoVITS 脚本
    try:
        command = [
            "python", "path/to/sovits/inference_script.py",  # 替换为你的推理脚本路径
            "--model", os.path.join(SOVITS_MODEL_PATH, model_name),
            "--input", "input.txt",
            "--output", OUTPUT_AUDIO_PATH
        ]
        subprocess.run(command, check=True)  # 运行命令并检查错误

        return OUTPUT_AUDIO_PATH  # 返回输出音频的路径
    except subprocess.CalledProcessError as e:
        print(f"Error while running SoVITS: {e}")
        return None

def process_text_to_speech():
    """
    处理文本到语音请求的函数。

    :return: JSON 响应
    """
    data = request.get_json()
    text = data.get("text", "")
    model_name = data.get("model", "default_model")  # 默认模型名称

    if not text:
        return jsonify({"error": "Text is required"}), 400

    # 使用 SoVITS 生成语音
    audio_file_path = tts_sovits(text, model_name)
    if audio_file_path and os.path.exists(audio_file_path):
        return send_file(audio_file_path, mimetype='audio/wav', as_attachment=True, download_name="output.wav")
    else:
        return jsonify({"error": "Failed to process text."}), 500
