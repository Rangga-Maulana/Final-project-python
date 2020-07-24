import sys
import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
import playsound
from subprocess import run
from pyowm import OWM
from gtts import gTTS
import youtube_dl
import urllib
import urllib3
import urllib.request
import pyttsx3
import json
from bs4 import BeautifulSoup as soup
import urllib.request
import wikipedia
import random
import time
from subprocess import PIPE, run
from time import strftime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.setMinimumSize(QSize(200, 50))    
        self.setWindowTitle("Mitsuha")

        pybutton = QPushButton('START', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100,25)
        pybutton.move(50, 40)

        day_time = int(strftime('%H'))
        if day_time < 12:
            mytext = 'Hai Rangga. Selamat Pagi!'
            language = 'ID'
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("gmorning.mp3")
            playsound.playsound("C:/Users/User/Documents/gmorning.mp3")
            os.remove("gmorning.mp3")

        elif day_time <= 18:
            mytext = 'Hai Rangga. Selamat Sore!'
            language = 'ID'
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("gafternoon.mp3")
            playsound.playsound("C:/Users/User/Documents/gafternoon.mp3")

        else:
            mytext = 'Hai Rangga. Selamat Malam'
            language = 'ID'
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("gevening.mp3")
            playsound.playsound("C:/Users/User/Documents/gevening.mp3")

            

    def clickMethod(self):
        mytext = 'Hai Rangga. Ucapkan sesuatu!'
        language = 'ID'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("cihelp.mp3")
        playsound.playsound("C:/Users/User/Documents/cihelp.mp3")
        os.remove("cihelp.mp3")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            mytext = 'tunggu sebentar'
            language = 'ID'
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("ooss.mp3")
            playsound.playsound("C:/Users/User/Documents/ooss.mp3")
            
        except sr.UnknownValueError:
            command = r.recognize_google(audio).lower()
            mytext = 'tolong ulangi'
            language = 'ID'
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("oosads.mp3")
            playsound.playsound("C:/Users/User/Documents/oosads.mp3")

            command = myCommand();
            
        dialog = QMessageBox(self)

        dialog.setWindowTitle('Mitsuha')
        dialog.setText('You said: ' + command + '\n')

        dialog.setMinimumHeight(500)
        dialog.setSizeIncrement(1, 1)
        dialog.setSizeGripEnabled(True)

        dialog.show()


        
        if 'open' in command:
            reg_ex = re.search('open (.+)', command)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                url = 'https://www.' + domain + '.com'
                webbrowser.open(url)
                mytext = 'situs yang kamu inginkan sudah dibuka!'
                language = 'ID'
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("oopn.mp3")
                playsound.playsound("C:/Users/User/Documents/oopn.mp3")
                
        elif 'who are you' in command:
                mytext = 'Saya Mitsuha, Saya adalah personal asisten!'
                language = 'ID'
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("ooks.mp3")
                playsound.playsound("C:/Users/User/Documents/ooks.mp3")

            
        elif 'can you run' in command:
            reg_ex = re.search('can you run (.*)', command)
            if reg_ex:
                appname = reg_ex.group(1)
                appname1 = appname+".exe" 
                filepath = appname1
                os.startfile(filepath)
                mytext = 'aplikasi yang kamu inginkan sudah dibuka!'
                language = 'ID'
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("ootk.mp3")
                playsound.playsound("C:/Users/User/Documents/ootk.mp3")

        elif 'shutdown' in command:
                mytext = 'siap!'
                language = 'ID'
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("ootk21.mp3")
                playsound.playsound("C:/Users/User/Documents/ootk21.mp3")
                os.system("shutdown now -h")
            
                
  
                    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
