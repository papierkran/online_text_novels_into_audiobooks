import tkinter as tk

def say_hello():
    print("Hello!")


# 创建主窗口
root = tk.Tk()
root.title("文本转有声小说")  # 设置窗口标题
root.geometry("900x600")     # 设置窗口大小

# 创建菜单栏
menu_bar = tk.Menu(root)
# 创建一个文件菜单
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=say_hello)
file_menu.add_command(label="Save", command=say_hello)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# 将文件菜单添加到菜单栏
menu_bar.add_cascade(label="File", menu=file_menu)

# 添加标签
label = tk.Label(root, text="Hello, Tkinter!")
label.grid(row=1, column=0, padx=10, pady=10)


def tts_gtts_button():
    label.config(text="Button clicked!")

# 添加按钮
tts_gtts_button = tk.Button(root, text="本地tts转语音", command=tts_gtts_button)
tts_gtts_button.grid(row=0, column=0, padx=10, pady=10)



tts_sovits_button = tk.Button(root, text="在线api转语音", command=tts_gtts_button)
tts_sovits_button.grid(row=0, column=1, padx=10, pady=10)


# 使用 grid 布局
button1 = tk.Button(root, text="Button 1")
button1.grid(row=1, column=0, padx=10, pady=10)

button2 = tk.Button(root, text="Button 2")
button2.grid(row=1, column=1, padx=10, pady=10)


# 设置菜单栏
root.config(menu=menu_bar)

# 运行主循环
root.mainloop()