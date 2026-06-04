
import streamlit as st
import re
from datetime import datetime

# 页面配置
st.set_page_config(
    page_title="AI 日报生成器",
    page_icon="🤖",
    layout="wide"
)

# 自定义CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    .report-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        font-family: monospace;
        white-space: pre-wrap;
    }
    @media (max-width: 768px) {
        .main-header h1 { font-size: 1.5rem; }
    }
</style>
""", unsafe_allow_html=True)

class DailyReportGenerator:
    def __init__(self):
        self.keyword_map = {
            "今日完成": ["修复", "完成", "开发", "实现", "写了", "做了", "上线", "部署", 
                        "提交", "解决", "合并", "发布", "搞定", "学习", "阅读"],
            "进行中工作": ["正在", "进行", "继续", "优化", "重构", "调试", "处理"],
            "明日计划": ["明天", "计划", "准备", "安排", "规划", "即将", "打算"],
            "风险与备注": ["风险", "问题", "困难", "阻塞", "延迟", "注意"]
        }
    
    def generate(self, raw_text: str, report_type: str = "daily"):
        if not raw_text or len(raw_text.strip()) < 5:
            return {"success": False, "error": "输入内容太短"}
        
        sentences = re.split('[，,。；;！!？?、\n]', raw_text)
        categorized = {cat: [] for cat in self.keyword_map.keys()}
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
            assigned = False
            for category, keywords in self.keyword_map.items():
                if any(kw in sentence for kw in keywords):
                    categorized[category].append(f"- {sentence}")
                    assigned = True
                    break
            if not assigned:
                categorized["今日完成"].append(f"- {sentence}")
        
        output = []
        sections = ["今日完成", "进行中工作", "明日计划", "风险与备注"]
        for section in sections:
            if categorized[section]:
                unique = list(dict.fromkeys(categorized[section]))
                output.append(f"## {section}\n" + "\n".join(unique))
            else:
                output.append(f"## {section}\n- 无")
        
        return {
            "success": True,
            "report": "\n\n".join(output),
            "metadata": {"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        }

generator = DailyReportGenerator()

# 界面
st.markdown('<div class="main-header"><h1>🤖 AI 智能日报生成器</h1><p>让工作汇报更简单</p></div>', unsafe_allow_html=True)

# 侧边栏
with st.sidebar:
    st.title("⚙️ 设置")
    report_type = st.radio("报告类型", ["daily", "weekly"], format_func=lambda x: "日报" if x=="daily" else "周报")
    st.markdown("---")
    st.info("💡 提示：用逗号或句号分隔不同任务")

# 主输入区
input_text = st.text_area("📝 工作记录", height=200, placeholder="例如：修复登录bug，开会讨论需求，写技术文档")

col1, col2 = st.columns(2)
with col1:
    generate_btn = st.button("🚀 生成报告", type="primary", use_container_width=True)
with col2:
    clear_btn = st.button("🗑️ 清空", use_container_width=True)

if generate_btn and input_text:
    with st.spinner("生成中..."):
        result = generator.generate(input_text, report_type)
        if result["success"]:
            st.success("✅ 生成成功")
            st.markdown('<div class="report-box">' + result["report"].replace("\n", "<br>") + '</div>', unsafe_allow_html=True)
            st.download_button("📥 下载报告", result["report"], file_name=f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
        else:
            st.error(result["error"])
elif generate_btn:
    st.warning("请输入工作记录")

st.markdown("---")
st.markdown("<p style='text-align:center;color:gray'>📱 手机/电脑自适应 | 数据不上传</p>", unsafe_allow_html=True)
