# 💼 Financial & Web Search Multi-Agent System (Phi SDK)

This project is a Python-based multi-agent assistant that fetches **financial data** and performs **web searches** using advanced AI models. Built with the **Phi SDK** and powered by **Groq's LLaMA 3**, this assistant helps you get real-time stock data, company news, and analyst insights in an easy-to-read format.

---

## 🧠 What It Does

- 📈 **Financial Agent**  
  Gets stock prices, fundamentals, news, and analyst recommendations using Yahoo Finance.

- 🌐 **Web Search Agent**  
  Searches the internet for relevant information using DuckDuckGo and summarizes it with sources.

- 🤝 **Multi-Agent Mode**  
  Both agents work together to answer complex queries with reliable, real-time data and formatted tables.

---

## 🔧 Technologies Used

- **Phi SDK**
- **Groq LLaMA 3 model**
- **Yahoo Finance Tools**
- **DuckDuckGo API**
- **Python 3.10+**
- **OpenAI (for API key handling)**

---

## 📌 Prerequisites

Make sure you have:

- Python 3.10 or higher installed
- A Groq-compatible model access (like LLaMA 3 via Groq)
- An OpenAI-compatible `.env` file with your API key

---

## 🛠️ Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/your-username/financial-agent.git
cd financial-agent
```

2. VENV
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set your API key in .env file

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

5. RUN
```bash
python financial_agent.py
```

---

## 🏆 Features
- Supports real-time stock analysis
- Automatically fetches latest news
- Uses Markdown tables for clear output
- Works with multiple agents using Phi’s team mode
