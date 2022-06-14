import datetime
from email.mime import audio
from logging import exception
import os
from tokenize import Special
# text = 'hello world , saifdin is dado '
# os.system('espeak "{}"'.format(text))
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
engine = pyttsx3.init('espeak')
# Set Rate
engine.setProperty('rate', 120)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()
def wishme ():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour < 10:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis Ma'am, Please tell me how may i help you ")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said{query}\n")
    except exception as e:
        print("Say that again Please....")
        return"None"
    return query

if __name__=="__main__" :
    wishme()
    # while True:
    if 1:
        query = takeCommand().lower()
        #Logic for executing queries
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = '//home//oem//Downloads//songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtime}")
