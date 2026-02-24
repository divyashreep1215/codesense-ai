import streamlit as st
from analyzer.llm_analyzer import analyze_code_with_ai, chat_with_ai
from analyzer.static_complexity import calculate_complexity
from analyzer.pattern_detector import detect_patterns
from analyzer.scorer import calculate_score
from analyzer.parser import parse_code
from utils.dashboard_utils import plot_score_history
import pandas as pd

st.set_page_config(page_title="CodeSense AI (Groq)", layout="wide")
st.title("💡 CodeSense AI – Groq Powered Code Review & Chatbot")

# Session states
if 'history' not in st.session_state:
    st.session_state['history'] = pd.DataFrame(columns=['Score','Functions','Classes','Loops','Conditionals','Complexity'])
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# ---------------- Upload / Paste Code ----------------
uploaded_file = st.sidebar.file_uploader("Upload code file", type=['py','java','cpp','js','html','css','txt'])
code_input = st.sidebar.text_area("Or paste your code here:")

if uploaded_file:
    code = uploaded_file.read().decode("utf-8")
elif code_input:
    code = code_input
else:
    code = None

# ---------------- Code Analysis ----------------
if code:
    st.subheader("🔍 Code Analysis Results")
    parsed = parse_code(code)
    st.write(parsed)

    patterns = detect_patterns(code)
    st.write(patterns)

    complexity = calculate_complexity(code)
    st.write(f"Static Complexity Score: {complexity}")

    ai_feedback = analyze_code_with_ai(code)
    st.write(ai_feedback)

    score = calculate_score(code, patterns, complexity)
    st.metric("Overall Score", score)

    st.session_state['history'] = pd.concat([
        st.session_state['history'],
        pd.DataFrame([{
            'Score': score,
            'Functions': len(patterns.get('functions',[])),
            'Classes': len(patterns.get('classes',[])),
            'Loops': len(patterns.get('loops',[])),
            'Conditionals': len(patterns.get('conditionals',[])),
            'Complexity': complexity
        }])
    ], ignore_index=True)

    st.subheader("📊 Performance Dashboard")
    plot_score_history(st.session_state['history'])

    if st.button("📄 Download PDF Report"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "CodeSense AI Report", ln=True, align="C")
        pdf.set_font("Arial", "", 12)
        pdf.ln(5)
        pdf.multi_cell(0, 10, f"Code:\n{code}")
        pdf.ln(5)
        pdf.multi_cell(0, 10, f"Parsed:\n{parsed}")
        pdf.ln(5)
        pdf.multi_cell(0, 10, f"Patterns:\n{patterns}")
        pdf.ln(5)
        pdf.multi_cell(0, 10, f"Static Complexity: {complexity}")
        pdf.ln(5)
        pdf.multi_cell(0, 10, f"AI Feedback:\n{ai_feedback}")
        pdf.ln(5)
        pdf.multi_cell(0, 10, f"Overall Score: {score}")
        filename = "CodeSenseAI_Report.pdf"
        pdf.output(filename)
        st.success("PDF Ready!")
        st.download_button("Download PDF", filename)

# ---------------- Context-Aware Chatbot ----------------
st.subheader("💬 AI Chatbot for Coding Help")
user_question = st.text_input("Ask a coding question or about your code:")

if st.button("Send") and user_question:
    # Pass the uploaded code as context
    code_context = code if code else None
    response = chat_with_ai(user_question, code_context)
    st.session_state['chat_history'].append(("You", user_question))
    st.session_state['chat_history'].append(("AI", response))

# Display chat history
for speaker, text in st.session_state['chat_history']:
    if speaker == "You":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**AI:** {text}")
