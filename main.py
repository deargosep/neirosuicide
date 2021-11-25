import sys
from lib.sound import Sound
from data.json import read, check

# initializing things
sound = Sound()
args_length = len(sys.argv)
# print(f"args length: {args_length}")


class Talk(object):
    def __init__(self):
        if args_length >= 3:
            self.depression = int(sys.argv[2])
        else:
            self.depression = 0
        if args_length >= 2:
            self.input = sys.argv[1]
        else:
            self.input = 'text'
        sound.setInput(self.input)
        print("input type:", self.input)
        print("depression level:", self.depression)
        self.checkDie()

    def setInput(self, value: str):
        self.input = value
        sound.setInput = value

    def increment(self, value=1):
        self.depression += value
        print("\nуровень депрессии:", self.depression)
        sound.say('ай блять')
        self.checkDie()

    def decrement(self, value=1):
        self.depression -= value
        print("\nуровень депрессии:", self.depression)
        sound.say('спасибо')
        self.checkDie()

    def reset(self):
        self.depression = 0
        print('reseted')

    def checkDie(self):
        if self.depression >= 10:
            self.die()

    def die(self):
        sound.say('блять. заебало. всё, пока.')
        sound.play("assets/gunshot.m4a")
        sys.exit()


siri = Talk()


def main():
    sound.say('привет, напиши или скажи мне что нибудь ')
    userType = sound.listenTo()
    sound.say("читаю: " + userType)
    sound.say('хм..')
    result = check(userType)
    if result == 'bad' or result == 'Negative':
        siri.increment()
    elif result == 'good' or result == 'Positive':
        siri.decrement()
    elif result == 'good' or result == 'Neutral':
        sound.say('ok..?')
    elif hasattr(result, 'id'):
        sound.say(result['choices'][0]['text'].strip())
    else:
        sound.say('чего?')


while True:
    main()
