import os
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            raise Exception("Error reading PDF file")
        
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    else:
        raise Exception("Unsupported file format. Please upload a PDF or TXT file.")  


def get_table_data(quiz_str):
    try:
        # Ensure quiz_str is a string
        quiz_dict=json.loads(quiz_str)
        quiz_table_data=[]

        for key, value in quiz_dict.items():
            # Safely access dictionary keys using get(), with default values
            mcq = value["mcq"]
            options = " || ".join(
                [
                    f"{option} -> {option_value}" for option, option_value in value["options"].items()
                ]
            )
            correct = value["correct"]
            quiz_table_data.append(
                {
                    "MCQ": mcq, 
                    "Options": options, 
                    "Correct": correct
                }
            )

        return quiz_table_data
    
    except Exception as e:
        # Print detailed error traceback for debugging
        traceback.print_exception(type(e), e, e.__traceback__)  
        return []  # Return an empty list to signify an error
