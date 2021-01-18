import pyttsx3 
import speech_recognition as sr 
import datetime 
import webbrowser
import os
import smtplib
import sys
import random 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate',175)
#choosing a female voice
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Maya, Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception:
        # print(e)
        #speak('i am trying to reconnect')
        print("Either you entered an elligible command or lost connection")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
       
        if 'hi maya' in query:
            speak('hi to you my friend')
            
        elif 'how are you' in query:
            speak('i am just fine, what about you?')
            
        elif 'open youtube' in query:
            webbrowser.open_new_tab('youtube.com')

        elif 'open google' in query:
            webbrowser.open_new_tab('google.com')

        elif 'open stack overflow' in query:
            webbrowser.open_new_tab('stackoverflow.com')   

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            print(len(songs),' Songs Found')    
            os.startfile(os.path.join(music_dir, songs[random.randint(0,len(songs))]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

            
        elif 'show command list' in query:
            speak('here is what i can do')
            print("""Command list:\nEmail To Harry\nPlay Music\nThe Time\nOpen Google\nOpen youtube\nOpen Stack Overflow\n""")
        
        elif 'bye-bye' in query:
            speak('bye-bye my good friend')
            sys.exit()

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harry2047@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend, I am not able to send this email")
                
        elif ' ' in query :
                 speak(f"sorry i can not do {query} yet it is not in my pre-programmed commands, to show you what i can do say show command list")
        
        elif '' in query:
                speak('did you say something? if you did i did not catch it i am sorry')
                print('Failed to reconnect...try again some other time')
                sys.exit()
                
            