
Overview:
This project leverages Python to create audiobooks from PDF files. It combines speech recognition and text-to-speech technologies to deliver an interactive experience. Users can convert and listen to their favorite PDF books in audio format. Two sample PDF books, revolution.pdf and english.pdf, are used in this repository.

Features:
AudioBook Conversion: Converts the text of PDF books into audio using the audiobook.py module.
Interactive Commands: Use voice commands to play audiobooks via the main.py script.
Additional Functionalities: Control web browsers, play YouTube songs, and perform other system-level actions through voice commands.
Prerequisites

Ensure the following libraries are installed:
speech_recognition
pyttsx3
webbrowser
pywhatkit
os

Install required libraries using pip:
pip install speechrecognition pyttsx3 pywhatkit

Usage:
Running the Program
Clone the repository.

Place revolution.pdf and english.pdf in the same directory as the scripts.

Run main.py to start the interactive voice-based audiobook application:
python main.py
Playing an Audiobook
Say: "Play audiobook".
The system will ask, "Which book do you want to hear?".
Specify either revolution or english as your choice.
The audiobook will start playing.

Additional Commands:
Open Google: "Open Google"
Open ChatGPT: "Open ChatGPT"
Play a song on YouTube: "Play song [song name]"
Start Calculator: "Start calculator"
Say: "Hello Jarvise" to activate the assistant.

File Descriptions:
main.py: The main script to run the interactive audiobook and execute voice commands.
audiobook.py: Module for converting PDF books into audio format.
revolution.pdf: Sample book included in the project.
english.pdf: Second sample book included in the project.

Example:
mathematica
Hello sir, your machine is activated.
Listening....
Yes sir. How can I help you?
Listening....
You said: Play audiobook.
Listening....
You said: Revolution.
[Audio playback starts for revolution.pdf]
Customization
You can extend this project by:

Adding more PDF books.
Enhancing the audiobook.py module to support more formats.
Integrating additional voice commands in main.py.

Contribution:
Feel free to fork this repository and contribute by submitting pull requests for bug fixes or new features.