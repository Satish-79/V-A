import speech_recognition as sr
import webbrowser
import time
from datetime import date
import pyttsx3
import os
import pyjokes

rec = sr.Recognizer()


# for voice input to text
def getcommand(ask=False):
    with sr.Microphone() as mic:
        # set the statu listening here
        if ask:
            print(ask)
        voice_in = rec.listen(mic)
        voice_data = ''
        try:
            voice_data = rec.recognize_google(voice_in)
            print(voice_data)
        except sr.UnknownValueError:
            print('sorry, not understandable')
        except sr.RequestError:
            print('sorry , service unavailable')
        return voice_data


# for text to speech:
tts = pyttsx3.init()


def speak(text_data):
    print(text_data)
    tts.setProperty('volume', 1.0)
    tts.setProperty('rate', 125)
    voices = tts.getProperty('voices')
    tts.setProperty('voice', voices[0].id)
    tts.say(text_data)
    tts.runAndWait()


# for command processing
def response(voice_data):
    text_out = ' '
    voice_data = voice_data.lower()

    # for general features
    if 'your name' in voice_data:
        text_out = 'my name is beerbal'
    elif 'the time' in voice_data:
        text_out = time.strftime("%I:%M %p  ")
    elif 'the date' in voice_data:
        text_out = date.today().strftime("%B %d, %Y")
    elif 'joke' in voice_data:
        text_out = pyjokes.get_joke()
    elif 'shutdown' in voice_data:
        pass#os.system("shutdown /s /t 5")

    # to open applications
    elif 'open' in voice_data:
        if 'file explorer' in voice_data:
            exe_path = "C:\\Windows\\explorer.exe"
            os.startfile(exe_path)
            text_out = "opening..."
        elif 'notepad' in voice_data:
            exe_path = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(exe_path)
            text_out = 'opening...'
        elif 'word' in voice_data:
            exe_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(exe_path)
            text_out = 'opening...'
        elif 'excel' in voice_data:
            exe_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(exe_path)
            text_out = 'opening...'
        elif 'setting' in voice_data:
            exe_path = "C:\\Windows\\System32\\control.exe"
            os.startfile(exe_path)
            text_out = 'opening...'
        elif 'paint' in voice_data:
            exe_path = "C:\\Windows\\system32\\mspaint.exe"
            os.startfile(exe_path)
            text_out = 'opening...'
        elif 'chrome' in voice_data:
            exe_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(exe_path)
            text_out = 'opening...'
        elif 'command prompt' in voice_data:
            exe_path = "C:\\Windows\\system32\\cmd.exe"
            os.startfile(exe_path)
            text_out = 'opening...'
        else:
            text_out = 'unable to open'

    # to open web applications
    elif 'search' in voice_data:
        voice_data = voice_data.replace('search', '')
        voice_data = voice_data.replace(' ', '+')
        url = 'https://google.com/search?q=' + voice_data
        webbrowser.get().open(url)
        text_out = "here is what i found"
    elif 'youtube' in voice_data:
        url = 'https://www.youtube.com/'
        webbrowser.get().open(url)
        text_out = "here is it"
    elif 'facebook' in voice_data:
        url = 'https://www.facebook.com/'
        webbrowser.get().open(url)
        text_out = "here is it"
    elif 'instagram' in voice_data:
        url = 'https://www.instagram.com/'
        webbrowser.get().open(url)
        text_out = "ok here it is..."
    elif 'map' in voice_data:
        url = 'https://www.google.com/maps'
        webbrowser.get().open(url)
        text_out = "here are the results"
    elif 'locate' in voice_data:
        voice_data = voice_data.replace('locate', '')
        voice_data = voice_data.replace(' ', '+')
        url = 'https://www.google.com/maps/place/' + voice_data
        webbrowser.get().open(url)
        text_out = "here is it"

    elif 'close' in voice_data:
        voice_data = voice_data.replace('close', '')
        voice_data = voice_data.replace('file ', '')
        speak("closing" + voice_data)
        os.system("taskkill /f /im " + voice_data + ".exe")

    elif 'exit' in voice_data:
        text_out = 'service stopped...'
        speak(text_out)
        exit()
    else:
        text_out = 'unable to fetch'
    return text_out



time.sleep(1)
speak("how may i help you?")
while 1:
    voice_data = getcommand()
    text = response(voice_data)
    speak(text)
