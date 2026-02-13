# 遵盛官网 GitHub 上传指南

此文档旨在帮助您手动将项目上传到 GitHub。

**新仓库地址**: `https://github.com/xinggggzz/zunsheng-web`

---

## 1. 准备工作
请确保您已经安装了 Git，并且已经获取了 GitHub 的 **Personal Access Token (Token)**。

> **小贴士**: 如果您还没有 Token，请前往 GitHub 设置 -> Developer Settings -> Personal access tokens -> Tokens (classic) -> 点击 "Generate new token"，并勾选 **`repo`** 权限。

## 2. 一键上传命令 (在项目根目录运行)

如果您已经初始化过 Git，请直接运行以下命令：

```bash
# 1. 添加所有文件
git add .

# 2. 提交更改
git commit -m "初始化遵盛官网项目"

# 3. 设置远程仓库 (如果还没设置)
git remote add origin https://github.com/xinggggzz/zunsheng-web.git

# 4. 推送到主分支
git push -u origin main
```

**输入验证**:
- **Username**: `xinggggzz`
- **Password**: (输入您的 Token，注意粘贴时屏幕不会有任何显示)

---

## 3. 关于 .gitignore 的说明
我已经为您重写了 `.gitignore` 文件。
- 默认情况下，**`db.sqlite3`** (数据库) 和 **`media/`** (产品图片) **会被上传**。
- 这符合您“私人项目云存储”的需求。
- 如果您未来不想上传这些庞大的数据文件，只需在 `.gitignore` 中取消对应行的 `#` 注释即可。

## 4. 后续维护
以后每次修改代码后，只需运行：
```bash
git add .
git commit -m "描述您的修改"
git push
```

如有任何问题，请随时查阅 `HANDOVER.md`。
