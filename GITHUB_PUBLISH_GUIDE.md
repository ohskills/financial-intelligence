# GitHub 发布步骤 - 详细指南

跟着这个指南一步步操作,5分钟发布到 GitHub!

---

## 🚀 方法 1: 使用自动化脚本 (最简单)

### 步骤 1: 创建 GitHub 仓库

1. 打开浏览器,访问: https://github.com/new

2. 填写信息:
   - **Repository name**: `financial-intelligence`
   - **Description**: `综合金融智能分析助手 - 新闻聚合 + 股票研究 + 技术分析`
   - **Public** (公开) ✅
   - **不要勾选** "Add a README file"
   - **不要勾选** "Add .gitignore"
   - **License**: 选择 "MIT License" (可选)

3. 点击 **"Create repository"**

4. 复制仓库 URL (在页面顶部):
   ```
   https://github.com/你的用户名/financial-intelligence.git
   ```

---

### 步骤 2: 运行发布脚本

在服务器上执行:

```bash
cd /home/ubuntu/.openclaw/workspace/skills/financial-intelligence

# 运行脚本
bash publish_to_github.sh
```

脚本会:
1. 初始化 Git
2. 添加所有文件
3. 创建提交
4. 要求你输入 GitHub 仓库 URL
5. 推送到 GitHub

---

## 🛠️ 方法 2: 手动操作 (完整控制)

### 步骤 1: 初始化 Git

```bash
cd /home/ubuntu/.openclaw/workspace/skills/financial-intelligence

# 初始化
git init
git branch -M main

# 配置用户信息 (首次使用需要)
git config user.name "你的名字"
git config user.email "your-email@example.com"
```

---

### 步骤 2: 添加文件

```bash
# 添加所有文件
git add .

# 检查状态
git status
```

应该看到所有文件被添加 (绿色)。

---

### 步骤 3: 创建提交

```bash
git commit -m "feat: Financial Intelligence Agent v1.0.0

📰 财经新闻聚合
- 20+ 新闻源支持 (财经慢报、CoinDesk、Bloomberg、Reuters 等)
- 自动分类与重要性评分
- 用户可自定义配置新闻源

📊 股票深度研究
- 实时行情获取 (AKShare)
- 10项技术指标分析 (MA, MACD, KDJ, BOLL, RSI, ATR, OBV)
- 资金流向监控
- 龙虎榜追踪
- 智能综合评分

🌍 多市场支持
- A股、美股、港股、加密货币

🎯 核心特性
- 完全免费 (无需 API Key)
- 开箱即用
- 用户可配置
- 完整中英文档 (15000+ 字)
- Mac/Linux 支持"
```

---

### 步骤 4: 创建 GitHub 仓库

(同方法 1 的步骤 1)

---

### 步骤 5: 关联远程仓库

```bash
# 替换为你的仓库 URL
git remote add origin https://github.com/你的用户名/financial-intelligence.git

# 验证
git remote -v
```

应该看到:
```
origin  https://github.com/你的用户名/financial-intelligence.git (fetch)
origin  https://github.com/你的用户名/financial-intelligence.git (push)
```

---

### 步骤 6: 推送到 GitHub

```bash
# 推送
git push -u origin main
```

如果要求输入凭据:
- **用户名**: 你的 GitHub 用户名
- **密码**: 使用 Personal Access Token (不是密码!)

**如何获取 Personal Access Token**:
1. 访问: https://github.com/settings/tokens
2. 点击 "Generate new token" → "Generate new token (classic)"
3. 勾选 `repo` (完整权限)
4. 生成并复制 token
5. 在命令行粘贴作为密码

---

## ✅ 验证发布

推送成功后:

1. 访问你的仓库: `https://github.com/你的用户名/financial-intelligence`

2. 检查文件:
   - ✅ README.md 显示在首页
   - ✅ 所有模块文件都在
   - ✅ LICENSE 文件存在
   - ✅ 文档完整

3. 检查提交历史:
   - 点击 "Commits"
   - 应该看到 "feat: Financial Intelligence Agent v1.0.0"

---

## 🎨 可选: 美化 README

GitHub 会显示 README.md 作为首页,确保它清晰易读:

```bash
# 检查 README 是否完整
cat README.md

# 如果需要修改
nano README.md  # 或 vim/其他编辑器

# 提交修改
git add README.md
git commit -m "docs: 更新 README"
git push
```

---

## 📸 准备截图

在发布到 ClawHub 前,需要截图:

### 生成输出

```bash
cd /home/ubuntu/.openclaw/workspace/skills/financial-intelligence

# 1. 新闻抓取
python3 modules/news/fetch_financial_express.py 15

# 2. 股票分析
python3 modules/research/stock_analyzer.py 688110

# 3. 龙虎榜
python3 modules/research/stock_with_dragon_tiger.py 688110
```

### 截图保存

将终端输出截图,保存为:
- `screenshots/news.png`
- `screenshots/analysis.png`
- `screenshots/dragon-tiger.png`

然后上传到 GitHub:

```bash
mkdir -p screenshots
# 把截图复制到 screenshots/ 目录

git add screenshots/
git commit -m "docs: 添加截图"
git push
```

---

## 🖼️ 准备图标 (可选)

如果你有图标 (256x256 PNG):

```bash
cp /path/to/your/icon.png icon.png
git add icon.png
git commit -m "docs: 添加图标"
git push
```

如果没有图标,可以暂时跳过,ClawHub 会使用默认图标。

---

## 🏷️ 创建 Release (可选但推荐)

在 GitHub 创建正式版本:

1. 访问: `https://github.com/你的用户名/financial-intelligence/releases`
2. 点击 "Create a new release"
3. 填写:
   - **Tag version**: `v1.0.0`
   - **Release title**: `v1.0.0 - Financial Intelligence Agent`
   - **Description**: 复制 CHANGELOG.md 的内容
4. 点击 "Publish release"

---

## 🎯 完成!

GitHub 发布完成后:

✅ 仓库地址: `https://github.com/你的用户名/financial-intelligence`

现在可以:
1. 把 GitHub URL 分享给别人
2. 提交到 ClawHub.ai
3. 在 Discord/Twitter 宣传

---

## 🚨 常见问题

### Q1: git push 要求输入密码

**A**: GitHub 不再支持密码认证,需要使用 Personal Access Token:
1. 访问: https://github.com/settings/tokens
2. 生成 token (勾选 `repo`)
3. 使用 token 作为密码

---

### Q2: 推送失败: "refusing to merge unrelated histories"

**A**: GitHub 仓库已有内容,需要合并:
```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

---

### Q3: 推送超时或失败

**A**: 网络问题,配置代理:
```bash
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890
```

---

### Q4: 想要修改提交信息

**A**: 修改最后一次提交:
```bash
git commit --amend -m "新的提交信息"
git push -f origin main  # 强制推送
```

---

## 📞 需要帮助?

如果遇到问题,在飞书 @ 我:
```
@小丽 GitHub 发布遇到问题: [描述问题]
```

---

**准备好了就开始吧!** 🚀

预计耗时: 5-10 分钟
