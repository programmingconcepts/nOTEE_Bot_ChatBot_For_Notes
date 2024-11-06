from docx import Document
from keybert import KeyBERT
import pandas as pd

# Loading Keybert
kw_model = KeyBERT()

document = Document("FireDetection.docx")

csv_file_path = "NewData.csv"

df = pd.read_csv(csv_file_path)

Title = ""
Heading1 = ""
Heading2 = ""
Heading3 = ""
Heading4 = ""
Heading5 = ""
Heading6 = ""


RecordHeadings = True

headings = []
texts = []

CurrentTopic = ""
CurrentText = ""
CurrentKeywords = ""

for paragraph in document.paragraphs:
    if (paragraph.style.name == "Normal" or paragraph.style.name == "List Paragraph"):
        if(RecordHeading):
            CurrentTopic = (Title + " " + Heading1 + " " + Heading2 + " " + Heading3 + " " + Heading4 + " " + Heading5 + " " + Heading6).strip()
            RecordHeading = False
        CurrentText += " " + paragraph.text
        keywords = kw_model.extract_keywords(paragraph.text, keyphrase_ngram_range=(1, 2))
        for element in keywords:
            if (float(element[1]) >= 0.5):
                CurrentKeywords += ", " + element[0]

    else:
        if(len(CurrentText) >= 1 and len(CurrentKeywords) >= 1 and len(CurrentTopic) >= 1):
            # Writing Topic, Keys and Text in .csv
            row = pd.DataFrame([[CurrentTopic, CurrentKeywords.strip(", "), CurrentText.strip()]], columns=['Topic', 'Keys', 'Text'])
            row.to_csv(csv_file_path, mode = 'a', index = False, header=False)

            print (CurrentTopic)
            print (CurrentText)
            print (CurrentKeywords)
            print()
            CurrentText = ""
            CurrentKeywords = ""
            CurrentText = ""

        if paragraph.style.name == "Title":
            Title = paragraph.text
            Heading1 = ""
            Heading2 = ""
            Heading3 = ""
            Heading4 = ""
            Heading5 = ""
            Heading6 = ""
            RecordHeading = True
        elif paragraph.style.name == "Heading 1":
            Heading1 = paragraph.text
            Heading2 = ""
            Heading3 = ""
            Heading4 = ""
            Heading5 = ""
            Heading6 = ""
            RecordHeading = True
        elif paragraph.style.name == "Heading 2":
            Title = ""
            Heading2 = paragraph.text
            Heading3 = ""
            Heading4 = ""
            Heading5 = ""
            Heading6 = ""
            RecordHeading = True
        elif paragraph.style.name == "Heading 3":
            Title = ""
            Heading1 = ""
            Heading3 = paragraph.text
            Heading4 = ""
            Heading5 = ""
            Heading6 = ""
            RecordHeading = True
        elif paragraph.style.name == "Heading 4":
            Title = ""
            Heading1 = ""
            Heading2 = ""
            Heading4 = paragraph.text
            Heading5 = ""
            Heading6 = ""
            RecordHeading = True
        elif paragraph.style.name == "Heading 5":
            Title = ""
            Heading1 = ""
            Heading2 = ""
            Heading3 = ""
            Heading5 = paragraph.text
            Heading6 = ""
            RecordHeading = True
        elif paragraph.style.name == "Heading 6":
            Title = ""
            Heading1 = ""
            Heading2 = ""
            Heading3 = ""
            Heading4 = ""
            Heading6 = paragraph.text
            RecordHeading = True