from playsound import playsound
import eel

#Playing assistant sound function

@eel.expose
def playAssistantSound():
    music_dir ="www\\assets\\audio\\tone-beep.mp3"
    playsound(music_dir)