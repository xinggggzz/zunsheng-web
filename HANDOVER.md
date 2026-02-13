# 项目交接与维护指南 (Handover Document)

**项目名称**: 遵盛汽车零部件官网 (Zunsheng Auto Parts Website)
**交接日期**: 2026-02-13
**版本**: 1.0.0

---

## 1. 核心资产概览
*   **代码仓库**: `AutoPartsWeb/`
*   **数据库**: `db.sqlite3` (当前开发环境数据)
*   **配置中心**: `zunsheng/settings.py` (包含数据库连接、密钥、邮件配置)
*   **静态资源**: `static/` (CSS, JS, Fonts)
*   **媒体文件**: `media/` (用户上传的产品图片、PDF图册、Banner图)

---

## 2. 部署关键配置 (Critical Configuration)

### ⚠️ 安全设置 (Production Safety)
在正式部署到生产服务器前，**必做**以下修改：

1.  **修改 SECRET_KEY**:
    *   打开 `zunsheng/settings.py`。
    *   修改 `SECRET_KEY` 为一个全新的、随机生成的长字符串（可以使用 Django 的 `get_random_secret_key()` 生成）。
    *   **切勿**将当前的开发密钥用于生产环境。

2.  **关闭调试模式 (DEBUG)**:
    *   在 `zunsheng/settings.py` 中设置 `DEBUG = False`。
    *   这将关闭详细的错误页面，防止敏感信息泄露。

3.  **ALLOWED_HOSTS**:
    *   修改 `ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']`。
    *   列出所有允许访问该网站的域名。

### 📧 邮件通知配置 (Email Service)
网站使用了 QQ SMTP 服务发送客户留言通知。

*   **当前配置**:
    *   使用的是个人的 QQ 邮箱 SMTP 服务。
    *   **建议**: 将其更改为公司的专用企业邮箱 SMTP。
    *   `EMAIL_HOST`: `smtp.qq.com` (或腾讯企业邮 `smtp.exmail.qq.com`)
    *   `EMAIL_HOST_USER`: `your-company-email`
    *   `EMAIL_HOST_PASSWORD`: 此处需填入 **授权码** (Authorization Code)，而非邮箱登录密码。
    *   `ADMIN_EMAILS`: 需要接收通知的管理员邮箱列表。

---

## 3. 定期维护 (Routine Maintenance)

### 数据备份 (Backup)
*   **数据库**: 定期备份 `db.sqlite3` 文件。建议每周备份一次，或配置自动化脚本。使用 MySQL/PostgreSQL 时请使用相应的 dump 工具。
*   **媒体文件**: 定期备份 `media/` 文件夹。这里存放着所有产品图片和图册，一旦丢失无法恢复。

### 更新内容 (Content Update)
所有内容均可通过 Django Admin `/admin` 后台管理：
*   **产品管理**: 添加新产品、修改产品描述、图片。
*   **公司信息**: 修改公司简介、联系电话、地址、首页 Banner 图。
*   **新闻发布**: 发布公司新闻、行业动态。
*   **图册更新**: 在后台上传新的 PDF 图册后，需要重新生成二维码。

### 生成二维码 (Generate QR)
当 PDF 图册 URL 发生变化（例如上传了新文件或更换了域名）时，二维码需要更新：
1.  登录后台上传新 PDF。
2.  确保 `website/management/commands/generate_qr.py` 中的 `catalog_url` 指向正确的生产环境 URL。
3.  运行命令: `python manage.py generate_qr`。
4.  生成的二维码会自动保存在 `static/images/catalog_qr.png`，前端页面将立即生效。

---

## 4. 已知问题与优化建议 (Known Issues & Future Improvements)
1.  **静态文件服务**:
    *   当前使用 Django `runserver` 服务静态文件。在生产环境中 (Nginx/Apache)，需要运行 `python manage.py collectstatic` 并配置 Web 服务器来托管 `/static/` 和 `/media/` 路径。
    
2.  **安全性**:
    *   建议为后台 `/admin` 路径增加额外的访问限制（如 IP 白名单）。
    *   建议配置 HTTPS 证书（SSL）。

3.  **性能优化**:
    *   当前图片未做压缩处理。若图片过多，建议集成 PIL 压缩或使用第三方 CDN 存储。

---

## 5. 联系人 (Contacts)
*   **原开发负责人**: [Antigravity Agent]
*   **技术支持**: [Please Insert Contact Info]

---
*文档结束*
