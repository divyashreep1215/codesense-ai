# 💡 CodeSense AI

An AI-powered code analysis and review platform built with Streamlit and Groq LLM. CodeSense AI analyzes your code for structure, complexity, and quality — then uses AI to generate human-readable feedback, all through an interactive web interface.

🔗 **Live Demo:** https://codesense-ai-igudsesvrjumlv9phgjeck.streamlit.app/

---

## ✨ Features

- **Multi-Language Support** — Upload or paste code in Python, Java, C++, JavaScript, HTML, or CSS
- **Static Code Analysis** — Parses code structure and detects functions, classes, loops, and conditionals
- **Complexity Scoring** — Calculates a static complexity score for the submitted code
- **AI-Powered Review** — Uses Groq's LLM to generate contextual feedback and suggestions on code quality
- **Context-Aware Chatbot** — Ask coding questions, with the AI referencing your uploaded code for context
- **Overall Quality Score** — Combines pattern detection and complexity into a single score metric
- **Performance Dashboard** — Visualizes score history across analysis sessions
- **PDF Report Export** — Download a full analysis report as a PDF via ReportLab

---

## 🛠 Tech Stack

| Category      | Technology              |
|----------------|--------------------------|
| Frontend       | Streamlit                |
| AI Backend     | Groq LLM API              |
| Model Used     | openai/gpt-oss-20b        |
| PDF Engine     | ReportLab                 |
| Environment    | python-dotenv              |
| Data Handling  | Pandas, NumPy               |
| Visualization  | Plotly                       |
| Language       | Python                        |

---

## 📂 Project Structure

```
codesense-ai/
├── app.py                          # Main Streamlit application
├── analyzer/
│   ├── parser.py                    # Code parsing logic
│   ├── pattern_detector.py          # Detects functions, classes, loops, conditionals
│   ├── static_complexity.py         # Static complexity scoring
│   ├── scorer.py                    # Overall quality score calculation
│   ├── llm_analyzer.py              # Groq LLM integration for AI review & chatbot
│   └── report_generator.py          # Report generation logic
├── utils/
│   ├── dashboard_utils.py           # Score history visualization
│   ├── pdf_generator.py             # PDF report generation
│   └── prompts.py                   # AI prompt templates
├── requirements.txt
├── .env                              # Environment variables (not committed)
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A [Groq API key](https://console.groq.com)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/divyashreep1215/codesense-ai.git
   cd codesense-ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the project root:
   ```
   GROQ_API_KEY="your_groq_api_key_here"
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

   The app will open in your browser at `http://localhost:8501`

---

## 🎮 How to Use

1. Upload a code file (`.py`, `.java`, `.cpp`, `.js`, `.html`, `.css`, `.txt`) or paste code directly into the sidebar
2. View the automatic analysis: parsed structure, detected patterns, and static complexity score
3. Read the AI-generated feedback on code quality and potential improvements
4. Check your **Overall Score** and track it over time on the performance dashboard
5. Download a full **PDF report** of the analysis
6. Use the built-in **chatbot** to ask questions about your code or general coding concepts

---

## 🔒 Environment Variables

| Variable        | Description                          |
|------------------|----------------------------------------|
| `GROQ_API_KEY`   | Your API key from Groq, used to power AI analysis and chat |

> ⚠️ Never commit your real `.env` file with a live API key. Add `.env` to your `.gitignore` before pushing.

---

## 🤝 Contributing

Contributions are welcome! Fork the repo, create a feature branch, and open a pull request with your changes.

---



## 👤 Author

**Divyashree P**
- GitHub: [@divyashreep1215](https://github.com/divyashreep1215)
- LinkedIn: [divyashreep1215](https://www.linkedin.com/in/divyashreep1215)
- Email: divyashreep2004@gmail.com
