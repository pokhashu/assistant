# import random
# import datetime
# import webbrowser
# import pyttsx3
# import requests
# from bs4 import BeautifulSoup as bs
# import wikipedia as wiki
# import speech_recognition as sr
# import time
# import win32com.client
# import subprocess
# from pygame import mixer

import pyttsx3

voice = pyttsx3.init()
voice.setProperty('rate', 175)
voice.setProperty('volume', 0.9)
voice.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Irina')

def say(string):
    voice.say(str(string))
    voice.runAndWait()

say('Hello')
say('привет мир')
say(5)
say(True)