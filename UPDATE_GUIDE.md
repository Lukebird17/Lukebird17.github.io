# 个人主页更新指南

## 📄 简历文件放置位置

1. **将你的简历 PDF 放到这里**：
   ```
   /Users/leon/Project/personal-homepage/static/cv.pdf
   ```

2. **更新简历链接**：
   编辑 `/layouts/index.html`，找到这一行：
   ```html
   <p>📄 <em>My CV is available here: <a href="#">Curriculum Vitae (PDF)</a></em></p>
   ```
   
   改为：
   ```html
   <p>📄 <em>My CV is available here: <a href="/cv.pdf" target="_blank">Curriculum Vitae (PDF)</a></em></p>
   ```

## 🔗 更新超链接

### 1. 论文链接

在 `/layouts/index.html` 中找到每篇论文的链接部分，例如：

```html
<div class="links">
    <a href="#">📄 Paper</a>
    <a href="#">💻 Code</a>
    <a href="#">🌐 Project</a>
</div>
```

替换 `#` 为实际链接：

```html
<div class="links">
    <a href="https://arxiv.org/abs/xxxxx" target="_blank">📄 Paper</a>
    <a href="https://github.com/username/repo" target="_blank">💻 Code</a>
    <a href="https://project-website.com" target="_blank">🌐 Project</a>
</div>
```

**提示**：
- 如果某个链接暂时没有（比如代码还未开源），可以直接删除那一行
- `target="_blank"` 会让链接在新标签页打开

### 2. 社交媒体链接

**当前已配置的链接**：
- Google Scholar: https://scholar.google.com/citations?hl=en&user=nwKRB-EAAAAJ
- GitHub: https://github.com/Lukebird17
- LinkedIn: https://www.linkedin.com/in/hongliang-lu
- X (Twitter): https://x.com/Lukebird18k
- Email: leonsny2017@gmail.com

**如需修改**，编辑 `/layouts/index.html` 中的社交链接部分，找到：
```html
<div class="social-links">
    <a href="YOUR_SCHOLAR_URL" target="_blank" title="Google Scholar">
    <a href="YOUR_GITHUB_URL" target="_blank" title="GitHub">
    ...
</div>
```

同时也要更新 `hugo.toml` 中的配置。

### 3. 如何检查链接是否正确

**方法 1：本地预览检查**
1. 启动服务器：`hugo server`
2. 打开浏览器：http://localhost:1313/
3. 点击每个链接，看是否能正常打开

**方法 2：浏览器开发者工具**
1. 右键点击链接 → "检查元素"
2. 查看 `<a>` 标签的 `href` 属性是否正确

**方法 3：部署后测试**
- 部署到 GitHub Pages 后，完整测试所有链接

## 🖼️ 添加论文图片

### 1. 准备图片

- **推荐尺寸**：160×120 像素（或相同比例）
- **格式**：JPG 或 PNG
- **文件名**：`gm100.jpg`, `qdit4sr.jpg`, `tacache.jpg`

### 2. 放置图片

将图片放到这个目录：
```
/Users/leon/Project/personal-homepage/static/img/
```

例如：
```
static/img/gm100.jpg
static/img/qdit4sr.jpg
static/img/tacache.jpg
```

### 3. 图片已经配置好了

在 HTML 中已经设置好了：
```html
<img src="/img/gm100.jpg" alt="GM-100" class="publication-image">
<img src="/img/qdit4sr.jpg" alt="Q-DiT4SR" class="publication-image">
<img src="/img/tacache.jpg" alt="TACache" class="publication-image">
```

只需要确保图片文件名匹配即可。

### 4. 如果没有图片

如果暂时没有论文图片，可以：
1. 从论文 PDF 中截取 Figure 1 或主要架构图
2. 使用论文的缩略图
3. 或者临时删除 `<img>` 标签那一行

## 📝 Miscellaneous 部分一般写什么？

### 典型内容包括：

1. **Technical Skills（技术技能）**
   - 编程语言：Python, C++, Java 等
   - 框架/工具：PyTorch, TensorFlow, ROS 等
   - 其他技能：Linux, Git, Docker 等

2. **Awards & Honors（奖项荣誉）**
   - 奖学金
   - 竞赛获奖
   - 学术荣誉

3. **Languages（语言能力）**
   - 中文（母语）
   - 英文（流利）
   - 其他语言

4. **Hobbies & Interests（兴趣爱好）**【可选】
   - 展示个性的部分
   - 运动、音乐、阅读等
   - 让你看起来更立体

5. **Teaching Experience（教学经历）**【可选】
   - 助教经历
   - 辅导经验

6. **Community Service（社区服务）**【可选】
   - 开源贡献
   - 志愿者活动
   - 学生组织

### 你目前的 Miscellaneous 包括：

✅ Technical Skills（已有）
✅ Awards & Honors（已有）
✅ Hobbies & Interests（已有）

这个配置已经很合适了！

## 🚀 部署到 GitHub Pages

### 1. 生成静态网站

```bash
cd /Users/leon/Project/personal-homepage
hugo
```

这会在 `public/` 目录生成静态文件。

### 2. 推送到 GitHub

```bash
cd public/
git init
git add .
git commit -m "Update personal homepage"
git branch -M main
git remote add origin https://github.com/Lukebird17/Lukebird17.github.io.git
git push -u origin main
```

### 3. 访问你的网站

几分钟后，访问：https://lukebird17.github.io/

## ❓ 常见问题

### Q: 修改后看不到更新？
A: 
1. 强制刷新浏览器（Cmd+Shift+R）
2. 清除浏览器缓存
3. 检查终端是否有 Hugo 重建信息

### Q: 图片显示不出来？
A: 
1. 检查图片文件名是否正确
2. 检查图片是否在 `static/img/` 目录
3. 检查图片格式（JPG/PNG）

### Q: 链接点击无效？
A: 检查是否还是 `href="#"`，需要改为实际 URL

### Q: 如何添加新的论文？
A: 
1. 在 `/layouts/index.html` 中复制一个 `publication-card` div
2. 修改标题、作者、描述等内容
3. 添加对应的论文图片到 `static/img/`

## 📧 需要帮助？

如果有任何问题，可以：
1. 检查浏览器控制台（F12）的错误信息
2. 查看 Hugo 终端输出的警告/错误
3. 参考 Hugo 官方文档：https://gohugo.io/documentation/
