# Zunsheng Auto Parts Website (遵盛汽车零部件官网)

## 📌 项目简介 (Project Overview)
本项目是为遵盛汽车零部件有限公司开发的官方企业网站。采用 **Python / Django** 框架开发，旨在展示公司产品、新闻动态、企业文化及技术实力。项目注重视觉设计（Apple/Hawbo 风格的高端极简主义）与 SEO 优化。

## 🏗️ 技术架构 (Technical Architecture)
*   **后端**: Python 3.9+ / Django 4.0+
*   **前端**: HTML5, CSS3 (Vanilla CSS), JavaScript, FontAwesome 6.0
*   **数据库**: SQLite (默认), 可配置为 MySQL/PostgreSQL
*   **模板引擎**: Django Template Language (DTL)

## 📂 目录结构 (Directory Structure)
```text
AutoPartsWeb/
├── manage.py                # Django 项目管理脚本
├── requirements.txt         # 项目依赖列表
├── db.sqlite3               # SQLite 数据库文件 (开发环境)
├── zunsheng/                # 项目核心配置 (Settings, URL路由, WSGI/ASGI)
├── website/                 # 核心应用 App (业务逻辑)
│   ├── management/          # 自定义管理命令 (初始化数据、生成二维码等)
│   ├── migrations/          # 数据库迁移文件
│   ├── models.py            # 数据模型定义
│   ├── views.py             # 视图函数
│   └── urls.py              # App 内部路由
├── templates/               # HTML 模板文件
│   ├── base.html            # 全站基础骨架 (Header/Footer)
│   └── website/             # 各页面模板 (Index, About, Product...)
├── static/                  # 静态资源 (CSS, JS, Images, Fonts)
│   ├── css/globals.css      # 全局样式表
│   └── js/main.js           # 前端交互逻辑
└── media/                   # 用户上传的文件 (产品图, Banner, PDF等)
```

## 🚀 快速开始 (Getting Started)

### 1. 环境准备
确保已安装 Python 3.8 或更高版本。

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 数据库迁移
初始化数据库结构：
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. 数据初始化 (重要)
项目包含几个自定义命令，用于快速填充演示数据：

*   **初始化公司基本信息** (必跑):
    ```bash
    python manage.py init_company
    ```
*   **初始化产品数据** (可选，会清空现有产品):
    ```bash
    python manage.py init_products
    ```
*   **生成图册二维码** (确保 static/images 目录下有二维码):
    ```bash
    python manage.py generate_qr
    ```

### 5. 启动开发服务器
```bash
python manage.py runserver
```
访问 `http://127.0.0.1:8000` 查看效果。

### 6. 后台管理
创建管理员账户：
```bash
python manage.py createsuperuser
```
访问 `http://127.0.0.1:8000/admin` 管理全站内容。

## 🛠️ 维护与开发 (Maintenance)
*   **样式修改**: 主要样式位于 `static/css/globals.css`。请遵循现有的 CSS 变量规范。
*   **邮件配置**: 在 `zunsheng/settings.py` 中配置 SMTP 服务器 (`EMAIL_HOST_user`, `EMAIL_HOST_PASSWORD`) 以启用留言通知功能。

## 📝 许可证
此项目为内部私有项目，仅供遵盛汽车零部件有限公司使用。
