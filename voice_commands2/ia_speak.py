import speech_recognition as src
import pyttsx3

text_speaker = pyttsx3.init()

def speak(audio):
   
   text_speaker.setProperty('rate', 170)
   voices = text_speaker.getProperty('voices')
   text_speaker.setProperty('voice', voices[1].id) #sets the voice to the index 1 in voices

   text_speaker.say(audio)
   text_speaker.runAndWait()

   return speak