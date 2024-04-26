"""from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot"""

import os

import speech_recognition as sr

"""bot = ChatBot()

bot.set_trainer(ListTrainer)

for _file in os.listdir('Giramille'):
    lines = open('Giramille/Giramille-IA/' + _file, 'r').readlines()

    bot.train(lines) 
"""
r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)

    while True:
        audio = r.listen(s)

        speech = r.recognize_google(audio, language='pt-br', show_all = True )

        print('falas: ', speech)
        """print('dublagem: ', bot.get_response(speech))"""