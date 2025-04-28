# Thinklet : An MCQ Generator Using Langchain and Gemini-2.0 Flash Model

Thinklet is an MCQ Generator built using Python, Streamlit UI, Langchain and Gen AI model Gemini 2.0 Flash.

# Features
- A clean and interactive user interface is developed using Streamlit to facilitate seamless MCQ generation.
- The system employs LangChain with a dual-chain architecture — one chain for answer generation and another for answer validation.
- Google Gemini-2.0 Flash model serves as the core LLM backend, responsible for creating high-quality MCQ questions.
- Users can upload PDF or TXT files containing the content from which questions are to be generated.
- After uploading, users specify the Subject Name, desired number of questions, and the tone/style of the MCQs.
- The model processes the input and generates a set of well-structured MCQs along with validated answers.

# Project Setup Guide
- Clone the repo : ```https://github.com/Rishav123raj/Thinklet```
- ```cd Thinklet```
- ```pip install -r requirements.txt```
- Create a .env file including your GOOGLE_API_KEY
- Run : ```streamlit run StreamlitAPP.py```

# Requirements
- Python latest version
- Google Gemini Access with API Key
- Langchain installation
