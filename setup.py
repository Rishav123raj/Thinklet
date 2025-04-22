from setuptools import setup, find_packages

setup(
    name="mcqgenerator",
    version="0.1.0",
    author="Rishav Raj Bhagat",
    author_email="rishavrajbhagat123@gmail.com",
    description="A package to generate MCQs from text using Gemini's 2.o-flash model.",
    install_requires=["google-generativeai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)