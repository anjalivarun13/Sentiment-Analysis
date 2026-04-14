# 🎬 IMDB Movie Review Sentiment Analysis using LSTM

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Deep Learning](https://img.shields.io/badge/DL-LSTM-brightgreen)
![NLP](https://img.shields.io/badge/NLP-Sentiment-yellow)
![Gradio](https://img.shields.io/badge/Gradio-Deployed-orange)
![Status](https://img.shields.io/badge/Project-Completed-success)
![Dataset](https://img.shields.io/badge/Dataset-IMDB-red)

---

## 🔍 Project Overview

A **Deep Learning & NLP based Sentiment Analysis system** that classifies movie reviews as **Positive or Negative** using an **LSTM (Long Short-Term Memory) model**.

The system is trained on the **IMDB Movie Review Dataset** and can analyze user-input reviews in real time through an interactive web interface.

---

## 🎯 Business Problem

Understanding customer sentiment is critical for:
- 🎬 Movie recommendation systems  
- 📊 Brand and product feedback analysis  
- 💬 Social media monitoring  

Challenges:
- Unstructured text data  
- Context understanding  
- Handling long reviews  

This system helps:
- ⚡ Automatically classify sentiment  
- 🧠 Capture context using LSTM  
- 📈 Improve decision-making  

---

## 🧠 ML Objective

Predict:
- Sentiment of review → **Positive / Negative**  
- Confidence based classification  

---

## 🧾 Dataset

- **IMDB Movie Review Dataset**  
- Contains labeled movie reviews:
  - Positive (1)  
  - Negative (0 → converted to 1 label format if needed)

---

## 🧹 Data Preprocessing

The text data is cleaned and transformed into machine-readable format.

### 🔧 Steps Performed

- Lowercasing text  
- Removing HTML tags  
- Cleaning unwanted characters  
- Label encoding (0 → 1 format if applied)  

---

## 📊 Data Processing Pipeline

Text → Cleaning → Tokenization → Sequence Conversion → Padding → Model Input

---

## 🔤 Text Processing

### 🔹 Tokenization
- Converts words into numerical tokens

### 🔹 Sequence Conversion
- Converts tokens into sequences

### 🔹 Padding
- Ensures equal input length for all sequences  

---

## 🤖 Model

This project uses a **Deep Learning Sequential Model with LSTM**.

### 📊 Architecture

- Embedding Layer  
- LSTM Layer  
- Dense Layer  
- Output Layer (Sigmoid)

---

## ⚙️ Training Pipeline

- Train-Test Split  
- Tokenizer fitting on training data  
- Sequence & padding  
- Model training using LSTM  

---

## 📈 Model Output Logic

- Output: Probability score  
- If output > 0.5 → Positive  
- If output < 0.5 → Negative  

---

## 💾 Model Saving

- Saved trained LSTM model  
- Saved tokenizer for inference  

---

## 🚀 Features

- 🎯 Real-time sentiment prediction  
- 🧠 Context-aware classification using LSTM  
- ⚡ Fast inference  
- 🌐 Interactive Gradio UI  
- 📊 Clean output display  

---

## 🛠 Technology Stack

- Frontend: Gradio  
- Backend: Python  
- DL Framework: TensorFlow / Keras  
- NLP: Tokenizer, Padding  
- Libraries: NumPy, Pandas  
- Deployment: Gradio  

---

## 🖥️ Gradio App Features

- Text input box  
- One-click prediction  
- Instant sentiment output  
- Simple and clean interface  

---

## 📸 Screenshots

### 🎯 Prediction Output
![Output](https://github.com/anjalivarun13/Sentiment-Analysis/blob/main/Screenshot/Positive%20Review.png)

![Output](https://github.com/anjalivarun13/Sentiment-Analysis/blob/main/Screenshot/Negative%20Review.png)

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/imdb-sentiment-analysis.git
cd imdb-sentiment-analysis
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
python app.py
```
--- 

## 🔮 Future Improvements
- Add multi-class sentiment (neutral)
- Use Bidirectional LSTM
- Try Transformer models (BERT)
- Improve accuracy with more data
- Deploy using FastAPI + Docker

---

## 👩‍💻 Author

**Anjali Varun**

GitHub: https://github.com/anjalivarun13

LinkedIn: https://www.linkedin.com/in/anjali-varun/
