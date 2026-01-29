# 快速使用指南

## 📋 目录结构

```
personal-homepage/
├── content/
│   └── _index.md              # ✏️ 主要内容编辑这个文件
├── static/
│   └── img/
│       └── avatar.jpg         # 📸 你的头像放这里
├── themes/
│   └── tokiwa-single/
│       └── layouts/
│           └── index.html     # 🎨 页面模板和样式
├── hugo.toml                  # ⚙️ 网站配置
└── .github/
    └── workflows/
        └── hugo.yml           # 🚀 自动部署配置
```

## ⚡ 三步快速开始

### 1️⃣ 修改个人信息

编辑 `hugo.toml`：

```toml
[params]
  author = "你的名字"
  email = "your@email.com"
  location = "你的城市"
```

### 2️⃣ 添加头像

把你的照片放到：`static/img/avatar.jpg`

### 3️⃣ 更新内容

编辑 `content/_index.md`，更新所有 section

## 🎯 重点修改位置

### hugo.toml - 基本信息

```toml
baseURL = "https://你的用户名.github.io/"
title = "你的名字 - Homepage"

[params]
  author = "你的名字"
  email = "your@email.com"
  location = "城市, 国家"
  
[params.social]
  github = "https://github.com/你的用户名"
  scholar = "Google Scholar 链接"
  linkedin = "LinkedIn 链接"
  twitter = "Twitter 链接"
  email = "mailto:your@email.com"
```

### content/_index.md - 所有内容

这个文件包含：
- 📝 About Me
- 📚 Publications  
- 💼 Experience
- 🎓 Education
- 🤝 Services
- 🎨 Miscellaneous

直接编辑 HTML 内容即可。

## 🚀 部署到 GitHub Pages

### 方式一：命令行部署（推荐）

```bash
cd /Users/leon/Project/personal-homepage

# 初始化并上传
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/你的用户名/你的用户名.github.io.git
git push -u origin main
```

### 方式二：GitHub Desktop

1. 打开 GitHub Desktop
2. Add Repository → Add Existing Repository
3. 选择 `/Users/leon/Project/personal-homepage`
4. Publish repository
5. 命名为：`你的用户名.github.io`

### 配置 Pages

1. 打开 GitHub 仓库 Settings
2. 点击 Pages
3. Source 选择 **GitHub Actions**
4. 等待自动部署完成

✅ 完成！访问：`https://你的用户名.github.io`

## 📝 内容修改示例

### 添加新论文

在 `content/_index.md` 的 Publications section 中添加：

```html
<div class="publication-card">
    <div class="title">你的论文标题</div>
    <div class="authors"><strong>你的名字</strong>, 合作者</div>
    <div class="venue">会议或期刊名称 2025</div>
    <span class="badge">Oral</span>
    <div class="description">
        论文简介...
    </div>
    <div class="links">
        <a href="#">📄 Paper</a>
        <a href="#">💻 Code</a>
    </div>
</div>
```

### 添加新经历

```html
<div class="timeline-item">
    <div class="date">2025.01 - Present</div>
    <div class="position">职位名称</div>
    <div class="organization">公司/学校名称</div>
    <div class="details">
        <strong>导师：</strong>导师名字<br>
        <strong>工作内容：</strong>
        <ul>
            <li>具体工作1</li>
            <li>具体工作2</li>
        </ul>
    </div>
</div>
```

## 🎨 自定义样式

### 修改颜色

编辑 `themes/tokiwa-single/layouts/index.html`，找到：

```css
:root {
    --primary-color: #01513a;      /* 深绿色 - 主标题 */
    --primary-light: #028760;      /* 中绿色 - 链接 */
    --bg-light: #edf9f8;           /* 浅绿色 - 卡片背景 */
    --accent-orange: #ff9800;      /* 橙色 - 标签 */
}
```

### 添加新的导航项

1. 在 `hugo.toml` 添加菜单项：

```toml
[[menu.main]]
  identifier = "awards"
  name = "Awards"
  url = "#awards"
  weight = 7
```

2. 在 `content/_index.md` 添加对应 section：

```html
<section id="awards">
    <h2>🏆 Awards</h2>
    <ul>
        <li>Award 1</li>
        <li>Award 2</li>
    </ul>
</section>
```

## 💡 使用技巧

### 1. 本地预览

```bash
hugo server -D
# 访问 http://localhost:1313
```

### 2. 更新网站

```bash
git add .
git commit -m "Update content"
git push
```

GitHub Actions 会自动部署。

### 3. 检查部署状态

在 GitHub 仓库页面 → Actions 标签查看

### 4. 紧急回滚

```bash
git revert HEAD
git push
```

## ❓ 常见问题速查

| 问题 | 解决方案 |
|------|----------|
| 网站显示 404 | 检查仓库名是否为 `用户名.github.io`，等待 5-10 分钟 |
| 图片不显示 | 确认图片在 `static/img/`，使用 `/img/xxx.jpg` |
| 样式错乱 | 清除浏览器缓存，强制刷新（Ctrl+F5） |
| 修改没生效 | 检查是否 push，查看 Actions 是否成功 |

## 📂 文件清单

必须文件：
- ✅ `hugo.toml` - 配置文件
- ✅ `content/_index.md` - 页面内容
- ✅ `themes/tokiwa-single/layouts/index.html` - 模板
- ✅ `.github/workflows/hugo.yml` - 部署配置
- ✅ `static/img/avatar.jpg` - 头像

可选文件：
- 📄 `README.md` - 项目说明
- 📄 `DEPLOYMENT.md` - 部署指南
- 📄 `.gitignore` - Git 忽略文件

## 🔗 有用的链接

- [Hugo 文档](https://gohugo.io/documentation/)
- [GitHub Pages 文档](https://docs.github.com/pages)
- [Markdown 语法](https://www.markdownguide.org/basic-syntax/)
- [HTML 参考](https://developer.mozilla.org/en-US/docs/Web/HTML)

---

## 🎓 示例内容

项目已包含示例内容，可以直接在此基础上修改：

- ✅ About Me 模板
- ✅ 3 篇示例论文
- ✅ 3 段经历示例
- ✅ 教育背景模板
- ✅ Academic Services 示例
- ✅ 技能和兴趣模板

---

**需要帮助？查看 `README.md` 或 `DEPLOYMENT.md`** 📚
