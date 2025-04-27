import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
import streamlit as st
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain

with open("C:\\Users\\Lenovo\\Desktop\\PROJECTS\\LLM\\Thinklet\\Response.json") as file:
    RESPONSE_JSON = json.load(file)

st.title("MCQ Generator using LangChain")

with st.form("user_inputs"):
    uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

    mcq_count=st.number_input("Number of MCQs", min_value=3, max_value=50)

    subject=st.text_input("Write Subject Name", max_chars=100)

    tone=st.text_input("Complexity level of questions", max_chars=50, placeholder="Simple")

    button=st.form_submit_button("Generate MCQs")

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Generating MCQs...."):
            response=None
            try:
                text=read_file(uploaded_file)
                response=generate_evaluate_chain.invoke(
                    {
                    "text": text, 
                    "number": mcq_count, 
                    "subject": subject, 
                    "tone": tone, 
                    "response_json": json.dumps(RESPONSE_JSON)
                    }
                )  
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error reading file. Please upload a valid PDF or TXT file.")
            if response is not None:  # ✅ Only process if response exists
                if isinstance(response, dict):
                    quiz = response.get("quiz", None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            st.write("table_data content:", table_data)
                            df = pd.DataFrame(table_data)
                            df.index = df.index + 1
                            st.table(df)
                            st.text_area(label="Review", value=response.get("review", ""))
                        else:
                            st.error("Error in the table data")
                    else:
                        st.error("Quiz not found in response")
                else:
                    st.write(response)