#!/bin/bash

# GitHub Pages 快速部署脚本

echo "========================================="
echo "  GitHub Pages 部署助手"
echo "========================================="
echo ""

# 检查是否安装了 git
if ! command -v git &> /dev/null; then
    echo "❌ 错误：未安装 Git"
    echo "请先安装 Git: https://git-scm.com/downloads"
    exit 1
fi

# 检查是否是 git 仓库
if [ ! -d .git ]; then
    echo "📦 初始化 Git 仓库..."
    git init
    echo "✅ Git 仓库初始化完成"
    echo ""
fi

# 提示用户输入信息
echo "请输入你的 GitHub 用户名："
read github_username

if [ -z "$github_username" ]; then
    echo "❌ 错误：用户名不能为空"
    exit 1
fi

# 更新配置文件
echo ""
echo "📝 正在更新配置文件..."

# 使用 sed 更新 baseURL
sed -i.bak "s|baseURL = \"https://yourusername.github.io/\"|baseURL = \"https://${github_username}.github.io/\"|g" hugo.toml
sed -i.bak "s|github = \"https://github.com/yourusername\"|github = \"https://github.com/${github_username}\"|g" hugo.toml

# 删除备份文件
rm -f hugo.toml.bak

echo "✅ 配置文件更新完成"
echo ""

# 检查是否已经添加了远程仓库
if git remote | grep -q "origin"; then
    echo "⚠️  检测到已存在的远程仓库"
    git remote -v
    echo ""
    echo "是否要更新远程仓库地址？(y/n)"
    read update_remote
    if [ "$update_remote" = "y" ]; then
        git remote remove origin
        git remote add origin "https://github.com/${github_username}/${github_username}.github.io.git"
        echo "✅ 远程仓库地址已更新"
    fi
else
    echo "🔗 添加远程仓库..."
    git remote add origin "https://github.com/${github_username}/${github_username}.github.io.git"
    echo "✅ 远程仓库添加完成"
fi

echo ""
echo "📋 准备提交代码..."

# 添加所有文件
git add .

# 提交
echo "请输入提交信息（留空使用默认信息）："
read commit_message

if [ -z "$commit_message" ]; then
    commit_message="Initial commit: Setup Hugo blog with Tokiwa theme"
fi

git commit -m "$commit_message"

echo ""
echo "🚀 准备推送到 GitHub..."
echo ""
echo "请确保你已经在 GitHub 上创建了仓库："
echo "  仓库名：${github_username}.github.io"
echo "  地址：https://github.com/${github_username}/${github_username}.github.io"
echo ""
echo "是否继续推送？(y/n)"
read push_confirm

if [ "$push_confirm" = "y" ]; then
    # 检查当前分支
    current_branch=$(git branch --show-current)
    
    if [ -z "$current_branch" ]; then
        git branch -M main
        current_branch="main"
    fi
    
    echo "📤 推送到分支: $current_branch"
    git push -u origin $current_branch
    
    echo ""
    echo "========================================="
    echo "  ✅ 部署完成！"
    echo "========================================="
    echo ""
    echo "接下来的步骤："
    echo "1. 访问你的仓库：https://github.com/${github_username}/${github_username}.github.io"
    echo "2. 进入 Settings > Pages"
    echo "3. 在 Source 下选择 'GitHub Actions'"
    echo "4. 等待几分钟后访问：https://${github_username}.github.io"
    echo ""
    echo "查看部署状态："
    echo "https://github.com/${github_username}/${github_username}.github.io/actions"
    echo ""
else
    echo "❌ 已取消推送"
    echo ""
    echo "你可以稍后手动推送："
    echo "  git push -u origin main"
fi
