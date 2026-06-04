# 🤖 AI 智能日报/周报生成器

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-iOS%20%7C%20Android%20%7C%20Web-lightgrey.svg)

**一个基于 Streamlit 的智能日报/周报生成工具，手机电脑都能用，无需安装任何软件。**

[![在线使用](https://img.shields.io/badge/🌐-在线使用-0077FF?style=for-the-badge)](https://report-generator-daisyzhao21.streamlit.app)
[![GitHub](https://img.shields.io/badge/📦-GitHub-181717?style=for-the-badge)](https://github.com/Daisyzhao21/Report_Generator)

</div>

---

## ✨ 在线使用

> **无需安装任何软件，手机电脑都能用！**

👉 **[点击这里直接使用](https://report-generator-daisyzhao21.streamlit.app)**

或者复制链接到浏览器：https://report-generator-daisyzhao21.streamlit.app


### 📱 手机使用
1. 打开手机浏览器（微信、Safari、Chrome 均可）
2. 输入上方链接
3. 开始使用！（界面会自动适配手机屏幕）

---

## 🎯 功能特点

| 功能 | 说明 |
|------|------|
| 📱 **响应式设计** | 手机、平板、电脑完美适配，自动调整布局 |
| 🎯 **智能分类** | 自动识别工作内容并分类到对应栏目 |
| 📊 **日报/周报** | 一键切换日报和周报两种格式 |
| 💾 **导出功能** | 支持下载 Markdown 格式报告 |
| 🔒 **隐私安全** | 数据不上传，完全在浏览器本地处理 |
| 🚀 **无需安装** | 打开链接即用，无需注册登录 |

---

## 📝 使用示例

### 输入
修复了登录页面的bug
下午和产品经理开了需求评审会
学习了Docker容器化部署
明天准备代码评审


### 输出（日报格式）

```markdown
## 今日完成
- 修复了登录页面的bug
- 下午和产品经理开了需求评审会
- 学习了Docker容器化部署

## 进行中工作
- 无

## 明日计划
- 明天准备代码评审

## 风险与备注
- 无

🛠️ 本地运行
如果你想在本地运行或二次开发：

1. 克隆仓库
git clone https://github.com/Daisyzhao21/Report_Generator.git
cd Report_Generator

2. 安装依赖
bash
pip install -r requirements.txt
3. 运行应用
bash
streamlit run app.py
4. 访问应用
本地访问：http://localhost:8501

局域网访问：http://你的IP:8501


📂 项目结构
text
Report_Generator/
├── app.py                    # Streamlit 主应用
├── requirements.txt          # Python 依赖
├── report_gen.py             # 核心生成器类
├── Demo_Report_Generator.ipynb  # Jupyter 演示
├── README.md                 # 项目说明
└── .gitignore               # Git 忽略文件

🔧 技术栈
技术	用途
Python 3.10	核心逻辑
Streamlit 1.28+	Web 界面框架
Pandas	数据处理
正则表达式	文本分类


📊 智能分类规则
系统会根据关键词自动分类：

分类	关键词示例
今日完成	修复、完成、开发、实现、写了、上线、部署
进行中工作	正在、进行、继续、优化、重构
明日计划	明天、计划、准备、安排、规划
风险与备注	风险、问题、困难、阻塞、延迟


🚀 部署（供开发者参考）
本项目已部署在 Streamlit Cloud：

推送代码到 GitHub

登录 Streamlit Cloud

选择仓库 Daisyzhao21/Report_Generator

设置主文件为 app.py

自动部署完成

后续优化建议
增加 AI API 支持：配置 OpenAI/通义千问，让报告更智能

添加用户认证：让团队成员有独立的报告历史

数据库存储：保存历史报告，支持查询和统计

定时提醒：每天下午 6 点提醒写日报



📄 开源协议
MIT License - 随意使用、修改、分享

🤝 贡献
欢迎提交 Issue 和 Pull Request！

Fork 本项目

创建你的分支 (git checkout -b feature/AmazingFeature)

提交修改 (git commit -m 'Add some AmazingFeature')

推送到分支 (git push origin feature/AmazingFeature)

打开 Pull Request

📧 联系方式
GitHub: @Daisyzhao21

项目链接: https://github.com/Daisyzhao21/Report_Generator

⭐ 支持
如果这个项目对你有帮助，欢迎点个 Star ⭐

<div align="center">
Made with ❤️ by Daisy | Powered by Streamlit

https://img.shields.io/badge/%E2%AC%86%EF%B8%8F-%E5%9B%9E%E5%88%B0%E9%A1%B6%E9%83%A8-0077FF?style=flat-square

</div> ```
