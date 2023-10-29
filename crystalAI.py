import pyttsx3
import datetime
import pywhatkit
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import pyjokes
import time
import random

words = ["play music", "send emails","tell some jokes", " search wikipedia" , " browse google", "what can i do for you"]

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[-1].id)
engine. setProperty("rate", 130)
# tif function tells progrema to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon")
    else:
        speak("Good Evening")
    speak("This is crystal, How may i help you")
    
def send_email(to,content):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('primemember248@gmail.com','123qwe@456rty')
    server.sendmail('indradhanushhs@gmail.com',
                  to,
                  content)

    server.quit()
def takeCommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        print("suggested commands: ",random.choice(words),";",random.choice(words))
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
wish()
while True:
    query = takeCommand().lower()

    if "wikipedia" in query:
        print("Searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif "open" in query:
        list(query)
        web,web1 = query.split()
        web1 = web1.lower()
        web2 = web1 +".com"
        print(f"opening{web1}")
        speak(f"opening{web1}")
        time.sleep(1)
        webbrowser.open(web2)
    elif "time" in query:
        hour = int(datetime.datetime.now().hour)
        print(hour)
        speak(hour)
    elif "play" in query: 
        v = query.replace('play', '')                                 
        a = f"playing{v}..."
        print(a)
        speak(a)
        pywhatkit.playonyt(v)
    elif "what can you do" in query:
        a = "i can play music, i can send emails,i can tell some jokes, i can search wikipedia and i can browse google, what can i do for you"
        print(a)
        speak(a)
        
    elif "email" in query:
        try:  
            z = "To whom should i send: "
            speak(z)
            a = input(z)
            if "@gmail.com" in a:
                speak("What should i say??")
                b = takeCommand()
                send_email(a,b)
                print("Your email has been sent")
                speak("Your email has been sent")
            else:
                print("the gmail is incorrect")
                speak("the gmail is incorrect")
        except Exception as e:
            print(e) 
    elif "joke" in query:
        a1 = pyjokes.get_joke()
        print(a1)
        speak(a1)
    elif "search" in query or "google" in query:
        if "search" in query:
            a = query.replace("search","")
            webbrowser.open(a)
        elif "google" in query:
            a = query.replace("google","")
            webbrowser.open(a)
            
    else:
        speak("Sorry, I can't understand what you said" )