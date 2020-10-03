import pyttsx3
import PyPDF2

book = open("sample.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("No. of pages: ", pages)
speaker = pyttsx3.init()
for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    print("Reading: ", text)
    speaker.runAndWait()
