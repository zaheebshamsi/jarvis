import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser as wb
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio): #takes a string and then says it
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Assalamualaikum! kem chho")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("This is Just A Rather Very Intelligent System aka JARVIS")

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said ", query)

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('zaheeb.shamsi120815@gmail.com','necessary changes required')
    server.sendmail('zaheeb.shamsi120815@gmail.com',to,content)
    server.close()

    

    

if __name__ == "__main__":
    speak("Laal phool peela phool Zaheeb Bhaiya Beutiful")
    wishMe()

    while True:
    
        query = takeCommand().lower()

        #Logic for executiong task based on query

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2) #sentences specifies how many sentence from wiki you want jarvis to speak
            speak("According to wikipedia")
            print(results.encode('utf-8'))
            speak(results)

        elif 'open youtube' in query:
            wb.open("youtube.com")

        elif 'open google' in query:
            wb.open("google.com")

        elif 'open stack overflow' in query:
            wb.open("stackoverflow.com")

        elif 'gana bajao' in query:
            music_dir = 'Z:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%Hhour%Mminutes%Sseconds")
            speak(f"The time is{strTime} ")
            print(strTime)

        elif 'code' in query:
            codePath = "C:\\Users\\ZZZShamsi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'chrome' in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif 'quit' in query:
            exit()

        elif 'email to me' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "zaheeb.shamsi120815@gmail"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Zaheeb bhaiya...Email has not been sent ")

