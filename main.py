import speech_recognition as sr
import webbrowser
import pyttsx3
import audio_book #self
import pywhatkit
import os

# Initialize recognizer and speech engine
r = sr.Recognizer()
engine = pyttsx3.init()
songs=music_library.music

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    c = c.lower() 
    if "open google" in c or "open gogol" in c or "open googol" in c:
        webbrowser.open("https://www.google.com")

    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in c:
        webbrowser.open("https://www.facebook.com/")

    elif "open chatgpt" in c or "open chat gpt" in c:
        webbrowser.open("https://chatgpt.com/")

    elif "start calculator" in c:
        os.startfile("calc.exe")

    elif "start messenger" or "start mesengar" or "start messengar" or "start mesenger" in c:
        os.startfile(r"C:\program files\WindowsApps\FACEBOOK.317180B0BB486_2150.23.211.0_x64__8xx8rvfyw5nnt\app\Messenger.exe")

    #youtube
    elif c.startswith("play song"):
        speak("which song do you want to hear, Sir?")
        while True:
            try:
                with sr.Microphone() as source:
                        print("Listening....")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source, timeout=20, phrase_time_limit=20)
                    
                word = r.recognize_google(audio)
                c=word
                print("you said:",c)
                pywhatkit.playonyt(c)
                if "jarvis stop" or "jarvic stop" or "jarvice stop" or "jar stop" in c.lower():
                 speak("ok sir, exiting from this function")
                 break
                
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
            
            except sr.RequestError as e:
                print(f"Could not request results; check your internet connection. Error: {e}")

    #plya audio from audio book
    elif "play audio book" or "play audiobook" or "play odibook" or "play odi book" in c.lower():
        while True:
            try:
                speak("which book do you want to hear, Sir?")
                with sr.Microphone() as source:
                        print("Listening....")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source, timeout=20, phrase_time_limit=20)
                    
                word = r.recognize_google(audio)
                c=word
                print("you said: ",c)
                audio_book.AudioBook(word)
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
            
            except sr.RequestError as e:
                print(f"Could not request results; check your internet connection. Error: {e}")
            if "jarvis stop" or "jarvice stop" or "service stop" in c:
                speak("ok sir, exiting from the function")

    else:
        print(f"{c} not found")
        speak("command not found sir")
if __name__ == "__main__":
    speak("Hello sir, your machine is activated")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening....")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=20, phrase_time_limit=20)
            
            word = r.recognize_google(audio)
            
            if word.lower() == "hello jarvis" or "hello jar":
                speak("Yes sir. How can I help you?")
                
                with sr.Microphone() as source:
                    print("Listening....")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source, timeout=20, phrase_time_limit=20)
                
                command = r.recognize_google(audio)
                print("you said: ",command)
                process_command(command)
                if "exit" in command:
                    speak("ok sir turning off mechine")
                    break
            elif "exit" in command:
                speak("ok sir turning off mashin")
                break
            else:
                print("You said:", word)

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        
        except sr.RequestError as e:
            print(f"Could not request results; check your internet connection. Error: {e}")
            

