![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-F9AB00?style=for-the-badge&logo=huggingface&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Welcome to the **AI Conversational Agent Playground**! This repository provides a simple, clean, and highly customizable chatbot application built using **Streamlit**, **LangChain**, and **HuggingFace's** powerful open-source large language models (LLMs).

Whether you want to interact with the model via a sleek web interface or experiment with raw code in a Jupyter Notebook, this project has you covered!

---

## ✨ Features

- **Interactive Web Interface:** A fully functional chat UI built with Streamlit.
- **State-of-the-Art Models:** Defaulted to `Qwen/Qwen2.5-72B-Instruct`, but easily swappable with Llama 3.3, DeepSeek R1, Mistral, or Phi-4.
- **Conversational Memory:** Uses LangChain's message handling (`SystemMessage`, `HumanMessage`, `AIMessage`) to maintain chat history and context.
- **Notebook Prototyping:** Includes a Jupyter Notebook for rapid testing, inference, and model comparison.

---

## 📂 Project Structure

```text
📦 repository
 ┣ 📜 simple-converstaional-agent-app.py   # The Streamlit web application UI
 ┣ 📜 Conversational-chatbot.ipynb         # Jupyter notebook for testing & model prototyping
 ┗ 📜 README.md                            # You are here!

```

---

## 🚀 Step-by-Step Quickstart Guide

### 1. Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.8+**
* A **HuggingFace Account** and an [Access Token](https://huggingface.co/settings/tokens) (Note: Keep this token secret! Never commit it to GitHub).

### 2. Clone the Repository

```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

```

### 3. Set Up a Virtual Environment (Recommended)

It's always best practice to use a virtual environment to manage your dependencies.

```bash
python -m venv env
source env/bin/activate  # On Windows use: env\\Scripts\\activate

```

### 4. Install Dependencies

Install the required packages using pip:

```bash
pip install streamlit langchain-core langchain-huggingface jupyter

```

### 5. Set Your HuggingFace API Token

You need to provide your HuggingFace API token for the models to work.

**For the Streamlit App:**
Open `simple-converstaional-agent-app.py` and replace the placeholder with your actual token (or better yet, set it as an environment variable in your OS):

```python
import os
os.environ['HUGGINGFACEHUB_API_TOKEN'] = 'hf_your_actual_token_here' 

```

*(⚠️ **Security Warning:** Do not push your actual API token to GitHub!)*

### 6. Run the Application! 🎉

Launch the Streamlit web interface by running:

```bash
streamlit run simple-converstaional-agent-app.py

```

This will open a new tab in your default web browser where you can start chatting with your AI assistant!

---

## 🧪 Exploring the Jupyter Notebook

If you want to test different models without running the UI, open the provided Jupyter Notebook:

```bash
jupyter notebook Conversational-chatbot.ipynb
```

Inside, you'll find pre-configured setup steps to test out some of the best open-source models available on HuggingFace:

* `Qwen/Qwen2.5-72B-Instruct` (Default)
* `deepseek-ai/DeepSeek-R1`
* `meta-llama/Llama-3.3-70B-Instruct`
* `mistralai/Mistral-Small-3.1-24B-Instruct-2503`
* `microsoft/phi-4`

Simply swap out the `repo_id` in the `HuggingFaceEndpoint` configuration to try a new model!

---

## 🛠️ Customization

Want to change how the AI behaves? Modify the `SystemMessage` in the Streamlit app:

```python
# Change this line in simple-converstaional-agent-app.py
SystemMessage(content="You are a sarcastic but helpful AI assistant.")
```

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

You can download the generated `README.md` file using the link above and drop it directly into your project directory before pushing to GitHub!

```
