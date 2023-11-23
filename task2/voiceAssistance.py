import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices [1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning! Durgesh yadav")
        
    elif hour>=12 and hour<18:
        speak("good afternoon! Durgesh yadav")
    
    else:
        speak("good evening! Durgesh yadav")
        
    speak(" Hello Sir I am  your personal Assistance. Please tell me how can I help you ")
    
def takeCommand():
    # it takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1     #secconds of non-speaking audio before a phrase is considered completed
        audio=r.listen(source)
    try:
        print("Recognising..........")
        query = r.recognize_google(audio,language='en-in')      #use google's engine
        print(f"Durgesh said: {query}\n")
    except Exception as e:
        # print(e)
        print("please!! say it again")
        return 'None' # it will return the none string
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('durgeshkyadav04@gmail.com','Durgesh@321')
    server.sendmail('durgeshkyadav1998@gmail.com', to ,content )
    server.close()
    


if __name__ =="__main__":
    wishMe()
    if 1:
        query =takeCommand().lower()
         
        # logic for executing tasks base on query
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtub'  in query:
            webbrowser.open("youtube")   
        
        elif 'open google' in query:
            webbrowser.open("google.com") 
            
        elif 'open stackover' in query:
            webbrowser .open ("stackoverflow.com")
            
        elif ' the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is{strTime} ")
            
        elif 'open code' in query:
            codePath = "C:\\Users\\durgesh yadav\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'play music' in query:
            music_dir = 'D:\\music '
            songs = os.listdir (music_dir) 
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            
        elif 'email to durgesh' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "durgeshkyadav04@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as  e:
                print(e)
                speak("sorry my friend durgesh .I am not able to send this email")