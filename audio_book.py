import PyPDF2
import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def AudioBook(book):
    try:
        # Open the PDF file
        book = open(f"{book.lower()}.pdf", "rb")
        reader = PyPDF2.PdfReader(book)
        pages = len(reader.pages)
        print(f"Total Pages: {pages}")
        speak("Which page do you want to start from, sir? type the starting page number below: ")
        strt_page=int(input("page no: "))
        # Get user input via microphone
        
        # Read and speak the text
        for n in range(strt_page-1, pages):
            page = reader.pages[n]
            text = page.extract_text()
            speak(text)
            speak("do you want to continue sir?")
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source)  # Reduce ambient noise
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                word = r.recognize_google(audio).lower()
                print(f"You said: {word}")
                if "no" in word.lower():
                    exit() #stop reading book
                else:
                    continue #start reading from the next page
        
        book.close()
    
    except FileNotFoundError:
        print("The specified PDF file was not found.")
        speak("I couldn't find the file. Please check the name and try again.")
    except sr.RequestError as e:
        print(f"Could not request results; check your internet connection. Error: {e}")
        speak("There was an error with the internet connection.")
