# GitHub Pages 部署指南

本项目已配置为通过 GitHub Actions 自动部署到 GitHub Pages。

## 部署步骤

### 1. 修改配置文件

打开 `hugo.toml` 文件，修改以下内容：

```toml
author = "Your Name"  # 改为你的名字
baseURL = "https://yourusername.github.io/"  # 改为你的 GitHub 用户名
title = "我的博客"  # 改为你想要的网站标题

[params.social]
github = "https://github.com/yourusername"  # 改为你的 GitHub 地址
```

### 2. 创建 GitHub 仓库

1. 在 GitHub 上创建一个新仓库
2. 仓库名必须是：`yourusername.github.io`（将 `yourusername` 替换为你的 GitHub 用户名）
3. 可以设为公开（Public）或私有（Private，需要 GitHub Pro）

### 3. 推送代码到 GitHub

在项目目录下执行以下命令：

```bash
# 初始化 Git 仓库（如果还没有的话）
git init

# 添加所有文件
git add .

# 提交更改
git commit -m "Initial commit: Setup Hugo blog with Tokiwa theme"

# 添加远程仓库（替换为你的仓库地址）
git remote add origin https://github.com/yourusername/yourusername.github.io.git

# 推送到 GitHub（如果你的主分支是 main）
git branch -M main
git push -u origin main
```

### 4. 配置 GitHub Pages

1. 进入你的 GitHub 仓库页面
2. 点击 **Settings**（设置）
3. 在左侧菜单中找到 **Pages**
4. 在 **Source** 下，选择 **GitHub Actions**
5. 保存设置

### 5. 等待部署完成

- 推送代码后，GitHub Actions 会自动开始构建和部署
- 在仓库的 **Actions** 标签页可以看到部署进度
- 部署成功后，你的网站将在 `https://yourusername.github.io` 上线

## 本地预览

在本地预览网站效果：

```bash
# 安装 Hugo（如果还没有安装）
# macOS:
brew install hugo

# 运行本地服务器
hugo server -D

# 在浏览器中访问 http://localhost:1313
```

## 添加新文章

在 `content/post/` 目录下创建新的 Markdown 文件：

```bash
hugo new post/my-new-post.md
```

然后编辑文件，修改文章内容。

## 更新网站

每次修改文章或配置后：

```bash
git add .
git commit -m "Update content"
git push
```

GitHub Actions 会自动重新构建和部署你的网站。

## 主题自定义

本项目使用的是 Tokiwa 主题。你可以：

- 修改 `hugo.toml` 中的参数来自定义网站
- 在 `static/` 目录下添加自定义的静态文件
- 参考主题文档进行更多定制：https://github.com/heyeshuang/hugo-theme-tokiwa

## 故障排除

### 部署失败

1. 检查 **Actions** 标签页的错误日志
2. 确保 `hugo.toml` 配置正确
3. 确保 GitHub Pages 设置为 **GitHub Actions**

### 网站显示 404

1. 确保仓库名是 `yourusername.github.io` 格式
2. 等待几分钟让 DNS 生效
3. 检查 GitHub Pages 设置是否正确

### 样式丢失

1. 确保 `baseURL` 设置正确（必须以 `/` 结尾）
2. 确保部署脚本中的路径配置正确

## 目录结构

```
hugo-theme-tokiwa/
├── .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions 部署配置
├── content/                 # 文章内容
│   ├── post/               # 博客文章
│   ├── about.md            # 关于页面
│   └── _index.md           # 首页
├── static/                 # 静态文件
│   └── img/               # 图片
├── layouts/                # 主题布局文件
├── hugo.toml              # Hugo 配置文件
└── README_DEPLOYMENT.md   # 本文件
```

## 有用的资源

- [Hugo 官方文档](https://gohugo.io/documentation/)
- [Tokiwa 主题文档](https://github.com/heyeshuang/hugo-theme-tokiwa)
- [GitHub Pages 文档](https://docs.github.com/en/pages)
- [Markdown 语法](https://www.markdownguide.org/)

祝你使用愉快！🎉
