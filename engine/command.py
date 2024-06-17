import pyttsx3
import speech_recognition as sr
import eel


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate', 134)
    print(voices)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, timeout=10, phrase_time_limit= 6)

    try:
        print('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"Fri-Day thinks you said: {query}")
    
    except Exception as e:
        return ""
    
    return query.lower()

text = takecommand()



speak(text)