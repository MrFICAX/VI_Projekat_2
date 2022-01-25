# Import the required module for text
# to speech conversion
from typing import Counter
from gtts import gTTS
#from mpyg321.mpyg321 import MPyg321Player
#player = MPyg321Player()
import playsound

# This module is imported so that we can
# play the converted audio
import os
class Alexa2:
    # The text that you want to convert to audio
 
    counter = 0
    TopCounter = 5
    def SaySomething(self, text, language, speed):

        # mytext = 'Боже правде Боже правде, ти што спасе од пропасти досад нас, чуј и одсад наше гласе и од сад нам буди спас. Моћном руком води, брани будућности српске брод, Боже спаси, Боже храни, српске земље, српски род!'
        # mytext = "СПАСИБО ПОДРУГ!"
        # mytext = "Pristup nije odobren!"
        # mytext = "We play football!"
        # Language in which you want to convert
        #Example: language = 'en' or language = 'ru'
        # Passing the text and language to the engine,
        # here we have marked slow=False. Which tells
        # the module that the converted audio should
        # have a high speed
        myobj = gTTS(text=text, lang=language, slow=speed)

        # Saving the converted audio in a mp3 file named
        # welcome
        self.counter += 1
        if self.TopCounter <= self.counter:
            self.counter = 0
        myobj.save("./SoundsLibrary/welcome"+str(self.counter)+".mp3")
        playsound.playsound('./SoundsLibrary/welcome'+str(self.counter)+'.mp3', True)


