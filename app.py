import streamlit as st
import re
from datetime import datetime

st.set_page_config(page_title="AI 日报生成器", page_icon="🤖", layout="wide")

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
</style>
""", unsafe_allow_html=True)

class DailyReportGenerator:
    def __init__(self):
        self.keyword_map = {
            "今日完成": ["修复", "完成", "开发", "实现", "写了", "做了", "上线", "部署", "提交", "解决"],
            "进行中工作": ["正在", "进行", "继续", "优化", "重构", "调试"],
            "明日计划": ["明天", "计划", "准备", "安排", "规划"],
            "风险与备注": ["风险", "问题", "困难", "阻塞", "延迟"]
        }
    
    def generate(self, raw_text: str, report_type: str = "daily"):
        if not raw_text or len(raw_text.strip()) < 5:
            return {"success": False, "error": "输入内容太短，请提供更详细的工作记录", "report": None}
        
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

st.markdown('<div class="main-header"><h1>🤖 AI 智能日报生成器</h1><p>让工作汇报更简单</p></div>', unsafe_allow_html=True)

with st.sidebar:
    st.title("⚙️ 设置")
    report_type = st.radio("报告类型", ["daily", "weekly"], format_func=lambda x: "日报" if x=="daily" else "周报")
    st.info("💡 提示：用逗号或句号分隔不同任务")

input_text = st.text_area("📝 工作记录", height=200, placeholder="例如：修复登录bug，开会讨论需求，写技术文档")

if st.button("🚀 生成报告", type="primary"):
    if input_text:
        with st.spinner("生成中..."):
            result = generator.generate(input_text, report_type)
            if result["success"]:
                st.success(f"✅ 生成成功 {result['metadata']['timestamp']}")
                st.markdown("### 📄 生成的报告")
                st.markdown(result["report"])
                st.download_button(
                    label="📥 下载报告",
                    data=result["report"],
                    file_name=f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                    mime="text/markdown"
                )
            else:
                st.error(f"❌ {result['error']}")
    else:
        st.warning("⚠️ 请输入工作记录")

st.markdown("---")
st.markdown("<p style='text-align:center;color:gray'>📱 手机/电脑自适应 | 🔒 数据不上传 | 🚀 完全免费</p>", unsafe_allow_html=True)
