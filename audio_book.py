# pip install PyPDF2
import PyPDF2
import pyttsx3

book = open("book1.pdf", "rb")
reader = PyPDF2.PdfReader(book)
pages = len(reader.pages) 
print(f"Total Pages: {pages}")
speaker = pyttsx3.init()
for n in range(7, pages):
    page = reader.pages[n] 
    text = page.extract_text() 
    speaker.say(text)  
    speaker.runAndWait()
book.close()