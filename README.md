# Thniklet : An MCQ Generator Using Langchain and Gemini-2.0 Flash Model

Thinklet is an MCQ Generator built using Python, Streamlit UI, Langchain and Gen AI model Gemini 2.0 Flash.

# Features
- A simple UI built using Streamlit for MCQ Generation.
- The site uses Langchain with two LLM chains for generating answer to the MCQ and validation of the answer.
- Internally, it uses Gemini-2.0-Flash model for generation of possible MCQ questions.
- At first, the user needs to upload a PDF or TXT file data file for getting the content on which the MCQ is to be generated.
- Then, the user provides the name of the Subject, number of questions and the tone of questions.
- The Gemini Model works internally and then generates set of questions along with answers.

# Project Setup Guide
- Clone the repo : ```https://github.com/Rishav123raj/Thinklet```
- ```cd Thinklet```
- ```pip install requirements.txt```
- Create a .env file including your GOOGLE_API_KEY
- Run : ```streamlit run StreamlitAPP.py```
