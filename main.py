import speech_recognition as sr
from ia_speak import speak
import serial 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

mic = sr.Recognizer()
ser = serial.Serial('COM3', 9600) #change port

def audio_to_text():

   while True: 
      with sr.Microphone() as source:
         mic.adjust_for_ambient_noise(source) #reduce ambient noise
         speak("How can I help you?")
         audio = mic.listen(source) #listens do the microphone source

      try:
         audio_text = mic.recognize_google(audio, language='pt-BR').lower()
         print(audio_text)

         if 'ligar' in audio_text and 'quarto' in audio_text and 'des' not in audio_text:  
            speak('Ok')
            ser.write(b'1') #sends it to serial

         elif 'desligar' in audio_text and 'quarto' in audio_text:
            speak('Ok')
            ser.write(b'2')

         elif 'ligar' in audio_text and 'cozinha' in audio_text and 'des' not in audio_text:
            speak('Ok')
            ser.write(b'3')

         elif 'desligar' in audio_text and 'cozinha' in audio_text:
            speak('Ok')
            ser.write(b'4')

         elif 'ligar' in audio_text and 'sala' in audio_text and 'des' not in audio_text:
            speak('Ok')
            ser.write(b'5')

         elif 'desligar' in audio_text and 'sala' in audio_text:
            speak('Ok')
            ser.write(b'6')

         elif 'finish' in audio_text:
            speak("See you next time")
            break

         else:
            speak('Command not found, please try again')

      except sr.UnknownValueError:
         print("Not activated")
      
      except sr.RequestError as e:
        print("Erro ao requisitar resultados do serviço de reconhecimento de fala; {0}".format(e))

def start_button_clicked():
   audio_to_text()

def main():
   app = QApplication(sys.argv)
   window = QWidget()
   window.setWindowTitle('Simple Frontend')
   start_button = QPushButton('Start', window)
   start_button.clicked.connect(start_button_clicked)
   start_button.setGeometry(50, 50, 100, 50)
   window.show()
   sys.exit(app.exec_())
   
main()
ser.close()
