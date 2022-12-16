import pyttsx3
import datetime
import wikipedia
import pywhatkit
import speech_recognition as sr

# Receiving the audio command from the user
voice = sr.Recognizer()
engine = pyttsx3.init()


# Talk to the user by greeting & ask what they need help with
def talk_back(text):
    engine.say(text)
    engine.runAndWait()

# Greeting command & introduction
talk_back('Hi, I am Clement. Welcome to my command center')
talk_back('How can I help you')
print("\nListening....")


def speaker():
    with sr.Microphone() as source:
        audio = voice.listen(source)
        voice.adjust_for_ambient_noise(source)
        text = voice.recognize_google(audio)
        # ------------------------------------------------
        command = voice.recognize_google(audio)
        command = command.lower()

    # Conditional statement to check if the mention command
    if 'play' in command:
        song = command.replace('play', '')
        talk_back('Got it' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk_back(time + " is the current time in your area!")
        talk_back("Is there anything you need help with?")
    
    # Handle multiple commands send to by the user
    elif "who" in command or "what" in command or "how" in command or "when" in command:
        summary = wikipedia.summary(text)
        print(text)
        print(summary, "\n")
        talk_back(summary)
    
    else:
        talk_back("I don't quite understand your command")

speaker()
