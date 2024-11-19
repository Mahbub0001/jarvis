import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import audio_book

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
    
    elif c.startswith("play"):
        song_name = c.split(" ", 1)[1]
        link = music_library.music(song_name)
        if link:
            webbrowser.open(link)
            print(f"Playing '{song_name}'")
        else:
            print(f"Song '{song_name}' not found in music library.")


if __name__ == "__main__":
    speak("Hello sir, your machine is activated")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening....")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=True, phrase_time_limit=True)
            
            word = r.recognize_google(audio)
            
            if word.lower() == "hello jarvis":
                speak("Yes sir. How can I help you?")
                
                with sr.Microphone() as source:
                    print("Listening....")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source, timeout=True, phrase_time_limit=True)
                
                command = r.recognize_google(audio)
                process_command(command)
            else:
                print("You said:", word)

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        
        except sr.RequestError as e:
            print(f"Could not request results; check your internet connection. Error: {e}")
            

