# 部署指南

## 快速部署到 GitHub Pages

### 第一步：创建 GitHub 仓库

1. 登录 GitHub
2. 创建新仓库，命名为：`你的用户名.github.io`
   - 例如：`Lukebird17.github.io`
   - 必须是公开仓库（Public）

### 第二步：上传代码

在项目目录下执行：

```bash
cd /Users/leon/Project/personal-homepage

# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: Personal homepage"

# 设置主分支
git branch -M main

# 关联远程仓库（替换成你的用户名）
git remote add origin https://github.com/Lukebird17/Lukebird17.github.io.git

# 推送到 GitHub
git push -u origin main
```

### 第三步：配置 GitHub Pages

1. 打开你的 GitHub 仓库页面
2. 点击 **Settings**（设置）
3. 在左侧菜单找到 **Pages**
4. 在 **Source** 部分：
   - 选择 **GitHub Actions**
5. 保存后，GitHub 会自动开始构建

### 第四步：等待部署完成

1. 回到仓库主页
2. 点击 **Actions** 标签
3. 查看工作流运行状态
4. 等待绿色勾号（表示成功）

### 第五步：访问你的网站

网站地址：`https://你的用户名.github.io`

例如：`https://Lukebird17.github.io`

---

## 更新网站内容

每次修改内容后：

```bash
git add .
git commit -m "Update content"
git push
```

GitHub Actions 会自动重新部署。

---

## 自定义内容

### 1. 修改个人信息

编辑 `hugo.toml`：

```toml
[params]
  author = "卢鸿良"          # 你的名字
  email = "你的邮箱"
  location = "上海, 中国"
  
  [params.social]
    github = "https://github.com/Lukebird17"
    scholar = "你的Google Scholar链接"
    linkedin = "你的LinkedIn链接"
```

### 2. 添加头像

将你的照片命名为 `avatar.jpg`，放到：
```
static/img/avatar.jpg
```

建议：
- 正方形图片（500x500像素）
- 清晰的头像照片
- JPG 或 PNG 格式

### 3. 更新页面内容

编辑 `content/_index.md`，修改：
- About Me（关于我）
- Publications（发表论文）
- Experience（工作经历）
- Education（教育背景）
- Services（学术服务）
- Misc（其他信息）

---

## 常见问题

### Q1: 网站显示 404

**解决方案：**
1. 确认仓库名是 `你的用户名.github.io`
2. 检查 GitHub Actions 是否成功运行
3. 等待 5-10 分钟后再试

### Q2: 样式显示不正常

**解决方案：**
1. 清除浏览器缓存
2. 检查 `hugo.toml` 中的 `baseURL` 是否正确
3. 确认所有文件都已推送到 GitHub

### Q3: 图片不显示

**解决方案：**
1. 确认图片在 `static/img/` 目录下
2. 在 markdown 中使用 `/img/文件名.jpg`（以 / 开头）
3. 检查文件名大小写

### Q4: 修改后网站没更新

**解决方案：**
1. 检查是否已 push 到 GitHub
2. 查看 Actions 是否运行成功
3. 强制刷新浏览器（Ctrl+F5 或 Cmd+Shift+R）

---

## 本地测试

推送到 GitHub 前，可以本地测试：

```bash
# 安装 Hugo（macOS）
brew install hugo

# 或下载：https://github.com/gohugoio/hugo/releases

# 启动本地服务器
cd /Users/leon/Project/personal-homepage
hugo server -D

# 浏览器访问：http://localhost:1313
```

---

## 进阶自定义

### 修改配色

编辑 `themes/tokiwa-single/layouts/index.html`，找到 CSS 变量：

```css
:root {
    --primary-color: #01513a;      /* 主色调 */
    --primary-light: #028760;      /* 浅绿色 */
    --accent-orange: #ff9800;      /* 强调色 */
}
```

### 添加新的导航项

在 `hugo.toml` 中添加：

```toml
[[menu.main]]
  identifier = "projects"
  name = "Projects"
  url = "#projects"
  weight = 7
```

然后在 `content/_index.md` 中添加对应的 section：

```html
<section id="projects">
    <h2>🚀 Projects</h2>
    <!-- 你的项目内容 -->
</section>
```

---

## 需要帮助？

- Hugo 文档：https://gohugo.io/documentation/
- GitHub Pages 文档：https://docs.github.com/pages
- 项目 Issues：https://github.com/Lukebird17/Lukebird17.github.io/issues

---

**祝部署顺利！🎉**
