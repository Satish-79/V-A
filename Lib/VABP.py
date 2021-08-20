import speech_recognition as sr
import webbrowser
import time
from datetime import date
import pyttsx3
import os
import wolframalpha
import requests
import pyjokes
from PyQt5.QtCore import *
#from test2 import *


#object for speech recignition
rec = sr.Recognizer()

#object for text to speech:
tts = pyttsx3.init()


# threads class
class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
        self.run()

    def run(self):

        time.sleep(1)
        self.text_out = "how may i help you?"
        self.speak()
        while 1:
            self.getcommand()
            self.response()
            self.speak()

    # function voice input to text
    def getcommand(self, ask=False):
        with sr.Microphone() as mic:
            #set the status listening here
            if ask:
                print(ask)
            self.voice_in = rec.listen(mic)
            self.voice_data = ''
            try:
                self.voice_data = rec.recognize_google(self.voice_in)
                print(self.voice_data)
            except sr.UnknownValueError:
                print('sorry, not understandable')
            except sr.RequestError:
                print('sorry , service unavailable')
            #return self.voice_data

    #funtion for text to speech
    def speak(self):
        print(self.text_out)
        tts.setProperty('volume', 1.0)
        tts.setProperty('rate', 125)
        self.voices = tts.getProperty('voices')
        tts.setProperty('voice', self.voices[0].id)
        tts.say(self.text_out)
        tts.runAndWait()

    def get_temp(self):
        #API ID: 76ababf608808a939dd961a3e8adea29
        resp = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?appid=76ababf608808a939dd961a3e8adea29&q=Faridabad")
        weather = resp.json()
        if (weather['cod']) == '404':
            self.temp = "error"
        else:
            weather_data = weather['main']
            self.temp = str(int(weather_data["temp"] - 273)) +u"\N{DEGREE SIGN} C"
        return(self.temp)


    # for command processing
    def response(self):
        self.text_out = ' '
        self.voice_data = self.voice_data.lower()

        # for general features
        if 'your name' in self.voice_data:
            self.text_out = 'my name is Dumboo'
        elif 'the time' in self.voice_data:
            self.text_out = time.strftime("%I:%M %p  ")
        elif 'the date' in self.voice_data:
            self.text_out = date.today().strftime("%B %d, %Y")
        elif 'joke' in self.voice_data:
            self.text_out = pyjokes.get_joke()
        elif 'current location' in self.voice_data:
            self.text_out = "Faridabad "
        elif 'temperature' in self.voice_data:
            self.text_out = self.get_temp() + 'elcius'
        elif 'shutdown' in self.voice_data:
            pass#os.system("shutdown /s /t 5")

        # to open applications
        elif 'open' in self.voice_data:
            if 'file explorer' in self.voice_data:
                self.exe_path = "C:\\Windows\\explorer.exe"
                os.startfile(self.exe_path)
                self.text_out = "opening..."
            elif 'notepad' in self.voice_data:
                self.exe_path = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(self.exe_path)
                self.text_out = 'opening...'
            elif 'word' in self.voice_data:
                self.exe_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
                os.startfile(self.exe_path)
                self.text_out = 'opening...'
            elif 'excel' in self.voice_data:
                self.exe_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
                os.startfile(self.exe_path)
                self.text_out = 'opening...'
            elif 'setting' in self.voice_data:
                self.exe_path = "C:\\Windows\\System32\\control.exe"
                os.startfile(self.exe_path)
                self.text_out = 'opening...'
            elif 'paint' in self.voice_data:
                self.exe_path = "C:\\Windows\\system32\\mspaint.exe"
                os.startfile(self.exe_path)
                self.text_out = 'opening...'
            elif 'chrome' in self.voice_data:
                self.exe_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(self.exe_path)
                self.text_out = 'opening...'
            elif 'command prompt' in self.voice_data:
                self.exe_path = "C:\\Windows\\system32\\cmd.exe"
                os.startfile(self.exe_path)
                self.text_out = 'opening...'

            else:
                self.text_out = 'unable to open'

        # to open web applications
        elif 'what' in self.voice_data or 'who' in self.voice_data or 'where' in self.voice_data:
            self.client = wolframalpha.Client('G74W9A-AH9UUXPAH7')
            self.res = self.client.query(self.voice_data)
            self.text_out = next(self.res.results).text


        elif 'search' in self.voice_data:
            self.voice_data = self.voice_data.replace('search', '')
            self.voice_data = self.voice_data.replace(' ', '+')
            self.url = 'https://google.com/search?q=' + self.voice_data
            webbrowser.get().open(self.url)
            self.text_out = "here is what i found"
        elif 'youtube' in self.voice_data:
            self.url = 'https://www.youtube.com/'
            webbrowser.get().open(self.url)
            self.text_out = "here is it"
        elif 'facebook' in self.voice_data:
            self.url = 'https://www.facebook.com/'
            webbrowser.get().open(self.url)
            self.text_out = "here is it"
        elif 'instagram' in self.voice_data:
            self.url = 'https://www.instagram.com/'
            webbrowser.get().open(self.url)
            self.text_out = "ok here it is..."
        elif 'map' in self.voice_data:
            self.url = 'https://www.google.com/maps'
            webbrowser.get().open(self.url)
            self.text_out = "here are the results"
        elif 'find direction' in self.voice_data:
            self.voice_data = self.voice_data.replace('find direction to', '')
            self.voice_data = self.voice_data.replace(' ', '+')
            self.url = 'https://www.google.com/maps/dir/348%2FB,+Shiv+Durga+Vihar,+Faridabad,+Haryana+121009,+India/' + self.voice_data
            webbrowser.get().open(self.url)
            self.text_out = "here are the results"
        elif 'locate' in self.voice_data:
            self.voice_data = self.voice_data.replace('locate', '')
            self.voice_data = self.voice_data.replace(' ', '+')
            self.url = 'https://www.google.com/maps/place/' + self.voice_data
            webbrowser.get().open(self.url)
            self.text_out = "here is it"

        elif 'play' in self.voice_data or 'news' in self.voice_data:
            self.text_out = 'feature will be available soon!!'

        elif 'close word' in self.voice_data:
            self.voice_data = self.voice_data.replace('close', '')
            self.text_out = "closing" + self.voice_data
            os.system("taskkill /f /im " + "WINWORD.exe")
        elif 'close' in self.voice_data:
            self.voice_data = self.voice_data.replace('close', '')
            self.voice_data = self.voice_data.replace('file ', '')
            self.voice_data = self.voice_data.replace('google ', '')
            self.voice_data = self.voice_data.replace('paint', 'mspaint')
            self.text_out = "closing" + self.voice_data
            os.system("taskkill /f /im " + self.voice_data + ".exe")

        elif 'exit' in self.voice_data:
            self.text_out = 'service stopped...'
            self.speak()
            exit()
        else:
            self.text_out = 'unable to fetch'
        #return text_out


    #main part
    def activate(self):
        time.sleep(1)
        tts.say("how may i help you?")
        while 1:
            self.getcommand()
            self.response()
            self.speak()



abc = MainThread()
abc.start()