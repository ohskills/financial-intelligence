# GitHub 发布 - 快速参考

## 🚀 最快方法 (3分钟)

```bash
cd /home/ubuntu/.openclaw/workspace/skills/financial-intelligence
bash publish_to_github.sh
```

按提示操作即可!

---

## 📋 手动步骤

### 1. 创建 GitHub 仓库
- 访问: https://github.com/new
- 名称: `financial-intelligence`
- 公开 ✅
- 不初始化任何文件

### 2. 推送代码
```bash
cd /home/ubuntu/.openclaw/workspace/skills/financial-intelligence

git init
git branch -M main
git add .
git commit -m "feat: Financial Intelligence Agent v1.0.0"
git remote add origin https://github.com/你的用户名/financial-intelligence.git
git push -u origin main
```

### 3. 完成!
访问: `https://github.com/你的用户名/financial-intelligence`

---

## 📸 准备提交 ClawHub

### 需要准备:
- ✅ GitHub 仓库 URL
- ❓ 截图 (3张)
- ❓ 图标 (256x256, 可选)

### 截图生成:
```bash
python3 modules/news/fetch_financial_express.py 15
python3 modules/research/stock_analyzer.py 688110
```

截图保存到 `screenshots/` 并推送:
```bash
git add screenshots/
git commit -m "docs: 添加截图"
git push
```

---

## 🔑 认证问题

GitHub 不接受密码,使用 Personal Access Token:
1. https://github.com/settings/tokens
2. Generate new token (classic)
3. 勾选 `repo`
4. 复制 token 作为密码使用

---

## ✅ 检查清单

发布到 GitHub:
- [ ] 创建仓库
- [ ] 推送代码
- [ ] 验证文件完整

准备 ClawHub:
- [ ] README 清晰
- [ ] 截图准备
- [ ] 图标准备 (可选)

---

**详细指南**: 查看 `GITHUB_PUBLISH_GUIDE.md`
