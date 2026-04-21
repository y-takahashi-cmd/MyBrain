import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from docx import Document
doc = Document('C:/Users/y-takahashi/Downloads/クラウドパワー企業のオンライン保健室2025年12月月次報告書.docx')
for para in doc.paragraphs:
    if para.text.strip():
        print(para.text)
