import speech_recognition as sr
from ia_speak import speak
import pyaudio
import requests
import sys

mic = sr.Recognizer()
arduino_ip = "192.168.197.222"
urlOn = f"http://{arduino_ip}/on"
urlOff = f"http://{arduino_ip}/off"

def audio_to_text():

   while True: 
      with sr.Microphone() as source:
         mic.adjust_for_ambient_noise(source) #reduce ambient noise
         speak("How can I help you?")
         audio = mic.listen(source) #listens do the microphone source

      try:
         audio_text = mic.recognize_google(audio, language='pt-BR').lower()
         print(audio_text)

         if 'ligar' in audio_text and 'sala' in audio_text and 'des' not in audio_text:  
            speak('Ok')  
            try:
                response = requests.get(urlOn)
                if response.status_code == 200:
                    print("Request successful")
                    print(response.text)
                else:
                    print(f"Failed to connect to Arduino server. Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")

         elif 'ligar' in audio_text and 'des' in audio_text and 'sala' in audio_text:
            speak('Ok')  
            try:
                response = requests.get(urlOff)
                if response.status_code == 200:
                    print("Request successful")
                    print(response.text)
                else:
                    print(f"Failed to connect to Arduino server. Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")

         else:
            speak('Command not found, please try again')

      except sr.UnknownValueError:
         print("Not activated")
      
      except sr.RequestError as e:
        print("Erro ao requisitar resultados do serviço de reconhecimento de fala; {0}".format(e))



audio_to_text()