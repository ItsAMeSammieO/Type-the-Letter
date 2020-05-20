import random
import string
import os
import time
import playsound
from gtts import gTTS

letter = random.choice(string.ascii_lowercase)

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "question.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove("question.mp3")

speak("Type this letter: " + letter)
answer = str(input("What letter was said?"))

if answer == letter:
    speak("You typed the right letter!")
elif answer != letter:
    speak("That wasn't the right letter. The right letter was " + letter)
