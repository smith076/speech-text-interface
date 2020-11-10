import pyttsx3 

engine = pyttsx3.init() 
rate=engine.getProperty('rate')
engine.setProperty('rate', rate-7)
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')
engine.say("I love Python for text to speech, and you?") 
engine.runAndWait() 