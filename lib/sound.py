import os
import speech_recognition as sr

r = sr.Recognizer()


class Sound():
    def __init__(self):
        self.input = 'text'

    def setInput(self, value):
        self.input = value

    def play(self, filePath: str):
        os.system("afplay " + filePath)

    def say(self, string: str):
        if self.input == 'text':
            print(string)
        else:
            os.system("say " + string)

    def listenTo(self) -> str:
        if self.input == 'text':
            return input('текст: ')
        else:
            with sr.Microphone() as source:
                audio_text = r.listen(source)
                print("end of listening. processing..")
                try:
                    return r.recognize_google(audio_text, language="en-US")
                except:
                    return 'unrecognizable'
