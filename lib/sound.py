import os
import platform
import speech_recognition as sr

r = sr.Recognizer()


class Sound():
    def __init__(self):
        self.input = 'text'

    def setInput(self, value):
        self.input = value

    def play(self, filePath: str):
        if platform.system() == 'Linux':
            os.system("mpg123 " + filePath)
        elif platform.system() == 'Darwin':
            os.system("afplay " + filePath)
        elif platform.system() == 'Windows':
            os.system(
                f"powershell -c (New-Object Media.SoundPlayer '{filePath}').PlaySync();")
        else:
            print(
                f"the hell os are you on? i can't play sound. would you kindly open it by yourself? \npath is {filePath}")

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
