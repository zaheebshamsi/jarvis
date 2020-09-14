import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser as wb
import os
#import smtplib
import winsound

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
newRate = engine.setProperty('rate', 165)
volume = engine.getProperty('volume')

engine.setProperty('voice',voices[0].id)

#print(voices)
#print(rate)
#print(newRate)
#print(volume)

    #######################################################################################################################
    #                                          Function Definition                                                        #
    #######################################################################################################################


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....... Haan Haan Sun rahe hain\n")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing... Ab samajh rahe hain kya bawaseer faila rahe ho\n")
        query = r.recognize_google(audio, language='en-in')
        print("Aapne bhoka:", query)

    except Exception as e:
        print(e)

        print("Say that again please... Hain ????????\n")
        return "None"
    return query
    
    
def speak(audio): #takes a string and then says it
    engine.say(audio)
    engine.runAndWait()
    
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Zaheeb")

    elif hour>=12 and hour<18:
        speak("Good afternoon Zaheeb")

    else:
        speak("Good evening Zaheeb")

    speak("please tell what would you like me to do after the beep")
    winsound.PlaySound("beep-08b.wav", winsound.SND_ASYNC)
    
    
def fileHandling():
    f = open("t1.txt" , "r")
    speak(f.read())
    print(f.read())
    
    
    #######################################################################################################################
    #                                          Code starts from here                                                      #
    #######################################################################################################################

if __name__ == "__main__":
    speak("I am JARVIS aka Just A Rather Very Intelligent System")
    wishMe()
    
    
    print("Press Ctrl-C to shut-down JARVIS")
    
    

    while True:
        
        query = takeCommand().lower()
            
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
            
            
        elif 'play a song' in query:
            music_dir = 'Z:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
            
            
        elif 'gana bajao' in query:
            music_dir = 'Z:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
            
            
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H hour %M minutes %S seconds")
            speak(f"The time is{strTime} \n")
            print(strTime)
            
            
        elif 'shut down' in query:
            exit()
            
            
        elif 'file handling' in query:
            fileHandling()
            break