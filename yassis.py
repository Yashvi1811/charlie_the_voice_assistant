import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

### ** boy voice
# print(voices[0].id)
# engine.setProperty('voice',voices[0].id)

### ** girl voice
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")  
    else:
        speak("good evening")
    speak("I am  charlie please tell me how may i help you")     
def takeCommand():
    r=sr.Recognizer()  
    with sr.Microphone()as source:
       print("Listening....")
       r.pause_threshold = 1
       audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        # print(e)
        print("say again please.....")
        return "None"      
    return query 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()    
    
            

if __name__=="__main__":
    # speak(" HII  i am yashvi bansal from meerut")
    wishMe()
    # takeCommand()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('seacching wikipedia')
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentence=1)
            speak("According to wikipedia")
            print(results)
            # speak(results)
        elif'play music' in query:
            music_dir = 'D:\my music' 
            songs= os.listdir(music_dir)
            print(songs)   
            os.startfile(os.path.join(music_div,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}") 
        elif 'open code' in query:
            codePath = "C:\\Users\\yashv\\OneDrive\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codePath)
        elif 'email to yashvi' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yashvibansal1811@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry mam! I am not able to send this email")    


