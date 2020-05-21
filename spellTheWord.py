import random
import string
import os
import time
import playsound
from gtts import gTTS

yes = 'yes'

while yes == 'yes':
    letter = random.choice(string.ascii_lowercase)


    def speak(text):
        tts = gTTS(text=text, lang="en")
        filename = "question.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove("question.mp3")

    speak("Type this letter: " + letter)
    answer = str(input("What letter was said? "))



    if answer == letter:
        print("You typed the right letter!")
        speak("You typed the right letter!")
    elif answer != letter:
       print("That wasn't the right letter. The right letter was " + letter)
       speak("That wasn't the right letter. The right letter was " + letter)

    speak("Do you want to keep playing?")
    yes = input("Do you want to keep playing? ")

    if yes == 'no':
        print("Thanks for playing!")
        speak("Thanks for playing!")