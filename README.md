# TEXT-SUMMARIZATION-TOOL5

COMPANY CODTECH IT SOLUTIONS

NAME: KONDA KRISHNAVENI 

INTERN ID: ID:CODF46

ARTIFICIAL INTELLIGENCE MARKUP LANGUAGE 

DURATION: 4 WEEEKS

MENTOR: NEELA SANTOSH

As part of the CodTech AIML Internship, Task 1 focused on building a practical and real-world applicable NLP project: a Text Summarization Tool. The main objective of this project was to condense large paragraphs or documents into short, meaningful summaries using modern transformer-based models. Text summarization is a highly relevant application of Natural Language Processing (NLP) that is widely used across industries such as journalism, education, law, and business, where reading large amounts of text is time-consuming and challenging.

The project involved several key tasks. Initially, I imported the necessary Python libraries such as transformers, torch, and nltk. The transformers library by Hugging Face was central to this project, as it provides pre-trained state-of-the-art models like BART and T5 that are capable of performing abstractive summarization. These models understand the context of a given paragraph and generate an entirely new summary, rather than simply picking out sentences from the original content.

To make the tool user-friendly, I implemented two input options: the user can either manually enter a long text, or they can upload a .txt file containing the content they want to summarize. This adds flexibility for different use cases and makes the tool more accessible. After accepting the input, the tool optionally performs preprocessing, which includes cleaning the text by removing unnecessary whitespaces, brackets, and special characters to improve summarization accuracy.

For the summarization task itself, I used both BART (facebook/bart-large-cnn) and T5 (t5-small). These models were loaded from Hugging Face’s model hub. BART is known for its bidirectional and auto-regressive nature, making it excellent at generating fluent summaries. T5, on the other hand, treats every NLP problem as a text-to-text transformation task, and it was also effective in creating concise outputs. Using both models allowed for comparison and flexibility in selecting the preferred summary.

Once the text was summarized, the results were printed clearly for the user to read. The final script was created and tested in Google Colab, which was an ideal choice due to its browser-based setup, ease of use on mobile, and support for GPU-based execution. The final code was exported as a .py file to meet the project submission requirements and uploaded to GitHub for version control and review.

This tool demonstrates a practical use of NLP in making large text content more digestible. It can be applied in real-world scenarios such as summarizing news articles, legal documents, educational material, business reports, and customer feedback. The project not only strengthened my understanding of transformer models but also gave me hands-on experience in integrating AI models into real tools.

Overall, this task was a great learning experience. I learned how to build an end-to-end NLP application, use pre-trained models, handle user input, and work with GitHub for sharing code. It gave me a strong foundation for further exploration in Natural Language Processing and real-world AI Project

![Image](https://github.com/user-attachments/assets/b2883c2b-ca92-46cc-8c5a-2c12d87d3021)
