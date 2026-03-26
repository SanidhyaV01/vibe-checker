# 🧠 The Vibe Checker

> **AI-powered sentiment analysis — instantly tell if your text is giving positive or negative energy.**

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=flat-square&logo=streamlit)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=flat-square&logo=huggingface)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📌 What Is This?

**The Vibe Checker** is a simple, fun web app that uses a pre-trained AI model to analyze the sentiment of any text you type. Whether it's a tweet, a review, a message, or just a random thought — paste it in and find out if the vibe is ✅ Positive or ❌ Negative.

Built with **Streamlit** for the UI and **Hugging Face Transformers** (DistilBERT) for the AI backbone.

---

## 🚀 Live Demo

> Deployed on Streamlit Community Cloud  
> 🔗 **[your-app-link.streamlit.app](https://your-app-link.streamlit.app)** ← *(replace with your actual URL after deploying)*

---

## 🖼️ Features

- 🤖 **AI-Powered** — Uses a DistilBERT model fine-tuned on sentiment analysis
- ⚡ **Instant Results** — Get a label (Positive/Negative) with a confidence score
- 🎈 **Fun Feedback** — Balloon animation for positive vibes!
- 💾 **Cached Model** — Model loads once and stays in memory for fast repeated use
- 🧼 **Clean UI** — Simple, no-fuss Streamlit interface

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io) | Web app framework |
| [Hugging Face Transformers](https://huggingface.co/transformers/) | NLP / AI model |
| [DistilBERT](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) | Sentiment analysis model |
| Python 3.8+ | Language |

---

## 📦 Installation & Running Locally

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/vibe-checker.git
cd vibe-checker
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
vibe-checker/
│
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
└── README.md           # You're reading this!
```

---

## 📋 Requirements

```
streamlit
transformers
torch
```


## 🤝 Contributing

Pull requests are welcome! If you have ideas to improve the app (e.g., adding neutral sentiment, emotion detection, or multi-language support), feel free to open an issue or PR.

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Made with ❤️ by **[SanidhyaV01]([https://github.com/YOUR_USERNAME](https://github.com/SanidhyaV01/vibe-checker.git))**
