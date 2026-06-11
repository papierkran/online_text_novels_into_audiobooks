# 在线文本转有声小说

将在线小说文本抓取、管理并合成为有声小说的全栈项目。支持用户登录、小说书库管理、多引擎 TTS 合成（gTTS / 讯飞 / SoVITS）、在线阅读与进度记录。

---

## 项目结构

```
online_text_novels_into_audiobooks/
├── backend_flask/          # Python Flask 后端
│   ├── app/                # API 路由与业务逻辑
│   │   ├── routes.py              # 所有 API 路由入口
│   │   ├── tts_gtts.py            # gTTS 文本/文件转语音
│   │   ├── tts_sovits.py          # SoVITS 模型语音合成（预留）
│   │   ├── tts_api.py             # 讯飞 TTS WebSocket API
│   │   ├── search_for_novels.py   # Bing 小说搜索
│   │   ├── user_management.py     # 用户注册/登录
│   │   ├── reading_history.py     # 阅读历史增删查
│   │   ├── basic_operations_all_novels.py  # 小说 CRUD
│   │   ├── count_words.py         # 字数统计
│   │   └── __init__.py            # Flask 应用初始化
│   ├── module/              # 数据库模型
│   │   ├── novel_info.py           # 小说信息表模型
│   │   ├── user_info.py            # 用户表模型
│   │   └── ReadingHistory.py       # 阅读历史表模型
│   ├── audio_novels.sql     # MySQL 建表 + 测试数据
│   ├── config.py            # 数据库连接配置
│   ├── run.py               # 启动入口（端口 30600）
│   ├── requirements.txt     # Python 依赖
│   └── README.md
│
├── frontend_vue/            # Vue 2 前端（PC 端）
│   ├── src/
│   │   ├── components/      # 页面组件
│   │   │   ├── Login.vue, Home.vue, BookShelf.vue
│   │   │   ├── Novel.vue, History.vue, User.vue
│   │   │   ├── InternetSearch.vue, Load.vue
│   │   │   ├── HomeView.vue   # 侧边栏
│   │   │   └── test.vue, HostView.vue
│   │   ├── router/index.js  # 路由定义
│   │   ├── App.vue          # 根组件
│   │   └── main.js
│   ├── config/              # Webpack 构建配置
│   ├── build/               # 构建脚本
│   └── package.json
│
├── frontend_recat/          # React 前端（备用/尝试）
├── backend_java_springboot/ # Spring Boot 后端（备用/尝试）
└── README.md                # 本文件
```

---

## 功能概览

### 后端 API（Flask, port 30600）

| 端点 | 方法 | 说明 |
|------|------|------|
| `/register` | POST | 用户注册 |
| `/login` | POST | 用户登录 |
| `/api/get_all_novels` | GET | 获取所有小说 |
| `/api/get_novel_id/<id>` | GET | 按 ID 获取单本小说 |
| `/api/add_novel` | POST | 添加小说 |
| `/api/update_novel/<id>` | PUT | 更新小说信息 |
| `/api/delete_novel/<id>` | DELETE | 删除小说 |
| `/api/novels` | GET | 获取小说标题列表 |
| `/api/get_all_novels/<title>` | GET | 按标题获取小说内容 |
| `/api/tts_gtts_text` | POST | 输入文本 → gTTS 语音 |
| `/api/tts_gtts_file` | POST | 上传 .txt 文件 → gTTS 语音 |
| `/api/tts_sovits` | POST | 输入文本 → SoVITS 语音 |
| `/api/search_for_novels` | GET | 通过 Bing 搜索小说 |
| `/api/count_words` | GET | 统计字数 |
| `/api/save_reading_history` | POST | 保存阅读进度 |
| `/api/get_reading_history/<user_id>` | GET | 获取阅读历史 |
| `/api/get_recent_reading_history/<user_id>` | GET | 获取最近一条记录 |

### 前端（Vue 2）

- **登录页** — 用户注册/登录入口
- **书架页** — 展示已入库小说列表
- **阅读页** — 在线阅读 + TTS 语音合成
- **搜索页** — 在线搜索并导入小说
- **历史页** — 阅读记录查看
- **用户页** — 个人中心
- **加载页** — 数据/音频加载进度

---

## 本地运行

### 前置要求

- Python 3.9+
- Node.js 14+ / npm
- MySQL（用于存储小说、用户、阅读历史）

### 1. 后端

```bash
cd backend_flask

# 安装依赖
pip install -r requirements.txt

# 初始化数据库
# 在 MySQL 中执行 audio_novels.sql

# 修改 config.py 中的数据库连接
# SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://user:password@host:3306/audio_novels"

# 启动服务
python run.py
# 访问 http://localhost:30600
```

### 2. 前端

```bash
cd frontend_vue

# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建生产版本
npm run build
```

---

## 数据库说明

使用 MySQL，库名 `audio_novels`，三张表：

- **novels_info** — 小说元信息（id, title, url, content, file_path, cover_url）
- **user_info** — 用户账号（id, username, password_hash）
- **reading_history** — 阅读记录（id, user_id, novel_id, read_time, read_content）

建表 SQL 见 `backend_flask/audio_novels.sql`。

---

## TTS 引擎说明

- **gTTS**（默认）— Google Text-to-Speech，免费，输出 MP3，支持中文
- **讯飞 TTS**（`tts_api.py`）— WebSocket 实时合成，需在代码中填入 APPID / APIKey / APISecret，输出 PCM 格式
- **SoVITS**（`tts_sovits.py`）— 预留框架，需自行配置 SoVITS 模型路径与推理脚本

---

## 技术栈

| 层 | 技术 |
|----|------|
| 后端框架 | Flask 3.x |
| ORM | SQLAlchemy |
| 数据库 | MySQL |
| 前端 | Vue 2 + Vue Router + Webpack |
| 语音合成 | gTTS / 讯飞 WebSocket TTS / SoVITS |
| 搜索 | Bing 爬虫（BeautifulSoup） |
