import pyttsx3

engine = pyttsx3.init('sapi5')
sounds = engine.getProperty('voices')
engine.setProperty('rate',100)
engine.setProperty('voice',sounds[1].id)

def voice(script):
    engine.say(script)
    engine.runAndWait()

