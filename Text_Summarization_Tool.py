from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import nltk
import re
import warnings
import os

warnings.filterwarnings('ignore')

# BART Model and Tokenizer
bart_tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
bart_model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

# T5 Model and Tokenizer
t5_tokenizer = AutoTokenizer.from_pretrained("t5-small")
t5_model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")

def get_user_input():
    print("\n--- Text Summarization Tool ---")
    print("Choose input method:")
    print("1. Enter text manually")
    print("2. Upload a text file")

    choice = input("Enter 1 or 2: ")

    if choice == '1':
        text = input("\nPaste your long text below:\n")
    elif choice == '2':
        file_path = input("\nEnter the path of your .txt file: ")
        if not os.path.exists(file_path):
            print("File not found. Please check the path and try again.")
            return None
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        print("Invalid choice. Exiting...")
        return None

    return text

def preprocess_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^]*', '', text)  # Remove [brackets]
    text = re.sub(r'[^)]*', '', text)  # Remove (parentheses)
    text = text.strip()
    return text

# BART Summarization
def summarize_bart(text):
    inputs = bart_tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = bart_model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = bart_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# T5 Summarization
def summarize_t5(text):
    input_text = "summarize: " + text
    inputs = t5_tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = t5_model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = t5_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def main():
    text = get_user_input()
    if text is None:
        return

    text = preprocess_text(text)

    print("\n--- Generating Summary using BART ---")
    bart_summary = summarize_bart(text)
    print("\nBART Summary:\n", bart_summary)

    print("\n--- Generating Summary using T5 ---")
    t5_summary = summarize_t5(text)
    print("\nT5 Summary:\n", t5_summary)

if __name__ == "__main__":
    main()
  
