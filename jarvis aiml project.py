import tkinter as tk
import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # ... (existing code)

    if 'time' in query:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am jarvis maam. Please tell me how may I help you")

def takeCommand():
    #it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: ,{query}\n" )

    except Exception as e:
        # print(e)
        print("Say that again please...")
         
        return "None"
    return query.lower()

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.mitwpu.edu.in',587)
    server.ehlo()
    server.starttls()
    server.login('1032211352@mitwpu.edu.in', 'rudra@2320')
    server.sendmail('1032211352@mitwpu.edu.in', to,content)
    server.close()


if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand()
    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("Wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    import subprocess

# ...

if 'open linkedin' in query:
     webbrowser.open_new_tab("https://www.linkedin.com")

elif 'open google' in query:
   webbrowser.open_new_tab("https://www.google.com")

elif 'open youtube' in query:
    webbrowser.open_new_tab("https://www.youtube.com")

elif 'open mit website' in query:
    webbrowser.open_new_tab("https://www.mitwpu.edu.in")

elif 'open gmail' in query:
    webbrowser.open_new_tab("https://www.gmail.com")

elif 'open spotify' in query:
    webbrowser.open_new_tab("https://www.spotify.com")


elif 'play music' in query:
    music_dir = 'C:\\Users\\Rudra\\OneDrive\\Desktop\\music'
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir, songs[0]))

elif 'the time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Maam, the time is{strTime}")

elif 'email to rushita' in query:
    try:
        speak("What should I say?")
        content = takeCommand()
        to = "1032211352@mitwpu.edu.in"
        sendEmail(to, content)
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry maam . I am not able to send this email")


   




    


    
