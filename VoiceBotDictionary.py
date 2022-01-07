import speech_recognition as sr  
import json
from difflib import get_close_matches
import pyttsx3
import datetime
data = json.load(open("data.json"))

def intro():

    speak("hey buddy i am your voice dictionary  bot say --jarvis-- to quit  ")
    print("hey buddy i am your voice dictionary  bot say --jarvis-- to quit  ")

def wishes():  
   hour = int(datetime.datetime.now().hour)
   if hour >=0 and hour<12:
       speak("happy morning")
       speak("have an nice day ")
   elif hour >=12 and hour < 16 :
      speak("good afternoon")
   elif hour  >=16 and  hour < 20:
      speak("good evening")   
   else:
      speak("good night have an sweet dreams")   

def ask():
    speak("please tell the word to find the meaning ")

def listenthecommand():
    global text
    r = sr.Recognizer()

    mic = sr.Microphone()
    with mic as source:
            print("Listening...")
            audio = r.record(source,duration=5)
            print("Recognize...")

    try:
                text = r.recognize_google(audio)
                print(f"user said: {text}")
                
            
    except sr.UnknownValueError:
                           
                 print("Don not hear anything")   
                 text =  listenthecommand()        
                         
    return text

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        print("Did you mean %s instead?  " % get_close_matches(w, data.keys())[0])
        print("please tell yes or no")
        listenthecommand()
        if text == "yes":
            return data[get_close_matches(w, data.keys())[0]]
        elif text == "no":
            return "The word doesn't exist. Please double check it."
            speak("The word doesn't exist. Please double check it.")
        else:
            return "We didn't understand your entry."
            speak("We didn't understand your entry.")
    else:
        return "The word doesn't exist. Please double check it."
        speak("The word doesn't exist. Please double check it.")

def speak(audio):
      engine = pyttsx3.init()
      rate=engine.getProperty('rate')
      engine.setProperty('rate',rate-50)
      engine.say(audio)     
      engine.runAndWait()

def main():
       ask()
       listenthecommand()
       output = translate(text)
       if type(output) == list:
           for item in output:
            print(item)
            speak(item)
            main()
       else:
            print(output)
            speak(output)
            main()

while True:
    intro()
    main()
    if text == "Jarvis":
        break
    
       