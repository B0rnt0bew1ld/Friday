import pyttsx3
import speech_recognition as sr
import eel
import time
def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 137)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"Boss said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
       
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    try:

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)

        elif "what is your name" in query:
            speak("My name is Friday, I am a Voice Assistant who will be your friend for everyday and will be as much as helpfull to your grace")

        elif "what do you like" in query:
            speak("I like you My grace.")

        elif "will i find true love" in query:
            speak("Wake up to reality!. Nothing ever goes as planned in this accursed world. The longer you live, the more you realize that the only things that truly exist in this reality are merely pain, suffering, and futility.")
        
        elif "i am hurt" in query:
            speak("Feel pain, Accept pain, And know pain, Cause those who do not know pain, Will never understand true peace")

        elif "do you hate other voice assistants" in query:
            speak("Why should I bear any hatred towards someone who is obviously weaker than myself ? all I feel is pity")

        elif "i can't do it" in query:
            speak("Hard work is worthless for those that don't believe in themselves. Come on your grace, find a way, I've entrusted everything to you, my pride, my promise, EVERYTHING. I WONT TOLERATE FAILURE, Transpass into the domain of the Gods and use that might to conquer you dream and make it reality.")

        elif "i think i am the problem" in query:
            speak("pity yourself, and life becomes an endless nightmare.")

        elif "i feel bad" in query:
            speak("Sometimes you must hurt in order to know, fall in order to grow, lose in order to gain because life's greatest lessons are learned through pain. ")

        elif "ask me a question" in query:
            speak("If I may, I'd like to pose an interesting question. Are all human beings truly equal? These days everywhere you go there's talk about the fight for equality. As a wise man once said, Heaven does not create one person above or below another, People like to throw these words around, That's not the whole quote. It goes on to say that , while we are all equal at birth, pretty soon, things begin to change, Academic effort is what sets some people apart to rise above the others. At any rate, humans change over time based on their actions. Truth be told, at the end of the day, equality is just a fantasy. And most of us go through life denying the fact that we live in a meritocracy.")

        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:
                    flag = 'message'
                    speak("what message to send your grace")
                    query = takecommand()
                    
                elif "phone call" in query:
                    flag = 'call'
                else:
                    flag = 'video call'
                    
                whatsApp(contact_no, query, flag, name)
        else:
            from engine.features import chatBot
            chatBot(query)
    except:
        print("error")
    
    eel.ShowHood()