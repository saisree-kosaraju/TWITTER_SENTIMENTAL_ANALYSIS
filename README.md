---

## ✨ Overview

**SentimentIQ** is a web-based sentiment analysis tool built for exploring how people feel about brands, topics, or entities on Twitter. Upload your own dataset or use the built-in sample, and instantly get a rich, visual breakdown of sentiment — positive, negative, and neutral — powered by VADER and classic ML models.

## 🚀 Features

- **📈 Interactive Dashboard** — Visualize sentiment distribution, trends, and entity-level breakdowns with dynamic Plotly charts and word clouds.
- **🔍 Analyze Tweet** — Run sentiment analysis on any custom tweet or text input in real time.
- **🤖 AI Chatbot** — Ask natural-language questions about your dataset and get conversational insights.
- **📂 Custom CSV Upload** — Bring your own tweet dataset (`entity`, `label`, `tweet` columns) or use the sample dataset included in the repo.
- **🎨 Custom Styling** — Polished UI with custom CSS for a clean, modern look.

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| **Frontend / App Framework** | [Streamlit](https://streamlit.io/) |
| **Data Processing** | Pandas, NumPy |
| **Sentiment Analysis** | NLTK, VADER Sentiment |
| **Machine Learning** | scikit-learn, Joblib |
| **Visualization** | Plotly, Matplotlib, WordCloud |

## 📁 Project Structure

```
TWITTER_SENTIMENTAL_ANALYSIS/
├── app.py                 # Main Streamlit entry point
├── assets/                # Static assets (custom CSS, images)
├── components/            # Reusable UI components (e.g., sidebar)
├── data/                  # Sample dataset (tweets.csv)
├── models/                # Trained ML models / model artifacts
├── views/                 # App pages (Dashboard, Analyze, Chatbot)
├── requirements.txt       # Python dependencies
└── README.md
```

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/saisree-kosaraju/TWITTER_SENTIMENTAL_ANALYSIS.git
   cd TWITTER_SENTIMENTAL_ANALYSIS
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data** (required for VADER, first run only)
   ```python
   import nltk
   nltk.download('vader_lexicon')
   ```

## ▶️ Usage

Run the Streamlit app locally:

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`.

- Use the **sidebar** to upload your own CSV file, or leave it empty to use the sample dataset (`data/tweets.csv`).
- If uploading a custom file, ensure it includes columns for **entity**, **label**, and **tweet** text.
- Navigate between **Dashboard**, **Analyze Tweet**, and **AI Chatbot** using the sidebar menu.

## 📊 Data Format

The app expects a CSV with at least the following columns:

| Column | Description |
|---|---|
| `entity` | The subject/brand/topic the tweet refers to |
| `label` | Sentiment label (e.g., Positive, Negative, Neutral) |
| `tweet` | The tweet text content |

## 🗺️ Roadmap

- [ ] Add support for real-time tweet fetching via API
- [ ] Expand chatbot with more advanced NLP capabilities
- [ ] Add model comparison and accuracy metrics view
- [ ] Deploy live demo on Streamlit Community Cloud

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 👤 Author

**Saisree Kosaraju**
[GitHub](https://github.com/saisree-kosaraju)

---
