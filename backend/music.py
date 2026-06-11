import tkinter as tk
from tkinter import filedialog
import pygame
import os

# 初始化Pygame Mixer
pygame.mixer.init()

# 创建主窗口
root = tk.Tk()
root.title("Audio Player")
root.geometry("400x200")

# 播放音频的全局变量
current_file = None

# 定义打开文件函数
def open_file():
    global current_file
    current_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if current_file:
        pygame.mixer.music.load(current_file)
        label['text'] = os.path.basename(current_file)

# 定义播放函数
def play_audio():
    if current_file:
        pygame.mixer.music.play()

# 定义暂停函数
def pause_audio():
    if pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
        pygame.mixer.music.pause()

# 定义继续播放函数
def resume_audio():
    pygame.mixer.music.unpause()

# 定义停止函数
def stop_audio():
    pygame.mixer.music.stop()

# 标签显示当前加载的音频文件
label = tk.Label(root, text="No file loaded", font=("Arial", 14))
label.pack(pady=10)

# 创建按钮
open_button = tk.Button(root, text="Open", command=open_file)
play_button = tk.Button(root, text="Play", command=play_audio)
pause_button = tk.Button(root, text="Pause", command=pause_audio)
resume_button = tk.Button(root, text="Resume", command=resume_audio)
stop_button = tk.Button(root, text="Stop", command=stop_audio)

# 布局按钮
open_button.pack(pady=5)
play_button.pack(pady=5)
pause_button.pack(pady=5)
resume_button.pack(pady=5)
stop_button.pack(pady=5)

# 启动主循环
root.mainloop()
