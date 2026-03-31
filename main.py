import PyPDF2
from transformers import pipeline

user_pdf = input("Enter the name of the PDF file you want to read which should be in the same directory: ")

pdf_file = open(user_pdf, 'rb')
content = []

reader = PyPDF2.PdfReader(pdf_file)

for page in reader.pages:
    text = (page.extract_text())
    if text:
        content.append(text)

result = " ".join(content)
chunks = [chunk[:300] for chunk in result.split(". ") if chunk.strip()]

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

search_query = input("Enter the topic you want to search for in the PDF: ")

labels = [search_query]
result_list = []

for chunk in chunks:
    try:
        if chunk.strip() == "" or not chunk:
            continue

        output = classifier(chunk, candidate_labels = [search_query])
        if output['scores'][0] >= 0.50:
            result_list.append(chunk)

    except Exception as e:
        continue

for i in result_list:
    print(i)
